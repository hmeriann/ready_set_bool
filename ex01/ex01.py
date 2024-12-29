# The goal is the same as the previous exercise, except the returned natural number equals
# a * b. The only operations you’re allowed to use are:
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
# Prototype: fn multiplier(a: u32, b: u32) -> u32;

import argparse

def multiplier(a, b):
    result = 0
    while b > 0:
        if b & 1:
            result += a
        a <<= 1
        b >>= 1
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("a", type=int, help="The first number.")
    parser.add_argument("b", type=int, help="The second number.")
    
    args = parser.parse_args()
    result = multiplier(args.a, args.b)
    print(f"The multiplication of {args.a} and {args.b} is {result}.")

# ex. 5 * 3
# 0101 | a | 1010 | 0100 
# 0011 | b | 0001 | 0000 
# result   | +3   | +6