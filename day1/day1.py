#!/usr/bin/env python3
# https://adventofcode.com/2020/day/1

def part_one():
    input_numbers = []
    with open("input.txt", "r") as in_file:
        for line in in_file:
            input_numbers.append(int(line.strip("\n")))


    for first_num in input_numbers:
        for second_num in input_numbers:
            if first_num + second_num == 2020:
                print(first_num * second_num)
                return

def part_two():
    input_numbers = []
    with open("input.txt", "r") as in_file:
        for line in in_file:
            input_numbers.append(int(line.strip("\n")))


    for first_num in input_numbers:
        for second_num in input_numbers:
            for third_num in input_numbers:
                if first_num + second_num + third_num == 2020:
                    print(first_num * second_num * third_num)
                    return

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()