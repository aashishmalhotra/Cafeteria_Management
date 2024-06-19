class MenuDatabase:
    def __init__(self):
        self.menus = {}

    def add_menu(self, menu_id, meal_name, item_ids):
        if menu_id in self.menus:
            raise ValueError("Menu ID already exists")
        self.menus[menu_id] = {'meal_name': meal_name, 'item_ids': item_ids}

    def update_menu(self, menu_id, meal_name, item_ids):
        if menu_id not in self.menus:
            raise ValueError("Menu ID does not exist")
        self.menus[menu_id] = {'meal_name': meal_name, 'item_ids': item_ids}

    def delete_menu(self, menu_id):
        if menu_id not in self.menus:
            raise ValueError("Menu ID does not exist")
        del self.menus[menu_id]

    def get_menus(self):
        return self.menus
