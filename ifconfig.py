#!/usr/bin/env python3

import socket
import psutil

af_map = {
    socket.AF_INET: 'IPv4',
    socket.AF_INET6: 'IPv6',
    psutil.AF_LINK: 'MAC',
}


class InterfaceData(object):
    """
    The my_interfaces dict should look something like this:
     {
        'en0': {
            'IPv4': ('1.2.3.4', '255.255.255.0'),
            'IPv6': ('fe80::c5e:182f:ea94:c9c0%en0', 'ffff:ffff:ffff:ffff::'),
            'MAC': ('aa:bb:cc:dd:ee:ff', None)
        },
     }
    """
    def __init__(self):
        self.my_interfaces = {}

    def get_interfaces(self):
        """
        get_interfaces uses the psutil library to get all interfaces
        It then stores the interface name, tyhe address type, the address,
        netmask and mac address as applicable
        """
        # Define a dictionary to store interface data
        my_interfaces = {}

        for interface, addrs in psutil.net_if_addrs().items():
            self.my_interfaces[interface] = {}

            # We can have multiple address types for each interface
            for addr in addrs:
                self.my_interfaces[interface][af_map.get(addr.family, addr.family)] = \
                    (addr.address, addr.netmask)

        return self.my_interfaces

    def print_interfaces(self):
        """
        print_interfaces prints out the information retrieved from
        get_interfaces Should output in the form of:
        <Name 1>: <IPv4 or IPv6 address> <IPv4 subnet> <MAC address>
        """
        # from pprint import pprint
        # pprint(self.my_interfaces)
        ipv4 = af_map[socket.AF_INET]
        ipv6 = af_map[socket.AF_INET6]
        mac = af_map[psutil.AF_LINK]
        for iface in sorted(self.my_interfaces):
            output_prefix = f'{iface}:'
            output_data = []

            interface = self.my_interfaces[iface]

            if ipv4 in self.my_interfaces[iface]:
                output_data.append(f'{ipv4}: {interface[ipv4][0]}/{interface[ipv4][1]}')
            if ipv6 in self.my_interfaces[iface]:
                output_data.append(f'{ipv6}: {interface[ipv6][0]}/{interface[ipv6][1]}')
            if mac in self.my_interfaces[iface]:
                output_data.append(f'{mac}: {interface[mac][0]}')

            print(output_prefix, ', '.join(output_data))


if __name__ == '__main__':
    ifconfig = InterfaceData()
    ifconfig.get_interfaces()
    ifconfig.print_interfaces()
