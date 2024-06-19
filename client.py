import socket
import json
from handlers.client_handler import ClientHandler

class Client:
    def __init__(self, host='127.0.0.1', port=9997):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_handler = ClientHandler()

    def connect(self):
        self.sock.connect((self.host, self.port))
        print(f"Connected to server at {self.host}:{self.port}")

    def authenticate_user(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        data = {"command": "authenticate", "data": {"username": username, "password": password}}
        self.sock.sendall(json.dumps(data).encode())
        response = self.sock.recv(1024).decode()
        print(f"Server response: {response}")

    def run(self):
        self.connect()
        self.authenticate_user()
        try:
            while True:
                command = input("Enter command (or 'exit' to quit): ")
                if command == "exit":
                    break
                data = self.client_handler.handle_command(command)
                self.sock.sendall(json.dumps(data).encode())
                response = self.sock.recv(1024).decode()
                print(f"Server response: {response}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.sock.close()

if __name__ == '__main__':
    client = Client()
    client.run()
