from ipaddress import IPv4Interface


def generate_subnet_and_hosts(ip, main_pref, user_pref):
    pref_dif = user_pref - main_pref
    user_supernet = ip.network.supernet(prefixlen_diff=pref_dif)
    possible_subnets = list(user_supernet.subnets(new_prefix=user_pref))

    with open(f'./results/possible_networks.txt', 'w') as file_text:
        for subnet in possible_subnets:
            host_range = []
            for host in subnet.hosts():
                host_range.append(host)

            result = f'Network IP: {subnet.network_address}' \
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
        generate_subnet_and_hosts(ip, 8, user_pref)
    elif 17 <= user_pref <= 23:
        # when supernet prefix is 16
        generate_subnet_and_hosts(ip, 16, user_pref)
    elif 25 <= user_pref <= 31:
        # when supernet prefix is 24
        generate_subnet_and_hosts(ip, 24, user_pref)
