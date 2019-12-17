def my_func(a):
    for x in a:
        if x > 3:
            return None

    return "Woohoo"


class MyClass:
    def __init__(self, var):
        self.var = var


b = my_func([0,1,2,3,4])
classy = MyClass(b)

print(id(b), id(classy.var))
