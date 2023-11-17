import socket
import os

proxy_host = os.getenv('PROXY_HOST')
proxy_port = int(os.getenv('PROXY_PORT'))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((proxy_host, proxy_port))

print("Connected to Proxy. Type 'exit' to disconnect.")

while True:
    message = input("Enter a message: ")

    client.sendall(message.encode('utf-8'))

    if message.lower() == 'exit':
        print("Disconnecting from Proxy...")
        break

    response = client.recv(1024)
    print(f"Received response from proxy: {response.decode('utf-8')}")

client.close()


