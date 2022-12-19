import socket

if __name__ == "__main__":

    ip = socket.gethostname()
    port = 9988
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))

    buffer = server.recv(1024)
    buffer = buffer.decode("utf-8")
    print(f"The length of the string accepted via server is: {len(buffer)}")
