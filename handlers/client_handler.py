class ClientHandler:
    def handle_command(self, command):
        # Split the command and arguments
        parts = command.split()
        command_name = parts[0]
        command_args = parts[1:]

        if command_name == "authenticate":
            username = command_args[0]
            password = command_args[1]
            return {"command": "authenticate", "data": {"username": username, "password": password}}
        elif command_name == "add_menu":
            menu_id = int(command_args[0])
            meal_name = command_args[1]
            item_ids = list(map(int, command_args[2:]))
            return {"command": "add_menu", "data": {"menu_id": menu_id, "meal_name": meal_name, "item_ids": item_ids}}
        elif command_name == "update_menu":
            menu_id = int(command_args[0])
            meal_name = command_args[1]
            item_ids = list(map(int, command_args[2:]))
            return {"command": "update_menu", "data": {"menu_id": menu_id, "meal_name": meal_name, "item_ids": item_ids}}
        elif command_name == "delete_menu":
            menu_id = int(command_args[0])
            return {"command": "delete_menu", "data": {"menu_id": menu_id}}
        else:
            return {"command": "unknown", "data": {}}
