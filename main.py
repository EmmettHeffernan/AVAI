from mpi4py import MPI
import socket
import os

def get_meta_info():
    info = {
        "hostname": socket.gethostname(),
        "ip_address": socket.gethostbyname(socket.gethostname()),
        "os": os.uname().sysname,
        "release": os.uname().release,
        "version": os.uname().version,
        "machine": os.uname().machine,
        "cores": os.cpu_count()
    }
    return info

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    meta_info = get_meta_info()
    all_meta_info = comm.gather(meta_info, root=0)

    if rank == 0:
        print(f"Running on {size} nodes")
        for i, info in enumerate(all_meta_info):
            print(f"Node {i}:")
            for key, value in info.items():
                print(f"  {key}: {value}")

if __name__ == "__main__":
    main()
