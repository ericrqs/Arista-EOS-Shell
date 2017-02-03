from cloudshell.networking.arista.eos.arista_eos_cli_handler import AristaEOSCliHandler
from cloudshell.networking.arista.eos.flow.arista_eos_load_firmware_flow import AristaEOSLoadFirmwareFlow

from cloudshell.api.cloudshell_api import CloudShellAPISession
from cloudshell.cli.cli import CLI
from cloudshell.core.logger import qs_logger
from cloudshell.networking.devices.runners.firmware_runner import FirmwareRunner
from cloudshell.shell.core.context import ResourceCommandContext


class AristaEOSFirmwareRunner(FirmwareRunner):
    RELOAD_TIMEOUT = 500

    def __init__(self, cli, logger, api, context):
        """Handle firmware upgrade process

        :param CLI cli: Cli object
        :param qs_logger logger: logger
        :param CloudShellAPISession api: cloudshell api object
        :param ResourceCommandContext context: command context
        """

        super(AristaEOSFirmwareRunner, self).__init__(logger)
        self._cli_handler =  AristaEOSCliHandler(cli, context, logger, api)
        self._load_firmware_flow = AristaEOSLoadFirmwareFlow(self._cli_handler, self._logger)
