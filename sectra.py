allowed_operands=['ADD','SUBTRACT','MULTIPLY']
registers={}

def is_integer(val):
    try:
        integer=int(val)
        return True
    except ValueError:
        return False
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

        elif len(split_input)==2:
            if split_input[0]=="PRINT":
                print("now do prints")
                if split_input[1] in registers:
                    print(registers[split_input[1]])
                else:
                    print("this register does not exist! Error!")
            else:
                print("You input two commands, but the first one was not a print. Error!")
        elif len(split_input)==3:
            if split_input[1] not in allowed_operands:
                print("this operand is currently not supported")
            else:
                ### magic happens here

                # if gotten to this point the register will be a key in the registers dict
                key = split_input[0]

                # check first if key exists in registers. If not give it the value 0.
                # What will happen if reg1 MULTIPLY 5 happens when reg1 has no unassigned val?
                if key not in registers:
                    registers[key]=0
                print(registers)    
                operand = split_input[1]
                val_or_key = split_input[2]
                #since both values and registers can be in the third argument
                # it is necessary to check if it exists in the register dict
                # before doing any operations
                if val_or_key in registers:
                    key2=val_or_key
                    if operand == 'ADD':
                      registers[key]=registers[key]+registers[key2]
                elif is_integer(val_or_key):
                    print('its an int!')
                    integer=int(val_or_key)
                    if operand == 'ADD':
                      registers[key]=registers[key]+integer
                    print(registers)
                else:
                    print("this is not an integer, please enter integers!")
                    #if not it has to be a number, which has to be checked.
        else:
            print("You entered too many commands! Error!")
    else:
        print("you have to input something! Error!")
    
