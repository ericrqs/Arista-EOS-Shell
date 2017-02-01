from cloudshell.networking.arista.eos.arista_eos_cli_handler import AristaEOSCliHandler
from cloudshell.networking.arista.eos.autoload.arista_eos_autoload import AristaEOSAutoload

from cloudshell.networking.cisco.flow.cisco_autoload_flow import CiscoAutoloadFlow
from cloudshell.networking.devices.runners.autoload_runner import AutoloadRunner


class AristaEOSAutoloadRunner(AutoloadRunner):
    def __init__(self, cli, logger, api, context, supported_os):
        super(AristaEOSAutoloadRunner, self).__init__(cli, logger, context, supported_os)
        self._cli_handler = AristaEOSCliHandler(cli, context, logger, api)
        self._logger = logger
        self._autoload_flow = CiscoAutoloadFlow(cli_handler=self._cli_handler,
                                                autoload_class=AristaEOSAutoload,
                                                logger=logger,
                                                resource_name=self._resource_name)
