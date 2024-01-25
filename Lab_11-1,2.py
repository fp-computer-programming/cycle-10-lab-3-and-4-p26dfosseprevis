def find_evens(num_a,num_b):
    o = []
    ask = input("Do you want to enter your own numbers? (y/n)")[0]
    if ask == "y":
        num_a = input("num_1:")
        num_b = input
    for num in range(num_a,num_b):
        if num == int(num/2)*2:
            o += num
    return o


def is_palandrome(text):
    text = list(text)
    for i,letter in enumerate(text):
        if letter == " ":
            text[i] = ""
    if 

