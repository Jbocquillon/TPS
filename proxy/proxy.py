import socket
import threading
import os

proxy_host = os.getenv('PROXY_HOST')
proxy_port = int(os.getenv('PROXY_PORT'))
server_host = os.getenv('SERVER_HOST')
server_port = int(os.getenv('SERVER_PORT'))


def handle_client(client_conn):
    while True:
        data = client_conn.recv(1024)
        if not data:
            break

        print(f"Received data from client: {data.decode('utf-8')}")

        server_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_conn.connect((server_host, server_port))

        server_conn.sendall(data)
        server_response = server_conn.recv(1024)
        print(f"Received data from server: {server_response.decode('utf-8')}")

        client_conn.sendall(server_response)
        server_conn.close()

    client_conn.close()

proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxy.bind((proxy_host, proxy_port))
proxy.listen(5)

print(f"Proxy is listening on {proxy_host}:{proxy_port}")

while True:
    client_conn, client_addr = proxy.accept()
    print(f"Connected to client: {client_addr}")

    client_thread = threading.Thread(target=handle_client, args=(client_conn,))
    client_thread.start()


