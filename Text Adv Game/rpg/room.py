class Room():
    
    def __init__(self,room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None 

    def set_description (self, room_description):
        self.description = room_description

    def get_description (self):
        return self.description

    def set_name (self, room_name):
        self.name = room_name

    def get_name (self):
        return self.name

    def set_character (self, character):
        self.character = character

    def get_character (self):
        return self.character

    def describe (self):
        print (self.description)

    def set_item (self, item, visible):
        """Adds item to room"""
        self.item = item
        item.visible = visible

    def unset_item(self):
        """Removes item from room"""
        self.item = None

    def get_item (self):
        return self.item

    def link_room(self, room_to_link, direction):
        """Adds directions to room library"""
        self.linked_rooms[direction] = room_to_link
       
    def get_details(self):
        """Prints description of room plus occupants and items"""
        print ("This is the " + self.get_name() + " which is " + self.get_description())
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print( "The " + room.get_name() + " is " + direction)

        occupant = self.get_character()
        if occupant is not None:
            print ("There is " + occupant.describe() + " in the room")

        item_in_room = self.get_item()
        if item_in_room is not None and item_in_room.visible:           #visible attribute not used
            print ("You see " + item_in_room.get_description() + " in the room")
            
    def move(self, direction):
        """Returns new room (if possible0 or string to say you can't go that way"""
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self


