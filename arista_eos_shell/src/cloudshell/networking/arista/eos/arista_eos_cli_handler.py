import re
import time

from cloudshell.cli.command_mode_helper import CommandModeHelper
from cloudshell.networking.arista.eos.arista_eos_command_modes import AristaEOSDefaultCommandMode, \
    AristaEOSEnableCommandMode, AristaEOSConfigCommandMode
from cloudshell.networking.cli_handler_impl import CliHandlerImpl
from cloudshell.shell.core.api_utils import decrypt_password_from_attribute


class AristaEOSCliHandler(CliHandlerImpl):
    def __init__(self, cli, context, logger, api):
        super(AristaEOSCliHandler, self).__init__(cli, context, logger, api)
        modes = CommandModeHelper.create_command_mode(context)
        self.default_mode = modes[AristaEOSDefaultCommandMode]
        self.enable_mode = modes[AristaEOSEnableCommandMode]
        self.config_mode = modes[AristaEOSConfigCommandMode]

    def on_session_start(self, session, logger):
        """Send default commands to configure/clear session outputs
        :return:
        """

        self.enter_enable_mode(session=session, logger=logger)
        session.hardware_expect('terminal length 0', AristaEOSEnableCommandMode.PROMPT, logger)
        session.hardware_expect('terminal width 300', AristaEOSEnableCommandMode.PROMPT, logger)
        # session.hardware_expect('terminal no exec prompt timestamp', EnableCommandMode.PROMPT, logger)
        self._enter_config_mode(session, logger)
        session.hardware_expect('no logging console', AristaEOSConfigCommandMode.PROMPT, logger)
        session.hardware_expect('exit', AristaEOSEnableCommandMode.PROMPT, logger)

    def _enter_config_mode(self, session, logger):
        max_retries = 5
        error_message = 'Failed to enter config mode, please check logs, for details'
        output = session.hardware_expect(AristaEOSConfigCommandMode.ENTER_COMMAND,
                                         '{0}|{1}'.format(AristaEOSConfigCommandMode.PROMPT, AristaEOSEnableCommandMode.PROMPT), logger)

        if not re.search(AristaEOSConfigCommandMode.PROMPT, output):
            retries = 0
            while not re.search(r"[Cc]onfiguration [Ll]ocked", output, re.IGNORECASE) or retries == max_retries:
                time.sleep(5)
                output = session.hardware_expect(AristaEOSConfigCommandMode.ENTER_COMMAND,
                                                 '{0}|{1}'.format(AristaEOSConfigCommandMode.PROMPT, AristaEOSEnableCommandMode.PROMPT),
                                                 logger)
            if not re.search(AristaEOSConfigCommandMode.PROMPT, output):
                raise Exception('_enter_config_mode', error_message)

    def enter_enable_mode(self, session, logger):
        """
        Enter enable mode

        :param session:
        :param logger:
        :raise Exception:
        """
        result = session.hardware_expect('', '{0}|{1}'.format(AristaEOSDefaultCommandMode.PROMPT, AristaEOSEnableCommandMode.PROMPT),
                                         logger)
        if not re.search(AristaEOSEnableCommandMode.PROMPT, result):
            enable_password = decrypt_password_from_attribute(api=self._api,
                                                              password_attribute_name='Enable Password',
                                                              context=self._context)
            expect_map = {'[Pp]assword': lambda session, logger: session.send_line(enable_password, logger)}
            session.hardware_expect('enable', AristaEOSEnableCommandMode.PROMPT, action_map=expect_map, logger=logger)
            result = session.hardware_expect('', '{0}|{1}'.format(AristaEOSDefaultCommandMode.PROMPT, AristaEOSEnableCommandMode.PROMPT),
                                             logger)
            if not re.search(AristaEOSEnableCommandMode.PROMPT, result):
                raise Exception('enter_enable_mode', 'Enable password is incorrect')
