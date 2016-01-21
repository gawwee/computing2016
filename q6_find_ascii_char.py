x=True
while x:
    try:
        input_character=int(input("Please enter an integer between 0 and 127:"))
        out_char=chr(input_character)
        if 0<input_character<127:
            print("Your char is:",out_char)
            x=False

        else:
            print("This integer is not between 0 and 127!")

    except ValueError:
            print("Not interger")
