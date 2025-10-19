
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

#calculates how many bits are needed to represent an integer
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

#main routine goes here
image_ans = image_calc()
print(image_ans)
