# How to run
The code is written in python3.
On a computer that has python3 installed, run it by "python sectra.py" in the terminal.
If I/O stream from textfile, run "python sectra.py test1.txt" in the terminal

# Code structure
The program's control flow is relatively straightforward.

The allowed operators are stated in a list at top of the file. To add more operators it first have to be added there and 
then it should also be added in do_operation()

It starts by checking if the user is reading from a file or inputs directly from the terminal.
Then it calls the function input_line()

input_line() is the main part of the program. There are a lot of comments and nothing complicated is happening there, see the comments.

Test case 3 is special as the commands have to be saved until the registers have values. 
This is done by having a dictionary with the saved commands with the left register has a key. 
Then when the left register should be printed it has to evaluate all the commands. 
It is possible that some registers are nested 

i.e. 

result = result - costs

costs = costs + salaries 

salaries = 20

Then result can not evaluate the first command immediately, as costs needs to have salaries evaluated before
it can be assigned value. 

This is solved with recursion in do_saved_commands()

Maybe that the evaluation should happen as soon as its possible, i.e. when every register have been assigned a value. But it is not necessary to check this every time a register is updated, better to wait until the evaluation is needed. The evaluation is only needed when a register is printed!


# Tests
The given tests and some further tests are included.

## Test 1,2,3
These are given, outputs correctly

## Test 4 
Simple add tester

## Test 5
Tests that commands are chained correctly. 

a=b=c=d=5 

print a should give 5

## Test 6
Saves a multiply d in buffer

Then adds values to a and d

result should be a=a*d

## test 7
saves a add b in buffer

then tries to print a. 

but b has no value

Requirements do not specificy what should happen.

This results in a key error.


## Test 8
does a add b twice

then gives a value to b

output should be a=b*2

## Test 9 
A requirement is that _any_ alphanumeric char can be a register

this means that integers can also be registers

This could result in user error but it works as specified

print 2 outputs 5

## test 10
Related to test 9. 

If 2 is defined as a register and the user wants to add 2 to the register 2

then the output will 0, as the register 2 now has the value 0.

Not a good requirement!

## test 11
Related to test 9,10

This first adds 3 to register 2. 

Then adds register 2 to register 3

reg 3 = 3

reg 2 = 3
