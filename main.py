name = input("Enter your name: ")
print("Hi buddy! Today we will play a game " + name + "!")

print("Are you ready?")

question = input("Are you ready ? Yes or no: ")
print(name + " we are starting!")


liste1 = ['My neighbor ', 'My girlfriend ', 'My boyfriend ', 'My dog ']
num = input("Enter a number: ")

liste1 = liste1[int(num)]

liste2 = ['hates ', 'loves ', 'enjoys ', 'ridicules ']
num = input("Enter a number: ")

liste2 = liste2[int(num)]

liste3 = ['with me ', 'with my grandma ', 'with our home staff ', 'with our money ']
num = input("Enter a number: ")

liste3 = liste3[int(num)]

liste4 = ['in every situation ! ', 'until end of the world ! ']
num = input("Enter a number: ")

liste4 = liste4[int(num)]

print(liste1 + liste2 + liste3 + liste4)