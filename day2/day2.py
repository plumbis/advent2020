#!/usr/bin/env python3
# https://adventofcode.com/2020/day/2

import re

# 5-11 t: glhbttzvzttkdx
def part_one():
    valid_passwords = 0
    with open("day2/input.txt", "r") as in_file:
        for line in in_file:
            policy = line[:line.find(" ")].strip()
            policy_low = int(policy[:policy.find("-")])
            policy_high = int(policy[policy.find("-") + 1:])
            password = line[line.find(":") + 1:].strip()
            letter = line[line.find(" "):line.find(":")].strip()

            letter_count = 0
            for char in password:
                if char == letter:
                    letter_count = letter_count + 1

            if letter_count <= policy_high and letter_count >= policy_low:
                valid_passwords = valid_passwords + 1

    print(valid_passwords)

def part_two():
    pass

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()