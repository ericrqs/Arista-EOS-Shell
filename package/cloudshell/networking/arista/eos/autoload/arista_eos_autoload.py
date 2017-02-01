import os

from cloudshell.networking.cisco.autoload.cisco_generic_snmp_autoload import CiscoGenericSNMPAutoload
from cloudshell.networking.cisco.ios.autoload.autoload_structure import GenericPort, GenericPortChannel, \
    CiscoIOSDevice, GenericChassis, GenericModule, GenericPowerPort


class AristaEOSAutoload(CiscoGenericSNMPAutoload):
    def __init__(self, snmp_handler, logger, supported_os, resource_name):
        super(AristaEOSAutoload, self).__init__(snmp_handler, logger, supported_os, resource_name)
        self.port = GenericPort
        self.power_port = GenericPowerPort
        self.port_channel = GenericPortChannel
        self.root_model = CiscoIOSDevice
        self.chassis = GenericChassis
        self.module = GenericModule

    def load_cisco_mib(self):
        super(AristaEOSAutoload, self).load_cisco_mib()
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'mibs'))
        self.snmp.update_mib_sources(path)
        self.snmp.load_mib(['ARISTA-SMI-MIB',
                            # 'ARISTA-ACL-MIB',
                            # 'ARISTA-BGP4V2-MIB',
                            # 'ARISTA-BGP4V2-TC-MIB',
                            # 'ARISTA-BRIDGE-EXT-MIB',
                            # 'ARISTA-CONFIG-COPY-MIB',
                            # 'ARISTA-CONFIG-MAN-MIB',
                            # 'ARISTA-DAEMON-MIB',
                            # 'ARISTA-ENTITY-SENSOR-MIB',
                            # 'ARISTA-IF-MIB',
                            # 'ARISTA-MAU-MIB',
                            # 'ARISTA-PFC-MIB',
                            'ARISTA-PRODUCTS-MIB',
                            # 'ARISTA-QOL-MIB',
                            # 'ARISTA-QUEUE-MIB',
                            # 'ARISTA-REDUNDANCY-MIB',
                            # 'ARISTA-SNMP-TRANSPORTS-MIB',
                            # 'ARISTA-SW-IP-FORWARDING-MIB',
                            # 'ARISTA-TEST-MIB',
                            # 'ARISTA-VRF-MIB',
                            ])
