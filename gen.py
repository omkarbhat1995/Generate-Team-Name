#!/usr/bin/env python3
import constant
import random


def pre_process(a):
    a = list(set(a))
    for i in range(len(a)):
        a[i] = a[i].title()
    a = list(set(a))
    return a


def main():
    adj = pre_process(constant.adj)
    noun = pre_process(constant.noun)
    output = str(random.choice(adj)) + " " + str(random.choice(noun))
    print(output)


if __name__ == '__main__':
    main()
