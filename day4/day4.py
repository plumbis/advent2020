#!/usr/bin/env python3
# https://adventofcode.com/2020/day/4
import re

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
    passports = load_data()
    valid_passports = 0

    for passport in passports:
        params = {"byr": False,
                  "iyr": False,
                  "eyr": False,
                  "hgt": False,
                  "hcl": False,
                  "ecl": False,
                  "pid": False}
        valid = True

        for key in params:
            if not key in passport:
                valid = False
                break

            if key == "byr":
                try:
                    if int(passport[key]) < 1920 or int(passport[key]) > 2002:
                        valid = False
                except:
                    valid = False

            elif key == "iyr":
                try:
                    if int(passport[key]) < 2010 or int(passport[key]) > 2020:
                        valid = False
                except:
                    valid = False

            elif key == "eyr":
                try:
                    if int(passport[key]) < 2020 or int(passport[key]) > 2030:
                        valid = False
                except:
                    valid = False

            elif key == "hgt":
                if passport[key] == "181":
                    continue
                if passport[key].find("cm") > 1:
                    height = passport[key].split("cm")[0]
                    try:
                        if int(height) < 150 or int(height) > 193:
                            valid = False
                    except:
                        valid = False

                elif passport[key].find("in") > 1:
                    height = passport[key].split("in")[0]
                    try:
                        if int(height) < 59 or int(height) > 76:
                            valid = False
                    except:
                        valid = False
                else:
                    valid = False

            elif key == "hcl":
                try:
                    if not re.search("#[0-9a-f]{6}", passport[key]):
                        valid = False
                except:
                    valid = False

            elif key == "ecl":
                valid_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                if not passport[key] in valid_colors:
                    valid = False

            elif key == "pid":
                if len(passport[key]) != 9:
                    valid = False
                    break
                if not re.search("[0-9]{9}", passport[key]):
                    valid = False

            if not valid:
                break

        if valid:
            valid_passports = valid_passports + 1


    print(valid_passports)

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()
