#!/usr/bin/env python3
import constant
import random


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
    # Input from user
    if input =="Positive":
        adj = pre_process(constant.adj_pos)
        output = str(random.choice(verb)) + " " + str(random.choice(adj)) + " " + str(random.choice(noun))
    else:
        adj = pre_process(constant.adj_neg)
        output = str(random.choice(verb)) + " " + str(random.choice(adj)) + " " + str(random.choice(noun))
    print(output)


if __name__ == '__main__':
    main()
