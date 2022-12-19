import socket

if __name__ == "__main__":

    ip = socket.gethostname()
    port = 9988
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)
    while True:
        client, address = server.accept()
        print(f"Connection Established - {address[0]}: {address[1]}")

        string = client.recv(1024)
        string = string.decode("utf-8")
        string = string.upper()
        if string == "PING":
            string = "PONG"
            client.send(bytes(string, "utf-8"))
