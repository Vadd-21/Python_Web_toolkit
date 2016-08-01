import socket
import threading


class Worker(threading.Thread):
    """
    worker holds the basic information for the threaded worker to do its job
    """
    def __init__(self, target, func):
        super().__init__()
        self.target = target
        self.func = func
        self.ports = []
        self.ret = []

    def run(self):
        """
        calls out to the threads starting function, this enters
        the provided function
        """
        for port in self.ports:
            self.ret.append(self.func(self.target, port))
        # allows pointer pointer manipulation


def conn_scan(tgt_host, tgt_port):
    """
    conn_scan(str, int)
    conn scan attempts to connect to the target host on the target port
    and returns a tuple of port number and open or closed
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(.02)
        sock.connect((tgt_host, tgt_port))
        sock.close()
        return (tgt_port, "open")
    except:
        return (tgt_port, "closed")


def scanner(tgt_host, start, end):
    """
    scan(str, int, int)
    scan takes a string of an ip address, a starting port as an int
    and an ending port as an int, it creates 10 threads, it divides the ports
    amoung the threads and then attempts a full connect scan of the ports
    """
    workers = []
    ret = []
    t_count = 10
    for i in range(t_count):
        workers.append(Worker(tgt_host, conn_scan))

    for i in range(start, end+1):
        workers[i % t_count].ports.append(i)

    for worker in workers:
        worker.start()

    for worker in workers:
        worker.join()
        ret += worker.ret

    ret = sorted(ret, key=lambda tup: tup[0])  # sorts by port
    return ret
