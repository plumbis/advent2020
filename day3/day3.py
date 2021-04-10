#!/usr/bin/env python3
# https://adventofcode.com/2020/day/3

# 5-11 t: glhbttzvzttkdx
def process_slope(right_offset=3, down_offset=1,verbose=False):
    right_pos = 0
    trees = 0
    skip_count = down_offset

    with open("day3/input.txt", "r") as in_file:
        for line in in_file:
            line = line.strip()
            if right_pos == 0:
                right_pos = right_pos + right_offset
                if verbose:
                    print(line)
                continue


            if skip_count > 1:
                skip_count = skip_count - 1
                continue

            index = right_pos

            if right_pos >= len(line):
                index = right_pos % (len(line))

            if line[index] == "#":
                trees = trees + 1
                if verbose:
                    print(line[:index] + "O" + line[index + 1:] + " // Tree")
            else:
                if verbose:
                    print(line[:index] + "O" + line[index + 1:])

            skip_count = down_offset
            right_pos = right_pos + right_offset

    return trees

def part_one():
    print(process_slope(verbose=False))

def part_two():
    print(process_slope(1,1) * process_slope(3,1) * process_slope(5,1) * process_slope(7,1) * process_slope(1,2))

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()