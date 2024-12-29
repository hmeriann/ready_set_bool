# III.0.1 Goal
# You must write a function that takes as parameters two natural numbers a and b and
# returns one natural number that equals a + b. However the only operations you’re
# allowed to use are:
# • & (bitwise AND)
# • | (bitwise OR)
# • ^ (bitwise XOR)
# • << (left shift)
# • >> (right shift)
# • = (assignment)
# • ==, !=, <, >, <=, >= (comparison operators)
# The incrementation operator (++ or += 1) is allowed only to increment the index of
# a loop and must not be used to compute the result itself.
# You must also turn in a main function in order to test your function, ready to be
# compiled (if necessary) and run.
# Prototype: fn adder(a: u32, b: u32) -> u32;

import argparse

def adder(a, b):
    while b != 0:
        sum_without_carry = (a ^ b) # = 1 if or a's or b's bite is 1
        carry = (a & b) << 1 # = 1 if in both it's = 1 but there will also be a carry
        # which needed to be shifted to the older register
        a = sum_without_carry
        # so when carry is 0 it could exit the loop
        b = carry
    return a


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("a", type=int, help="The first number.")
    parser.add_argument("b", type=int, help="The second number.")
    
    args = parser.parse_args()
    result = adder(args.a, args.b)
    print(f"The sum of {args.a} and {args.b} is {result}.")

# ex. 5 + 3
# 0101 | sum_without_carry (^) |   0110 | 0100 | 0000 | 0100 | a
# 0011 | carry (&) | (0001 << 1) = 0010 | 0100 | 0100 | 0000 | b