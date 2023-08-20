
# Usage of kind of methods
#--------------------------------
# Instance Method (access to attributes by objects)
# Class Method (to do something with the class itself)
# Static Method ( to do something doesnt have access to object or class but related to class)

class Toyota:
    Toyota_cars_num=0

    def __init__(self,Name,Color,Model):
        self.name = Name
        self.color = Color
        self.model = Model
        Toyota.Toyota_cars_num += 1

    # Instance Method
    def all_info(self):
        return f"{self.name} {self.color} {self.model}"

    # Class Method
    @classmethod
    def show_cars_number(cls):
        print(f"The number of our Toyota Cars : {cls.Toyota_cars_num} cars")

    # Static Method
    @staticmethod
    def Greating():
        print("\n\n\U0001F973 \U0001F47E Welcome in Our Toyota Cars \U0001F47E \U0001F973\n")

# Greating Instances
Toyota_one = Toyota("Corolla","Black",2015)
Toyota_two = Toyota("Prius","crimson",2018)
Toyota_three = Toyota("Camry","Turquoise",2022)



# Access Static Method
Toyota.Greating()

# Access Instance Method
print(Toyota_one.all_info())
print(Toyota_one.all_info())
print(Toyota_one.all_info())

# Access Class Method
Toyota.show_cars_number()





