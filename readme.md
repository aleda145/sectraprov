test 3 is not behaving like the other two. create a stack for the prints?

Can't really do it linearly as done before.

# Tests

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
