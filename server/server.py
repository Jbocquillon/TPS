import socket
import threading
import os

server_host = os.getenv('SERVER_HOST')
server_port = int(os.getenv('SERVER_PORT'))

def handle_client(client_conn, addr):
    while True:
        data = client_conn.recv(1024)
        if not data:
            print(f"Client {addr} disconnected.")
            break

        message = data.decode('utf-8')
        if message=='crash':
            print("Crashing server...")
            client_conn.close()
            server.close()
            break
        print(f"Received data from client {addr}: {message}")

        # Echo back to the client
        client_conn.sendall("Message received by server".encode('utf-8'))

    client_conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_host, server_port))
server.listen(5)

print(f"Server is listening on {server_host}:{server_port}")

while True:
    client_conn, addr = server.accept()
    print(f"Connected to client: {addr}")

    client_thread = threading.Thread(target=handle_client, args=(client_conn, addr))
    client_thread.start()


