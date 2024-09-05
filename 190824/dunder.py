# print(dir(int))
# print(dir(float))
# print(dir(str))

# class String:
#
#     def __init__(self, string):
#         self.string = string
#
#     def __repr__(self):
#         return 'object: {}'.format(self.string)
#
#     def __add__(self, other):
#         return self.string + other


# obj1 = String('Hi')
# # print(obj1 + ' kedar')
# print(obj1)

# class Number:
#     def __init__(self, num):
#         self.num = num
#
#     def __le__(self, other):
#         return self.num <= other.num
#
#     def __eq__(self, other):
#         return self.num == other.num
#
#     def __ne__(self, other):
#         return self.num != other.num
#
#     def __lt__(self, other):
#         return self.num < other.num

# obj_num1 = Number(4)
# print(obj_num1)
# obj_num2 = Number(5)
# print(obj_num1 <= obj_num2)
# print(obj_num1 != obj_num2)
# print(obj_num1 < obj_num2)
# print(obj_num1 <= obj_num2)


# class Test1:
#     def __str__(self):
#         return "This is Test1"
#
# obj_t = Test1()
# print(obj_t)

# class Test2:
#     def __new__(cls, *args, **kwargs):
#         # print(cls.__name__)
#         return Test1()
#
#     def __init__(self):
#         print('__init__')
#
#     def __del__(self):
#         print('Test2 deleted')
#
#
# obj_t1 = Test2()
# print(obj_t1)
# del obj_t1
# print(obj_t1)
