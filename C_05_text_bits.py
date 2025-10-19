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
text_ans = calc_text_bits()
print(text_ans)