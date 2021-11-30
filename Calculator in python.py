#                          /$\
#                         /$$$\
#                        /$$$$$\
#                       /$$$$$$$\
#                      /$$$$$$$$$\
#                     /$$$$$$$$$$$\
#                    /$$$$$$$$$$$$$\
#                   /$$$$$$$$$$$$$$$\
#                  /$$$$$$$$$$$$$$$$$\
#                 /$$$$$$$$$$$$$$$$$$$\
#                /$$$$$$$$$$$$$$$$$$$$$\
#               /$$$$ Made by t0sky $$$$\
#              /$$$$$$$$$$$$$$$$$$$$$$$$$\
#             /$$$$$$$$$$$$$$$$$$$$$$$$$$$\
#            /$$$$$$$$*************$$$$$$$$\
#           /$$$$$$$$$*************$$$$$$$$$\
#          /$$$$$$$$$$*************$$$$$$$$$$\
#         /$$$$$$$$$$$*************$$$$$$$$$$$\
#        /$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\
#       /$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\
#      /00000000000000000000000000000000000000000\

#      ## Old school python console calculator ##

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
print("\nfor addition press 1 \n"
      "for deficit press 2 \n"
      "for multiplication press 3 \n"
      "for division press 4 \n")

op = input("Which operation do you need to do? \n")
op = int(op)

if op == 1:
    result = float(num1) + float(num2)

if op == 2:
    result = float(num1) - float(num2)

if op == 3:
    result = float(num1) * float(num2)

if op == 4:
    result = float(num1) / float(num2)

print("Your result is: ")

# Display the result in int or float , so if it's an integer you don't get the .0!

if result == int(result):
    print(int(result))

else:
    print(float(result))