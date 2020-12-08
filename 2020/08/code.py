# Advent of Code 2020
# Day 08
# Author: irobin591

import os
import doctest
import re

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip().split('\n')

regex_instruction = re.compile(r'^(nop|acc|jmp) ((?:\+|-)[0-9]+)$')

class HandheldComputer():
    def __init__(self, asm_list):
        self.instructions = []
        # for each line do
        for asm in asm_list:
            # use regex to extract operation and argument
            r = regex_instruction.match(asm)

            if not r:
                raise RuntimeError('No valid instruction provided')

            # create a dict containing operation, argument (and loop count?)
            self.instructions.append({
                'operation': r.group(1),
                'argument': int(r.group(2)),
                'loop count': 0,
            })

    def get_current_acc(self):
        return self._acc

    def get_instruction(self, no):
        return self.instructions[no]

    def __iter__(self):
        # Create Iterator with start instruction 0
        self._cur_instruction = 0
        self._acc = 0
        return self

    def __next__(self):
        # Abort if the code runs though
        if self._cur_instruction >= len(self.instructions):
            raise StopIteration
        
        # parse current instruction, run it and go to next instruction if needed
        old_instruction = self.instructions[self._cur_instruction]
        # old_instruction['next_instruction'] = old_instruction['instruction']
        old_instruction['acc'] = self.get_current_acc()
        self.instructions[self._cur_instruction]['loop count'] += 1

        # run instruction
        if old_instruction['operation'] == 'jmp':
            self._cur_instruction += old_instruction['argument']
        elif old_instruction['operation'] == 'acc':
            self._cur_instruction += 1
            self._acc += old_instruction['argument']
        elif old_instruction['operation'] == 'nop':
            self._cur_instruction += 1
        else:
            # Something is wrong with the regex
            raise RuntimeError("Something is wrong with the regex!")

        # Increase executed amount

        # return old instruction
        return old_instruction

    def check_loop(self):
        # Iterate though computed instructions
        for instruction in self:
            # If the same instruction would be executed twice, return current acc
            if instruction['loop count'] > 1:
                return True
        return False

def part1(input_data):
    """
    >>> part1(["nop +0","acc +1","jmp +4","acc +3","jmp -3","acc -99","acc +1","jmp -4","acc +6"])
    5
    """
    computer = HandheldComputer(input_data)

    # Iterate though computed instructions
    for instruction in computer:
        # If the same instruction would be executed twice, return current acc
        if instruction['loop count'] > 1:
            return instruction['acc']
    return 0


def part2(input_data):
    """
    >>> part2(["nop +0","acc +1","jmp +4","acc +3","jmp -3","acc -99","acc +1","jmp -4","acc +6"])
    8
    """

    # Iterate though list of instructions
    for i in range(len(input_data)):
        # Create new computer
        computer = HandheldComputer(input_data)
        # Modify instruction i
        cur_op = computer.get_instruction(i)['operation']
        if cur_op == 'nop':
            computer.get_instruction(i)['operation'] = 'jmp'
        elif cur_op == 'jmp':
            computer.get_instruction(i)['operation'] = 'nop'
        else:
            # operation is neither nop nor jmp: 
            #    computer will not changed -> skip this change
            continue

        # Check if the computer would compute fully:
        if not computer.check_loop():
            return computer.get_current_acc()

    return None


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass