from Chef import Chef

class ChineseChef(Chef): #A new class called ChineseChef, inheriting Chef's attributes

    def make_fried_rice(self): #Chinese chef can also make fried rice
        print("The chef makes fried rice")

    def make_special_dish(self): #Chinese Chef's special dish orange chicken.
        print("The chef makes orange chicken") #We can change it from inheritence by overriding the code

