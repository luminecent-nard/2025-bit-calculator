
#ask user for width and loop until they enter a number that is more than 0
def int_check(question, low):
    error1 = F"please pick a number above or equal to {low}"
    error2 = "please pick a NUMBER to continue calculating"
    while True:

        try:
            #ask user for a number
            response = int(input(question))

            #check that width is more than 0
            if response >= low:
                return response
            else:
                print(error1)
        except ValueError:
            print(error2)


#main routine goes here
for item in range(0, 2):
    integer = int_check("integer: ", 1)
    print(integer)

print()

for item in range(0, 2):
    height = int_check("height: ", 1)
    print(height)

print()