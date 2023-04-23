import turtle


turtle.color('purple', 'yellow')
turtle.bgcolor('color')

# for i in range(4)
#     turtle.right(90)
#     turtle.forward(100)

# for i in range(25)
#     turtle.right(15)
#     turtle.forward(10)

# якщо умова = Правда:
#       дія
# '10' + '10'

# num1 = int(input('Ведіть число: '))
# num2 = input('Ведіть число: ')




# while True:
#     num1 = int(input())
#     num2 = int(input())
#     s = input()

#     if type(num1) == type(num2):
#         if type(s) == str:
#             if s == "+":
#                 print(num1 + num2)
#             if s == "-":
#                 print(num1 - num2)
#             if s == "*":
#                 print(num1 * num2)
#             if s == "/":
#                 print(num1 / num2)
#             if s == "exit":
#                 break

while True:
    s = input('Ведіть фігуру: ').split('')

    if s == "square":
        for i in range(4):
            if len(s) > 1:
                turtle.right(int(s[1]))
                if len(s) > 2:
                    turtle.forward(int(s[2]))
                else:
                    turtle.right(int(s[1]))
                    turtle.forward(100)
            else:
                turtle.right(90)
                turtle.forward(100)
    elif s[0] == "circle":
        for i in range(25):
            turtle.right(100)









