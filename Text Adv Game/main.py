import rpg

#-------------------------------------------------------------
#set up rooms

kitchen = rpg.Room ("Kitchen")
kitchen.set_description("a dank and dirty room buzzing with flies.")

dining_hall = rpg.Room ("Dining Hall")
dining_hall.set_description("a bare, scruffy room with sparse furniture.")

ballroom = rpg.Room ("Ballroom")
ballroom.set_description ("a large, well-lit room.")

porch = rpg.Room("Porch")
porch.set_description("a small, dank room with a locked door to the garden")

conservatory = rpg.Room("Conservatory")
conservatory.set_description("a light, airy room overlooking the garden")

kitchen.link_room(dining_hall, "south")
kitchen.link_room(porch, "east")
ballroom.link_room(dining_hall, "east")
ballroom.link_room(conservatory, "south")
dining_hall.link_room(ballroom, "west")
dining_hall.link_room(kitchen, "north")
porch.link_room(kitchen, "west")
conservatory.link_room(ballroom, "north")

#-------------------------------------------------------------
#set up characters

eric_the_zombie = rpg.Enemy("Eric the Zombie", "a bloodstained, ragged youth with a far off expression")
eric_the_zombie.set_conversation("growl.... growl...")
eric_the_zombie.set_weakness("stick")

elding = rpg.Character("Elding", "a friendly elf")
elding.set_conversation("hi, pleased to meet you. Can I help?")

sue = rpg.Character("Sue", "a smiling woman with a colourful jacket")
sue.set_conversation("I'm very happy to see you here")

bugblatter = rpg.Enemy("the Bugblatter Beast of Trall", "the fiercest monster you have ever seen")
bugblatter.set_conversation("I can't see you because you have a towel covering your eyes")
bugblatter.set_weakness("sword")

tinkerbell = rpg.Fairy("Tinkerbell", "a twinkling light floating in the corner", "a glowing fairy figure")
tinkerbell.set_conversation("if you find the bell and ring it I can appear")

#-------------------------------------------------------------
#set up items

sword = rpg.Item("sword", "a sharp, long, shiny metal object", "use")
stick = rpg.Item("stick", "a long, stout stick", "beat")
bell = rpg.Item("bell", "a small brass bell", "ring")
panda = rpg.Item("panda", "a large stuffed panda", "carry")


#-------------------------------------------------------------
#set initial parameters

dining_hall.set_character(eric_the_zombie)
conservatory.set_character(elding)
porch.set_character(sue)
ballroom.set_character(bugblatter)
kitchen.set_character(tinkerbell)

kitchen.set_item(sword, True)
dining_hall.set_item(bell, True)
ballroom.set_item(stick, True)
porch.set_item(panda, True)

current_room = kitchen

#-------------------------------------------------------------
#define variables

directions = ["north","south", "east", "west"]
has_changed = True
you_are_alive = True
item_list = []      #list of items in bag
max_items_in_bag = 2
old_room = None
what = False

#-------------------------------------------------------------
#define functions

def make_item_string_list (item_list):          #update item_string_list in Character class
    rpg.Character.item_string_list = []         #I wanted to keep a list of Item objects to enable user drop them etc - (not implemented)
    for item in item_list:
        rpg.Character.item_string_list.append(item.get_name())

#-------------------------------------------------------------
#main loop
print("---------------------------------------------------------------------")
print("\nHINT\nThe following words are recognised: north, east, south, west,\ntalk, poke, fight, take 'object', ring bell,\nnames of objects (to fight with)")
print("---------------------------------------------------------------------")   

while you_are_alive:
    
    if has_changed:                             #only update room description if something has changed   
        print("\n")         
        current_room.get_details()      
    has_changed = False                         #reset has_changed

    if what:                                    #if does not recognise the previous input
        command = input(">? ")                  
    else:
        command = input("> ")
    what = False
    
    occupant = current_room.get_character()     #set variables to use below
    item = current_room.get_item()
    if item is not None:
        item_name = item.get_name()
    
    if command in directions:                       #move room if possible
        old_room = current_room
        current_room = current_room.move(command)
        if old_room is not current_room:            #only update room description if changed rooms
            has_changed = True

    elif command == "talk":
        if occupant is not None:
            occupant.talk()
            
    elif command == "fight":
        if occupant is not None:        
            if not occupant.fight():                #you died!
                you_are_alive = False

    elif command == "poke":
        if occupant is not None:
            if not occupant.poke():                 #you died!
                print("I warned you.")
                you_are_alive = False

    elif command == "take " + item_name:
        if item is not None:
            if len(item_list) < max_items_in_bag:
                current_room.unset_item()
                item_list.append(item)
                make_item_string_list(item_list)         #update item_string_list in Character class for use in fight
                print("You have taken the " + item.get_name())
                has_changed = True
            else:
                print("Sorry you already have " + str(len(item_list)) + " items in your bag")

    # a specific instance to avoid lots of coding!!
    elif command == "ring bell":
        if isinstance(occupant, Fairy):
            if Character.item_string_list.count("bell"):        #you have a bell
                tinkerbell.make_visible()
                tinkerbell.set_conversation("Nice to meet you in person")
                has_changed = True

    else:
        what = True
        
print("-----------------------------------------------------")
print("END OF GANE.... TRY AGAIN")
print("-----------------------------------------------------")


                       






