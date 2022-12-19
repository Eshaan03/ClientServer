import socket

if __name__ == "__main__":

    ip = socket.gethostbyname(socket.gethostname())
    print(ip)
    port = 9988
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))

    string = input("Enter the string: ")
    client.send(bytes(string, "utf-8"))
    buffer = client.recv(1024)
    buffer = buffer.decode("utf-8")
    print(f"Server: {buffer}")
