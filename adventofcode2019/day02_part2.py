#! Python 3
'''
--- Part Two ---
"Good, the new computer seems to be working correctly! Keep it nearby during this mission - you'll probably use it
again. Real Intcode computers support many more features than your new one, but we'll let you know what they are
as you need them."

"However, your current priority should be to complete your gravity assist around the Moon. For this mission to
succeed, we should settle on some terminology for the parts you've already built."

Intcode programs are given as a list of integers; these values are used as the initial state for the computer's
memory. When you run an Intcode program, make sure to start by initializing memory to the program's values.
A position in memory is called an address (for example, the first value in memory is at "address 0").

Opcodes (like 1, 2, or 99) mark the beginning of an instruction. The values used immediately after an opcode,
if any, are called the instruction's parameters. For example, in the instruction 1,2,3,4, 1 is the opcode; 2, 3,
and 4 are the parameters. The instruction 99 contains only an opcode and has no parameters.

The address of the current instruction is called the instruction pointer; it starts at 0. After an instruction
finishes, the instruction pointer increases by the number of values in the instruction; until you add more
instructions to the computer, this is always 4 (1 opcode + 3 parameters) for the add and multiply
instructions. (The halt instruction would increase the instruction pointer by 1, but it halts the program instead.)

"With terminology out of the way, we're ready to proceed. To complete the gravity assist, you need to determine
what pair of inputs produces the output 19690720."

The inputs should still be provided to the program by replacing the values at addresses 1 and 2, just like
before. In this program, the value placed in address 1 is called the noun, and the value placed in address 2 is
called the verb. Each of the two input values will be between 0 and 99, inclusive.

Once the program has halted, its output is available at address 0, also just like before. Each time you try
a pair of inputs, make sure you first reset the computer's memory to the values in the
program (your puzzle input) - in other words, don't reuse memory from a previous attempt.

Find the input noun and verb that cause the program to produce the output 19690720. What is 100 * noun + verb?
(For example, if noun=12 and verb=2, the answer would be 1202.)
'''

input_list = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,5,23,1,23,5,27,2,27,10,31,1,31,9,35,1,35,5,39,1,6,39,43,2,9,43,47,1,5,47,51,2,6,51,55,1,5,55,59,2,10,59,63,1,63,6,67,2,67,6,71,2,10,71,75,1,6,75,79,2,79,9,83,1,83,5,87,1,87,9,91,1,91,9,95,1,10,95,99,1,99,13,103,2,6,103,107,1,107,5,111,1,6,111,115,1,9,115,119,1,119,9,123,2,123,10,127,1,6,127,131,2,131,13,135,1,13,135,139,1,9,139,143,1,9,143,147,1,147,13,151,1,151,9,155,1,155,13,159,1,6,159,163,1,13,163,167,1,2,167,171,1,171,13,0,99,2,0,14,0]

def solved_it(input_list):
    array = input_list[:]
    
    for index in range (0, len(array), 4): #range (start, stop[, step])
        operator = array[index]
        first_number = array[array[index + 1]]
        second_number = array[array[index + 2]]
        
        if operator == 99:
            return array[0]
        
        elif operator == 1:
            array[array[index+3]] = first_number + second_number
        
        elif operator == 2:
            array[array[index+3]] = first_number * second_number
            
    return array[0]
    
for noun in range(100):

    for verb in range(100):
        input_list[1] = noun
        input_list[2] = verb
        output = solved_it(input_list)

        if output == 19690720:
            print(100 * noun + verb)
            break
