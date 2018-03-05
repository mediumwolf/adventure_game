class Character():

    #define class variable to store item_list from main.py
    item_string_list = []

    #class variable
    enemies_killed = 0
    enemy_string = " enemy"     #to swap between 'enemy' and 'enemies' in print statement

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.alive = True
        self.poked = False
        self.item = None

    def describe(self):
        """Returns a description of this character when alive and when dead"""
        if self.alive:
            return self.description
        else:
            return self.description + " who is now lying dead on the floor"

    def set_conversation(self, conversation):
        """Set conversation"""
        self.conversation = conversation

    def talk(self):
        """Returns conversation string dependant on whether they are alive or dead"""
        if self.alive:
            if self.conversation is not None:
                print("[" + self.name + " says]: " + self.conversation)
            else:
                print(self.name + " doesn't want to talk to you")
        else:
            print("The dead don't talk")

    def fight(self):
        """Returns a string if character is 'poked' """
        print(self.name + " doesn't want to fight with you")
        return True

    def get_is_alive(self):
        """Returns self.alive as True or False"""
        return self.alive

    def poke(self):
        """Returns a string if character is 'poked' """
        if self.alive:
            if not self.poked:
                print("Please don't do that")
                self.poked = True
            else:
                print("I REALLY don't want you to do that again!")
            return True   
    

class Enemy(Character):

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, weakness):
        self.weakness = weakness

    def get_weakness(self):
        return self.weakness
        
    #overides method above
    def fight(self):
        """Asks what you want to fight with and prints outcome of fight"""
        if self.alive:
            fight_with = input("What do you want to fight with? >")
            if fight_with in Character.item_string_list:
                if fight_with == self.weakness:
                    print ("You beat " + self.name + " to pulp with your " + fight_with)
                    Character.enemies_killed += 1
                    if Character.enemies_killed > 1:
                        Character.enemy_string = " enemies"
                    print("\nYou have now killed " + str(Character.enemies_killed) + Character.enemy_string)
                    
                    self.alive = False
                    return True
                else:
                    print ("Ooops, your " + fight_with + " was not enough to beat " + self.name + ". You are dead.")
                    return False
            else:
                print("You don't have a " + fight_with + " to fight " + self.name + " with")
                return True
        else:
            print("Why fight the dead?")
            return True

    #overides method above
    def poke(self):
        """Returns a string if Enemy is 'poked' """
        if self.alive:
            if not self.poked:
                print("grwwyrhtuitz!!!!!!")
                print ("I wouldn't do that again!")
                self.poked = True
                return True
            else:
                print("Sorry, you poked " + self.name + " too often and you are dead")
                return False        
        else:
            return True
        

class Fairy(Character):
    
    def __init__(self, char_name, char_description, char_description_visible):
        super().__init__(char_name, char_description)
        self.description_visible = char_description_visible
        self.visible = False

    #overides method above
    def fight(self):
        """Returns string if you fight with Fairy"""
        print(self.name + " ignores you")
        return True

    #overides method above
    def poke(self):
        """Returns a string if Fairy is 'poked' """
        if self.visible:
            print("oooh, I like that")
        return True

    #new method for Fairy
        """Sets new description and visible attribute for Fairy"""
    def make_visible(self):
        self.description = self.description_visible
        self.visible = True

    
    
    
    
