import socket
import threading
import json
from handlers.admin_command_handler import AdminCommandHandler
# from handlers.chef_command_handler import ChefCommandHandler
from databases.menu_database import MenuDatabase

class Server:
    def __init__(self, host='127.0.0.1', port=9997):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server listening on {self.host}:{self.port}")

        self.menu_database = MenuDatabase()
        self.admin_handler = AdminCommandHandler(self.menu_database)
        # self.chef_handler = ChefCommandHandler()

        self.users = {
            'admin1': ('password1', 'admin'),
            'chef1': ('password2', 'chef'),
            'employee1': ('password3', 'employee')
        }

    def handle_client(self, client_socket):
        try:
            self.authenticate_user(client_socket)
            while True:
                message = client_socket.recv(1024).decode()
                if not message:
                    break
                data = json.loads(message)
                command = data['command']
                response = self.route_command(command, data['data'])
                client_socket.sendall(json.dumps(response).encode())
        except Exception as e:
            print(f"Error: {e}")
        finally:
            client_socket.close()

    def authenticate_user(self, client_socket):
        authenticated = False
        while not authenticated:
            client_socket.sendall("Enter username: ".encode())
            username = client_socket.recv(1024).decode().strip()
            client_socket.sendall("Enter password: ".encode())
            password = client_socket.recv(1024).decode().strip()

            if username in self.users:
                stored_password, role = self.users[username]
                if password == stored_password:
                    client_socket.sendall("Authenticated".encode())
                    authenticated = True
                    return role  # Return the role if authentication is successful

            client_socket.sendall("Authentication failed. Please try again.".encode())
        client_socket.close()
        return None  # Return None if authentication fails

    def route_command(self, command, data):
        if command in self.admin_handler.commands:
            return self.admin_handler.process_command(command, data)
        else:
            return {'status': 'error', 'message': 'Unknown command'}

    def run(self):
        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Accepted connection from {addr}")
            client_handler_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_handler_thread.start()

if __name__ == '__main__':
    server = Server()
    server.run()
