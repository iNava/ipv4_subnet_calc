from ipaddress import IPv4Interface


def generate_subnet_and_hosts(ip_address, main_pref, user_pref, pref_len):
    pref_dif = user_pref - main_pref  # difference between user provided netmask and supernet netmask length
    user_supernet = ip_address.network.supernet(prefixlen_diff=pref_dif)
    possible_subnets = list(user_supernet.subnets(new_prefix=user_pref))  # generates list of the possible networks

    with open(f'./results/possible_networks.txt', 'w') as file_text:  # save result into 'possible_networks.txt' file
        ip_in_list = str(ip_address).split('.')
        # Save main network part into 'network'
        if pref_len == 1:
            network = f'{ip_in_list[0]}.*.*.*'
        elif pref_len == 2:
            network = f'{ip_in_list[0]}.{ip_in_list[1]}.*.*'
        elif pref_len == 3:
            network = f'{ip_in_list[0]}.{ip_in_list[1]}.{ip_in_list[2]}.*'
        # Save string into the first line of the txt file
        file_text.write(f'\nAll {len(possible_subnets)} of the possible /{user_pref} Networks for {network}:\n' )

        for subnet in possible_subnets:  # Possible Networks in the supernet
            host_range = []
            for host in subnet.hosts(): # generates hosts on the network according to the netmask
                host_range.append(host)

            result = f'\nNetwork IP: {subnet.network_address}' \
                     f'\nUsable Host IP Range: {host_range[0]} - {host_range[-1]}' \
                     f'\nNetwork Broadcast IP: {subnet.broadcast_address}' \
                     f'\n--------------------------------------------------\n'

            file_text.write(result)


def calc_possible_subnets(ip_address, subnet):
    ip = IPv4Interface(ip_address + subnet)
    user_pref = int(subnet[1:])
    # when supernet prefix is 1 - 10, 16, 24 and 32
    if 1 <= user_pref < 10 or user_pref == 16 or user_pref == 24 or user_pref == 32:
        pass
    elif 10 <= user_pref <= 15:
        # when supernet prefix is 8
        generate_subnet_and_hosts(ip, 8, user_pref, 1)
    elif 17 <= user_pref <= 23:
        # when supernet prefix is 16
        generate_subnet_and_hosts(ip, 16, user_pref, 2)
    elif 25 <= user_pref <= 31:
        # when supernet prefix is 24
        generate_subnet_and_hosts(ip, 24, user_pref, 3)
