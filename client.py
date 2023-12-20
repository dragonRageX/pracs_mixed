import socket

def mpm():
    host = "localhost"
    port = 6000
    s = socket.socket()
    s.connect((host, port))
    while True:
        x = input("Enter new message: ")
        y = x.encode("ascii")
        s.send(y)
        data = s.recv(1024)
        d = data.decode("ascii")
        print(f"Server: {data}")

mpm()