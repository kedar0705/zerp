# # read file content
# file = open("demo.txt", 'r')
# print(file)
#
# print(file.readline())
#
# for i in file:
#     print(i)
#
# file.close()

# # append/write to file
# file = open("demo.txt", 'a')
# file.write("\n\nNew content!")
#
# file.close()
#
# file = open("demo.txt", 'r')
# print(file.read())

# # overwrite file
# file = open("demo.txt", 'w')
# file.write("Overwritten content")
# file.close()
#
# file = open("demo.txt", 'r')
# print(file.read())

# # create file 'x'
# file = open("demo1.txt", 'x')
# file.write(
#     "new Content"
# )
# print(file.read())

# file = open("demo2.txt", 'a')

# file = open("demo3.txt", 'w')

# import os

# # Delete existing file
#
# os.remove("demo1.txt")

# print(os.path.exists('demo.txt'))

# # create new directory
# os.makedirs('demo')

# # remove dir
# os.rmdir('demo')


# try:
#   f = open("demo.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")

# import os
# print(os.listdir())
#
# for i in os.listdir():
#     print(i)

