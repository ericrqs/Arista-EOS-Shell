from cloudshell.networking.arista.eos.arista_eos_cli_handler import AristaEOSCliHandler
from cloudshell.networking.devices.runners.state_runner import StateRunner


class AristaEOSStateRunner(StateRunner):
    def __init__(self, cli, logger, api, context):
        """

        :param cli:
        :param logger:
        :param api:
        :param context:
        """

        super(AristaEOSStateRunner, self).__init__(logger, api, context)
        self._cli_handler = AristaEOSCliHandler(cli, context, logger, api)
