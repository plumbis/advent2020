#!/usr/bin/env python3
# https://adventofcode.com/2020/day/4
import json

'''
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)  # NULL is valid
'''

def load_data():
    with open("day4/input.txt", "r") as in_file:
        passports = []
        elements = []
        for line in in_file:
            if line == "\n":
                temp = {}
                for elem in elements:
                    temp.update(elem)
                passports.append(temp)
                elements = []
            else:
                for item in line.split(" "):
                    x = item.strip().split(":")
                    elements.append({x[0]: x[1]})
        else:
            temp = {}
            for elem in elements:
                temp.update(elem)
            passports.append(temp)
            elements = []
    return passports

def part_one():
    passports = load_data()
    valid_passports = 0

    for passport in passports:
        params = {"byr": False,
                  "iyr": False,
                  "eyr": False,
                  "hgt": False,
                  "hcl": False,
                  "ecl": False,
                  "pid": False,
                  "cid": True}
        for key in params:
            params[key] = (key in passport)

        valid = True

        for val in params:
            if val == "cid" and not val in passport:
                continue

            if not val in passport:
                valid = False

        if valid:
            valid_passports = valid_passports + 1


    print(valid_passports)

def part_two():
    pass

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()
