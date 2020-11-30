from math import floor
from part1 import part1

if __name__ == "__main__":
    with open('input.txt', 'r') as infile:
        for line in infile:
            input_data = list(map(int, line.split(',')))
            search = 19690720
            print(len(input_data))
            for noun in range(max(100, len(input_data))):
                for verb in range(max(100, len(input_data))):
                    data = list(input_data)
                    data[1] = noun
                    data[2] = verb
                    if part1(data)[0] == search:
                        print("Noun: {}".format(noun))
                        print("Verb: {}".format(verb))
                        print("100*Noun+Verb: {}".format(100*noun+verb))
