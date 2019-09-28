while True:    
    input_data=input("enter input")
    
    print(input_data)
    if input_data=="quit":
        print("sequence finished, exiting")
        #after this all prints should happen
        break;
    split_input=input_data.split(" ")
    print(split_input)
    if split_input[0]=="print":
        print("now do prints")
