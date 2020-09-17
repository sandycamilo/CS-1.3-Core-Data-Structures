
class Cat:
    def __init__(self, cat_age , cat_says, is_sleeping):
        self.age = cat_age
        self.says = cat_says
        self.is_sleeping = is_sleeping
        self.is_fluffy = True


    def eat(self, food):
        return "I am eating: " + food 

    def is_fluffy_method(self):
        print(self.is_fluffy)
    

#instantiates an object 
#creates a Cat object in memory 
my_cat = Cat(6, "Meow", True)
other_cat = Cat(10, "Meow", True)

print(my_cat.eat("tuna"))


#composition, class that is composed of other classes 

class CatHouse:
    def __init__(self, cats_list):
        self.cats_list = cats_list

    cats = [Cat(5, "Meow", True),Cat(15, "Meep", True),Cat(45, "Pow", True), ]

    kitty_house = CatHouse(cats)
    print(CatHouse.cats_list)