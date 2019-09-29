import sys
allowed_operands=['ADD','SUBTRACT','MULTIPLY']
registers={}
saved_commands={}

def is_integer(val):
    try:
        integer=int(val)
        return True
    except ValueError:
        return False

def do_operation(val1, operand, val2):
    if operand =='ADD':
        return val1+val2
    if operand=='SUBTRACT':
        return val1-val2
    if operand=='MULTIPLY':
        return val1*val2

def do_saved_commands(key):
    for command in saved_commands[key]:
        if command[1] in saved_commands.keys():
            #its a key too! do recursion!
            do_saved_commands(command[1])
        registers[key]=do_operation(registers[key],command[0],registers[command[1]])
    #after executing the saved commands, delete them
    del saved_commands[key]

def input_line(input_data):
    
    if input_data:
        input_data=input_data.upper()
        # A requirement is for it to be case insensitive. Solved by only dealing with CAPITALS
        # when reading from file it is necessary to strip the input to remove trailing \n
        strip_input=input_data.strip()
        # after stripping split the input to isolate the commands
        split_input=strip_input.split(" ")
        # start by checking the length of the input
        if len(split_input)==1:
            print("Warning! one command inputs are not needed when reading from file.")
        elif len(split_input)==2:
            if split_input[0]=="PRINT":
                if split_input[1] in registers:
                    if split_input[1] in saved_commands.keys():
                        do_saved_commands(split_input[1])
                    print(registers[split_input[1]])
                else:
                    print("this register does not exist! Error!")
            else:
                print("You input two commands, but the first one was not a print. Error!")
        elif len(split_input)==3:
            if split_input[1] not in allowed_operands:
                print("this operand is currently not supported")
            else:
                # if gotten to this point the register will be a key in the registers dict
                key = split_input[0]
                # check first if key exists in registers. If not give it the value 0.
                if key not in registers:
                    registers[key]=0
                operand = split_input[1]
                val_or_key = split_input[2]
                # since both values and registers can be in the third argument
                # it is necessary to check if it exists in the register dict
                # before doing any operations
                if val_or_key in registers:
                    #if it is a register with assigned values, simply do the operation
                    key2=val_or_key
                    registers[key]=do_operation(registers[key], operand, registers[key2])
                elif is_integer(val_or_key):
                    integer=int(val_or_key)
                    registers[key]=do_operation(registers[key], operand, integer)
                else:
                    # if the input is not an existing register or an integer
                    # assume that its a register that will be assigned values later
                    # Then the commands have to be saved
                    if key not in saved_commands:
                        saved_commands[key]=[]
                    saved_commands[key].append([operand,val_or_key])
        else:
            print("You entered too many commands! Error!")
    else:
        print("you have to input something! Error!")

if len(sys.argv)==2:
    file_name=str(sys.argv[1])
    print("opening file:"+file_name)
    f = open(file_name,"r")
    for line in f:
        input_line(line)
    f.close()
else:
    while True:
        # A requirement is for it to be case insensitive. Solved by only dealing with CAPITALS
        input_data=input("enter input: ").upper()
        split_input=input_data.split(" ")    
        if len(split_input)==1:
            if split_input[0]=="QUIT":
                print("sequence finished, exiting")
                break
            else:
                print("You input only one command, but it is not a quit. Error!")
        else:
            input_line(input_data)
    
