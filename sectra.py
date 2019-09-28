allowed_operands=['ADD','SUBTRACT','MULTIPLY']

while True:    
    input_data=input("enter input").upper()
    # A requirement is for it to be case insensitive. Solved by only dealing with CAPITALS

    print(input_data)
    split_input=input_data.split(" ")
    print(split_input)
    if len(split_input)==1:
        if split_input[0]=="QUIT":
            print("sequence finished, exiting")
            #after this all prints should happen
            break;

    if len(split_input)==2:
        if split_input[0]=="PRINT":
            print("now do prints")
        else:
            print("You input two commands, but the first one was not a print. Error!")
    if len(split_input)==3:

        if split_input[1] not in allowed_operands:
            print("this operand is currently not supported")
    
