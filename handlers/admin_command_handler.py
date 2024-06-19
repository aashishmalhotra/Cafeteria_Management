class AdminCommandHandler:
    def __init__(self, menu_database):
        self.commands = ['add_menu', 'update_menu', 'delete_menu']
        self.menu_database = menu_database

    def process_command(self, command, data):
        if command == 'add_menu':
            return self.add_menu(data)
        elif command == 'update_menu':
            return self.update_menu(data)
        elif command == 'delete_menu':
            return self.delete_menu(data)
        else:
            return {'status': 'error', 'message': 'Unknown admin command'}

    def add_menu(self, data):
        try:
            self.menu_database.add_menu(data['menu_id'], data['meal_name'], data['item_ids'])
            return {'status': 'success', 'message': 'Menu added'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

    def update_menu(self, data):
        try:
            self.menu_database.update_menu(data['menu_id'], data['meal_name'], data['item_ids'])
            return {'status': 'success', 'message': 'Menu updated'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

    def delete_menu(self, data):
        try:
            self.menu_database.delete_menu(data['menu_id'])
            return {'status': 'success', 'message': 'Menu deleted'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
