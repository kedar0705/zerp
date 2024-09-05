# class and objects
class Test:
    x = 5

    def __init__(self):
        pass

    def func1(self, a, b):
        return a+b+self.x

    def func2(self):
        return "This is func2"

obj = Test()
print(obj.x)
print(obj.func1(2,5))
print(obj.func2())

class Test1:
    def __init__(self, a: str, b: int):
        self.a = a
        self.b = b

    def func1(self):
        return self.a, self.b


obj1 = Test1('kedar', 3)
print(obj1.func1())
x, y = obj1.func1()
print(x)
print(y)

