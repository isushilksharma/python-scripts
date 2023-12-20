#Python script to check if a given port is open on a remote server

import socket

def is_port_open(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

# Example usage:
host = "example.com"
port = 80
if is_port_open(host, port):
    print(f"Port {port} is open on {host}")
else:
    print(f"Port {port} is closed on {host}")
