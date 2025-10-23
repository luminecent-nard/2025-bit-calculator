#functions go here
def statement_generator(statement, decoration):
    print(f"{decoration * 5}{statement}{decoration * 5}")

#display instructions
def instructions():
    statement_generator("instructions","=")

    print('''
instructions go here.
- instruction 1
- instruction 2
''')


#asks user for file type
def get_filetype():
    while True:
        response = input("file type: ").lower()
        #check for 'i' or the exit code
        if response == "xxx" or response == "i":
            return response
    #check if it's an integer
        elif response in ['integer','int']:
            return "integer"
    #check if it's an image
        elif response in ['image','photo','img','p']:
            return "image"
    #check if its text
        elif response in ['text','txt','t',]:
            return "text"
    #this was for a dare i swear please ignore this
        elif response in ['pron','secks','fucc']:
            print("woah there buddy, no need to be freaky. this is a no freaky zone")
    #if the response is invalid
        else:
            print("please enter valid file type (int,img,txt)")

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

#calculates how many bits are needed to represent an image
def image_calc():
    #get image dimensions
    width = int_check("width: ", 1)
    height = int_check("height: ", 1)

#calcylate number of pixels and multiply by 24 to get bits
    num_pixels = width * height
    num_bits =  num_pixels * 24

#set up answer and return it
    return (f"number of pixels: {width} x {height} = {num_pixels} "
              f"\nnumber of bits: {num_pixels} x 24 = {num_bits}")

#calculates how many bits are needed to represent an integer
def integer_calc():
    #get image dimensions
    integer = int_check("integer: ", 0)


#convert int to binary

    raw_binary = bin(integer)

#remove the leading 0b
    binary = raw_binary[2:]
    num_bits = len(binary)
#set up answer and return it
    answer = f"{integer} in binary is {binary}. we need {num_bits} bits to represent it "
    return answer

#calculates number of bits needed to represent text in ascii
def calc_text_bits():
    pass

    #get text from user
    response = input("enter some text: ")

    #calculate bits needed
    num_chars = len(response)
    num_bits = num_chars * 8

    #set up answer and return it
    answer = (f"{response} has {num_chars} characters."
              f"\nwe need {num_chars} x 8 bits to represent it"
              f"\n{response} needs {num_bits} bits to store it")
    #retunt the calculated answer
    return answer





#main routine goes here

#display instructions if requested
want_instruction = input("press 〈enter〉 to view instructions,\n "
                         "or any key to continue ")
print()

if want_instruction == "":
    instructions()

while True:
    file_type = get_filetype()

    if file_type == "xxx":
        print("thank you for using the bit calculator")
        break

    print(f"you chose {file_type}")

    # if user chose "I" ask whether integer ot image
    if file_type == "i":
        want_image = input("press 〈enter〉 for a integer or any key for a image ")
        if want_image == "":
            file_type = "integer"

        else:
            file_type = "image"

    if file_type == "image":

        image_ans = image_calc()
        print(image_ans)

    elif file_type == "integer":

        integer_ans = integer_calc()
        print(integer_ans)

    else:
        text_ans = calc_text_bits()
        print(text_ans)



