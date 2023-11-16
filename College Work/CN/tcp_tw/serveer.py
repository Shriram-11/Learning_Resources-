import socket


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server is listening on port 12345...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        data = client_socket.recv(1024)
        print(f"Received data: {data.decode()}")
        client_socket.sendall(b"Hello, Client")
        client_socket.close()


if __name__ == "__main__":
    start_server()
