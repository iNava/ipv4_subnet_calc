from ipaddress import IPv4Interface



def generate_subnet_1to7pref_and_hosts(ip_address, pref_len):
    supernt = ip_address.network.supernet(prefixlen_diff=pref_len)
    possible_subnets = list(supernt.subnets(pref_len))

    with open('./results/possible_networks.txt', 'w') as file_text:  # save result into 'possible_networks.txt' file
        # Save string into the first line of the txt file
        file_text.write(f'\nAll {len(possible_subnets)} of the possible /{pref_len} Networks:\n' )

        for subnet in possible_subnets:  # Possible Networks in the supernet
            network_address = subnet.network_address
            broadcast_address = subnet.broadcast_address

            result = f'\nNetwork IP: {network_address}' \
                     f'\nUsable Host IP Range: {network_address + 1} - {broadcast_address - 1}' \
                     f'\nNetwork Broadcast IP: {broadcast_address}' \
                     f'\n--------------------------------------------------\n'

            file_text.write(result)


def generate_subnet_and_hosts(ip_address, pref_len, main_pref, condition):
    pref_dif = pref_len - main_pref  # difference between user provided netmask and supernet netmask length
    user_supernet = ip_address.network.supernet(prefixlen_diff=pref_dif)
    possible_subnets = list(user_supernet.subnets(new_prefix=pref_len))  # generates list of the possible networks

    with open('./results/possible_networks.txt', 'w') as file_text:  # save result into 'possible_networks.txt' file
        ip_in_list = str(ip_address).split('.')
        # Save main network part into 'network'
        if condition == 1:
            network = f'{ip_in_list[0]}.*.*.*'
        elif condition == 2:
            network = f'{ip_in_list[0]}.{ip_in_list[1]}.*.*'
        elif condition == 3:
            network = f'{ip_in_list[0]}.{ip_in_list[1]}.{ip_in_list[2]}.*'
        # Save string into the first line of the txt file
        file_text.write(f'\nAll {len(possible_subnets)} of the possible /{pref_len} Networks for {network}:\n' )

        for subnet in possible_subnets:  # Possible Networks in the supernet
            network_address = subnet.network_address
            broadcast_address = subnet.broadcast_address

            result = f'\nNetwork IP: {network_address}' \
                     f'\nUsable Host IP Range: {network_address + 1} - {broadcast_address - 1}' \
                     f'\nNetwork Broadcast IP: {broadcast_address}' \
                     f'\n--------------------------------------------------\n'

            file_text.write(result)


def calc_possible_subnets(ip_address, subnet):
    ip = IPv4Interface(ip_address + subnet)
    pref_len = int(subnet[1:])

    if 1 <= pref_len < 8:  # when supernet prefix is 1 - 7
        generate_subnet_1to7pref_and_hosts(ip, pref_len)
    elif 9 <= pref_len <= 15: # when supernet prefix is 8
        generate_subnet_and_hosts(ip, pref_len, 8, 1)
    elif pref_len == 8 or  pref_len == 16 or pref_len == 24 or pref_len == 32:  # pass calculations, not required
        pass
    elif 17 <= pref_len <= 23:  # when supernet prefix is 16
        generate_subnet_and_hosts(ip, pref_len, 16, 2)
    elif 25 <= pref_len <= 31:  # when supernet prefix is 24
        generate_subnet_and_hosts(ip, pref_len, 24, 3)


calc_possible_subnets('121.254.42.4', '/30')