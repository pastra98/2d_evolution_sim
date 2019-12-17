import random

class Parent:
    def __init__(self, g_type):

    def my_method(self):
        self.data += str(random.randint(0, 10))

    def update_friend(arg):




class Child(Parent):
    def change_data(self):
        self.data += random.choice(["b", "c", "d"])


class Friend:
    def __init__(self):
        self.info = [1]

    def extend_info(self, arg):
        self.info.append(arg)
        return self.info

dad = Parent()
kid = Child()

for x in range(10):
    print("Parent data: {}".format(dad.data))
    print("Kid data: {}".format(kid.data))
    print("now changing again \n")
    kid.my_method()

