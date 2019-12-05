#!Python3
'''
--- Day 5: Sunny with a Chance of Asteroids ---
You're starting to sweat as the ship makes its way toward Mercury. The Elves suggest that you get the air
conditioner working by upgrading your ship computer to support the Thermal Environment Supervision Terminal.

The Thermal Environment Supervision Terminal (TEST) starts by running a diagnostic program (your puzzle input).
The TEST diagnostic program will run on your existing Intcode computer after a few modifications:

First, you'll need to add two new instructions:

Opcode 3 takes a single integer as input and saves it to the position given by its only parameter. For example,
the instruction 3,50 would take an input value and store it at address 50.
Opcode 4 outputs the value of its only parameter. For example, the instruction 4,50 would output the value at
address 50.
Programs that use these instructions will come with documentation that explains what should be connected to the
input and output. The program 3,0,4,0,99 outputs whatever it gets as input, then halts.

Second, you'll need to add support for parameter modes:

Each parameter of an instruction is handled based on its parameter mode. Right now, your ship computer already
understands parameter mode 0, position mode, which causes the parameter to be interpreted as a position - if the
parameter is 50, its value is the value stored at address 50 in memory. Until now, all parameters have been in
position mode.

Now, your ship computer will also need to handle parameters in mode 1, immediate mode. In immediate mode, a
parameter is interpreted as a value - if the parameter is 50, its value is simply 50.

Parameter modes are stored in the same value as the instruction's opcode. The opcode is a two-digit number based
only on the ones and tens digit of the value, that is, the opcode is the rightmost two digits of the first value
in an instruction. Parameter modes are single digits, one per parameter, read right-to-left from the opcode: the
first parameter's mode is in the hundreds digit, the second parameter's mode is in the thousands digit, the third
parameter's mode is in the ten-thousands digit, and so on. Any missing modes are 0.

For example, consider the program 1002,4,3,4,33.

The first instruction, 1002,4,3,4, is a multiply instruction - the rightmost two digits of the first value, 02,
indicate opcode 2, multiplication. Then, going right to left, the parameter modes are 0 (hundreds digit), 1
(thousands digit), and 0 (ten-thousands digit, not present and therefore zero):

ABCDE
 1002

DE - two-digit opcode,      02 == opcode 2
 C - mode of 1st parameter,  0 == position mode
 B - mode of 2nd parameter,  1 == immediate mode
 A - mode of 3rd parameter,  0 == position mode,
                                  omitted due to being a leading zero
This instruction multiplies its first two parameters. The first parameter, 4 in position mode, works like it did
before - its value is the value stored at address 4 (33). The second parameter, 3 in immediate mode, simply has
value 3. The result of this operation, 33 * 3 = 99, is written according to the third parameter, 4 in position
mode, which also works like it did before - 99 is written to address 4.

Parameters that an instruction writes to will never be in immediate mode.

Finally, some notes:

It is important to remember that the instruction pointer should increase by the number of values in the
instruction after the instruction finishes. Because of the new instructions, this amount is no longer always 4.
Integers can be negative: 1101,100,-1,4,0 is a valid program (find 100 + -1, store the result in position 4).
The TEST diagnostic program will start by requesting from the user the ID of the system to test by running an
input instruction - provide it 1, the ID for the ship's air conditioner unit.

It will then perform a series of diagnostic tests confirming that various parts of the Intcode computer, like
parameter modes, function correctly. For each test, it will run an output instruction indicating how far the
result of the test was from the expected value, where 0 means the test was successful. Non-zero outputs mean that
a function is not working correctly; check the instructions that were run before the output instruction to see
which one failed.

Finally, the program will output a diagnostic code and immediately halt. This final output isn't an error; an
output followed immediately by a halt means the program finished. If all outputs were zero except the diagnostic
code, the diagnostic program ran successfully.

After providing 1 to the only input instruction and passing all the tests, what diagnostic code does the program
produce?
'''

###From day2 part 2
##input_list = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,5,23,1,23,5,27,2,27,10,31,1,31,9,35,1,35,5,39,1,6,39,43,2,9,43,47,1,5,47,51,2,6,51,55,1,5,55,59,2,10,59,63,1,63,6,67,2,67,6,71,2,10,71,75,1,6,75,79,2,79,9,83,1,83,5,87,1,87,9,91,1,91,9,95,1,10,95,99,1,99,13,103,2,6,103,107,1,107,5,111,1,6,111,115,1,9,115,119,1,119,9,123,2,123,10,127,1,6,127,131,2,131,13,135,1,13,135,139,1,9,139,143,1,9,143,147,1,147,13,151,1,151,9,155,1,155,13,159,1,6,159,163,1,13,163,167,1,2,167,171,1,171,13,0,99,2,0,14,0]
##
##def solved_it(input_list):
##    array = input_list[:]
##    
##    for index in range (0, len(array), 4): #range (start, stop[, step])
##        operator = array[index]
##        first_number = array[array[index + 1]]
##        second_number = array[array[index + 2]]
##        
##        if operator == 99:
##            return array[0]
##        
##        elif operator == 1:
##            array[array[index+3]] = first_number + second_number
##        
##        elif operator == 2:
##            array[array[index+3]] = first_number * second_number
##            
##    return array[0]
##    
##for noun in range(100):
##
##    for verb in range(100):
##        input_list[1] = noun
##        input_list[2] = verb
##        output = solved_it(input_list)
##
##        if output == 19690720:
##            print(100 * noun + verb)
##            break

input_list = [3,225,1,225,6,6,1100,1,238,225,104,0,101,20,183,224,101,-63,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,1101,48,40,225,1101,15,74,225,2,191,40,224,1001,224,-5624,224,4,224,1002,223,8,223,1001,224,2,224,1,223,224,223,1101,62,60,225,1102,92,15,225,102,59,70,224,101,-885,224,224,4,224,1002,223,8,223,101,7,224,224,1,224,223,223,1,35,188,224,1001,224,-84,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1001,66,5,224,1001,224,-65,224,4,224,102,8,223,223,1001,224,3,224,1,223,224,223,1002,218,74,224,101,-2960,224,224,4,224,1002,223,8,223,1001,224,2,224,1,224,223,223,1101,49,55,224,1001,224,-104,224,4,224,102,8,223,223,1001,224,6,224,1,224,223,223,1102,43,46,225,1102,7,36,225,1102,76,30,225,1102,24,75,224,101,-1800,224,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1101,43,40,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,226,226,224,1002,223,2,223,1005,224,329,1001,223,1,223,8,226,677,224,102,2,223,223,1006,224,344,1001,223,1,223,1007,226,677,224,1002,223,2,223,1005,224,359,101,1,223,223,1008,677,226,224,102,2,223,223,1006,224,374,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,389,1001,223,1,223,107,677,677,224,1002,223,2,223,1006,224,404,101,1,223,223,1007,226,226,224,1002,223,2,223,1006,224,419,101,1,223,223,7,677,226,224,1002,223,2,223,1005,224,434,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,449,101,1,223,223,107,226,226,224,1002,223,2,223,1006,224,464,1001,223,1,223,1108,677,677,224,1002,223,2,223,1005,224,479,101,1,223,223,8,677,226,224,1002,223,2,223,1006,224,494,101,1,223,223,7,226,677,224,102,2,223,223,1005,224,509,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,524,1001,223,1,223,1108,677,226,224,1002,223,2,223,1005,224,539,1001,223,1,223,1108,226,677,224,102,2,223,223,1006,224,554,101,1,223,223,108,226,677,224,102,2,223,223,1005,224,569,1001,223,1,223,8,677,677,224,1002,223,2,223,1005,224,584,101,1,223,223,108,677,677,224,1002,223,2,223,1005,224,599,1001,223,1,223,108,226,226,224,102,2,223,223,1006,224,614,101,1,223,223,1008,677,677,224,102,2,223,223,1006,224,629,1001,223,1,223,107,226,677,224,102,2,223,223,1006,224,644,101,1,223,223,1107,677,677,224,1002,223,2,223,1005,224,659,1001,223,1,223,7,226,226,224,1002,223,2,223,1005,224,674,101,1,223,223,4,223,99,226]

def solved_it(input_list):
    array = input_list[:]
    
    for index in range (0, len(array), 4): #range (start, stop[, step])
        operator = array[index]
        first_number = array[array[index + 1]]
        second_number = array[array[index + 2]]
        
        if operator == 99:
            return array[0]
        
        elif operator == 1: #Opcode 1 adds together numbers read from two positions
            array[array[index+3]] = first_number + second_number
        
        elif operator == 2: #Opcode 2 multiplies the two inputs
            array[array[index+3]] = first_number * second_number

        elif operator == 3: #Opcode 3 takes a single integer and saves it to position given by parameter
            #3, 50 would take an input value and store it at address 50
            #int_list[int_list[pointer + 1]] = ac_id_input
            #pointer = pointer + 2
            array[array[index + 1]] = 0 #takes some sort of input
            
    return array[0]
    
for noun in range(100):

    for verb in range(100):
        input_list[1] = noun
        input_list[2] = verb
        output = solved_it(input_list)

        if output == 19690720:
            print(100 * noun + verb)
            break
