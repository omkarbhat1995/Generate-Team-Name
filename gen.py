#!/usr/bin/env python3
import constant
import random

"""
Function: Pre-Processes Data into a Predetermined Fashion
Parameter: List of Elements (Duplicate elements maybe present)
Return: List of Elements - Formatted Removed Duplicate
"""


def pre_process(a):
    a = list(set(a))
    for i in range(len(a)):
        a[i] = a[i].title()
    a = list(set(a))
    return a


"""
Function: Main to Generate a Randomized Team Name 
Parameters: Null
Returns: A Team Name
"""


def main():
    verb = pre_process(constant.verb)
    noun = pre_process(constant.noun)
    input = "Positive"
    try:
        if input == "Positive":
            adj = pre_process(constant.adj_pos)
            output = str(random.choice(verb)) + " " + str(random.choice(adj)) + " " + str(random.choice(noun))
        elif input == "Negative":
            adj = pre_process(constant.adj_neg)
            output = str(random.choice(verb)) + " " + str(random.choice(adj)) + " " + str(random.choice(noun))
    except Exception as e:
        print(f"Exception while creating a name: {e}")
    print(output)


"""
Checks if the code has a main, if it does it executes that.
"""

if __name__ == '__main__':
    main()
