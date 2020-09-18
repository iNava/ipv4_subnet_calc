import json
import sys

from ipaddress import IPv4Address, IPv4Interface
from ext_ipv4 import MyIPv4
from data import subnets
from calc_subnets import calc_possible_subnets


class IPv4Calc:

    def __init__(self, ip_address, subnet):
        self.ip_address = ip_address
        self.subnet = subnet
        self.ip_interface = IPv4Interface(self.ip_address + self.subnet)

    # ip_and_subnet_in_binary() - converts doted decimal addresses into binary view
    def ip_and_subnet_in_binary(self):
        ipv4_in_binary = MyIPv4(
            self.ip_address).binary_repr  # "MyIPv4" - is an Extending IPv4Address, returns bytes in binary
        subnet_in_dot_decimal = subnets[self.subnet]  # "subnets" is a dictionary with prefixes and doted decimal values
        subnet_in_binary = MyIPv4(subnet_in_dot_decimal).binary_repr
        return ipv4_in_binary, subnet_in_binary

    # Convert doted decimal addresses into hexadecimal view
    def ip_in_hexd(self):
        ip_in_hexadecimal = MyIPv4(self.ip_address).hexd_repr
        return ip_in_hexadecimal

    #  Returns Network Address, Broadcast Address and Total Number of Hosts
    def net_broad_addr_and_totalhosts(self):
        network_interface = self.ip_interface
        net_address = network_interface.network
        broad_address = net_address.broadcast_address
        total_number_hosts = net_address.num_addresses
        return net_address.network_address, broad_address, total_number_hosts

    # Return a list of usable hosts in a network
    def usable_host_ip_range(self):
        hosts_ip_generator = self.ip_interface.network.hosts()  # .hosts() - Generates Iterator over usable hosts in a network
        usable_hosts = []
        while hosts_ip_generator:
            try:
                usable_hosts.append(next(hosts_ip_generator))
            except StopIteration:
                break
        return usable_hosts

    #  Return wildcard mask
    def wildcard_ip(self):
        wildcard = self.ip_interface
        return wildcard.hostmask

    #  Return IP Class
    def ip_class(self):
        host_ip = IPv4Address(self.ip_address)
        if IPv4Address('0.0.0.0') <= host_ip <= IPv4Address('127.255.255.255'):
            return 'A'
        if IPv4Address('128.0.0.0') <= host_ip <= IPv4Address('191.255.255.255'):
            return 'B'
        if IPv4Address('192.0.0.0') <= host_ip <= IPv4Address('223.255.255.255'):
            return 'C'
        if IPv4Address('224.0.0.0') <= host_ip <= IPv4Address('239.255.255.255'):
            return 'D'
        if IPv4Address('240.0.0.0') <= host_ip <= IPv4Address('255.255.255.255'):
            return 'E'

    #  IP belongs to Public or Private address
    def private_ip(self):
        host_ip = self.ip_interface
        if host_ip.is_private:
            return 'Private'
        else:
            return 'Public'

    # Converts IPv4 into IPv4 Mapped Address and 6to4 Prefix:
    def ipv4_to_ipv6(self):
        ip_in_hex = self.ip_in_hexd()
        ipv4_mapped_address = f':FFFF:{ip_in_hex[:4]}.{ip_in_hex[4:]}'
        ip_6to4_prefix = f'2002:{ip_in_hex[:4]}.{ip_in_hex[4:]}::/48'
        return ipv4_mapped_address, ip_6to4_prefix

    # Generates json file(data.json) with calculated results
    def generate_json(self):
        net_broad_total_hosts = self.net_broad_addr_and_totalhosts()
        host_range = self.usable_host_ip_range()
        ip_mask_binary = self.ip_and_subnet_in_binary()
        hexadecimal_values = self.ip_in_hexd()
        ipv6 = self.ipv4_to_ipv6()
        
        result = {
            'IP Address': self.ip_address,
            'Network Address': f'{net_broad_total_hosts[0]}',
            'Broadcast Address': f'{net_broad_total_hosts[1]}',
            'Total Number of Hosts': net_broad_total_hosts[2],
            'Number of Usable Hosts': net_broad_total_hosts[2] - 2,
            'Usable Host IP Range': f'{host_range[0]} - {host_range[-1]}',
            'Subnet Mask': subnets[self.subnet],
            'Wildcard Mask': f'{self.wildcard_ip()}',
            'Binary Subnet Mask': ip_mask_binary[1],
            'IP Class': self.ip_class(),
            'CIDR Notation': self.subnet,
            'IP Type': self.private_ip(),
            'Short': f'{self.ip_address} {self.subnet}',
            'Binary ID': ip_mask_binary[0].replace('.', ''),
            'Integer ID': int(IPv4Address(self.ip_address)),
            'Hex ID': f'0x{hexadecimal_values.replace(".", "")}',
            'in-addr.arpa': IPv4Address(self.ip_address).reverse_pointer,
            'IPv4 Mapped Address': ipv6[0],
            '6to4 Prefix': ipv6[1],
        }

        with open('./results/data.json', 'w') as f:
            json.dump(result, f, indent=4)

    # Print to STDOUT
    def stdout_result(self):
        self.generate_json()

        with open('./results/data.json', 'r') as jfile:
            data = json.load(jfile)
            for key, value in data.items():
                space_length = (28 - len(key)) * ' '  # counts required space to pretify stdout
                print(key + space_length + str(value))


def main():
    print('\nIPv4 Subnet Calculator')
    user_ip = input('\nPlease input IPv4 network address (e.g. 192.233.164.138):\n')
    user_sn = input('\nPlease input subnet using prefix (e.g. /24):\n')
    print('\n----------------------------------------------------------------')
    result = IPv4Calc(user_ip, user_sn)
    result.stdout_result()

    calc_possible_subnets(user_ip, user_sn)
    with open('./results/possible_networks.txt', 'r') as txtfile:
        for line in txtfile:
            print(line.strip())


if __name__ == '__main__':
    main()
