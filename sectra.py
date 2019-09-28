allowed_operands=['ADD','SUBTRACT','MULTIPLY']
registers={}

while True:    
    input_data=input("enter input").upper()
    # A requirement is for it to be case insensitive. Solved by only dealing with CAPITALS

    print(input_data)
    #only do things if input_data is not empty
    if input_data:
        split_input=input_data.split(" ")
        print(split_input)

        #start by checking the length of the input
        if len(split_input)==1:
            if split_input[0]=="QUIT":
                print("sequence finished, exiting")
                break;
            else:
                print("You input only one command, but is not a quit. Error!")

        if len(split_input)==2:
            if split_input[0]=="PRINT":
                print("now do prints")
            else:
                print("You input two commands, but the first one was not a print. Error!")
        if len(split_input)==3:
            if split_input[1] not in allowed_operands:
                print("this operand is currently not supported")
            else:
                ### magic happens here

                # if gotten to this point the register will be a key in the registers dict
                key = split_input[0]
                operand = split_input[1]
                val_or_key = split_input[2]
                    
        else:
            print("You entered too many commands! Error!")
    else:
        print("you have to input something! Error!")
    
