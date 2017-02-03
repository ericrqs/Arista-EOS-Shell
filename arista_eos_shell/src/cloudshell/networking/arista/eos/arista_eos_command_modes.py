
from cloudshell.cli.command_mode import CommandMode


class AristaEOSDefaultCommandMode(CommandMode):
    PROMPT = r'>\s*$|#\s*$'
    ENTER_COMMAND = ''
    EXIT_COMMAND = ''

    def __init__(self, context):
        """
        Initialize Default command mode, only for cases when session started not in enable mode

        :param context:
        """
        self._context = context
        CommandMode.__init__(self, AristaEOSDefaultCommandMode.PROMPT, AristaEOSDefaultCommandMode.ENTER_COMMAND,
                             AristaEOSDefaultCommandMode.EXIT_COMMAND)


class AristaEOSEnableCommandMode(CommandMode):
    # PROMPT = r'(?:(?!\)).)#\s*$'
    PROMPT = r'#\s*$'
    ENTER_COMMAND = 'enable'
    EXIT_COMMAND = ''

    def __init__(self, context):
        """
        Initialize Enable command mode - default command mode for Cisco Shells

        :param context:
        """
        self._context = context

        CommandMode.__init__(self, AristaEOSEnableCommandMode.PROMPT, AristaEOSEnableCommandMode.ENTER_COMMAND,
                             AristaEOSEnableCommandMode.EXIT_COMMAND)


class AristaEOSConfigCommandMode(CommandMode):
    PROMPT = r'\(config.*\)#\s*$'
    ENTER_COMMAND = 'configure terminal'
    EXIT_COMMAND = 'exit'

    def __init__(self, context):
        """
        Initialize Config command mode

        :param context:
        """
        exit_action_map = {
            self.PROMPT: lambda session, logger: session.send_line('exit', logger)}
        CommandMode.__init__(self, AristaEOSConfigCommandMode.PROMPT,
                             AristaEOSConfigCommandMode.ENTER_COMMAND,
                             AristaEOSConfigCommandMode.EXIT_COMMAND,
                             exit_action_map=exit_action_map)


CommandMode.RELATIONS_DICT = {
    AristaEOSDefaultCommandMode: {
        AristaEOSEnableCommandMode: {
            AristaEOSConfigCommandMode: {}
        }
    }
}