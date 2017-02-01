from cloudshell.networking.arista.eos.arista_eos_cli_handler import AristaEOSCliHandler
from cloudshell.networking.devices.runners.run_command_runner import RunCommandRunner


class AristaEOSRunCommandRunner(RunCommandRunner):
    def __init__(self, cli, context, logger, api):
        """Create CiscoRunCommandOperations

        :param context: command context
        :param api: cloudshell api object
        :param cli: CLI object
        :param logger: QsLogger object
        :return:
        """

        super(AristaEOSRunCommandRunner, self).__init__(logger)
        self._cli_handler = AristaEOSCliHandler(cli, context, logger, api)
