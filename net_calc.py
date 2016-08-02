import ipaddress


def get_network(addr):
    network = ipaddress.IPv4Interface(addr)
    return network.network


def get_hosts(network):
    return list(network.hosts())


def nflbx(addr):
    try:
        Network = get_network(addr)
        First = next(Network.hosts())
        Broadcast = Network.broadcast_address
        Last = Network.broadcast_address - 1
        neXt = Broadcast + 1
        hosts = Network.num_addresses
        return Network, First, Last, Broadcast, neXt, hosts
    except:
        return 0