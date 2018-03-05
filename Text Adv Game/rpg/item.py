class Item():
    
    def __init__ (self, item_name, description, action):
        self.name = item_name
        self.description = description
        self.visible = True
        self.action = action

    def set_name(self, item_name):
        self.name = item_name

    def get_name (self):
        return self.name

    def set_description (self, description):
        self.description = description

    def get_description (self):
        return self.description



    
