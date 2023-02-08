# Problem 4
# Write a function, called subStringMatchOneSub which takes two arguments: a target
# string and a key string. This function should return a tuple of all starting points of matches of the key to
# the target, such that at exactly one element of the key is incorrectly matched to the target.

import problem2 as p2
import problem3 as p3


def subStringMatchExactlyOneSub(target, key):
    main = list(p3.subStringMatchOneSub(key, target))
    delete = p2.subStringMatchExact(target, key)

    for a in range(len(main)):
        for i in delete:
            if i in main:
                main.remove(i)

    return main


def recursive_delete(main, delete):
    if len(main) == 0:
        return []

    if main[0] in delete:
        return recursive_delete(main[1:], delete)
    else:
        return [main[0]] + recursive_delete(main[1:], delete)


def subStringMatchExactlyOneSubRecursive(target, key):
    main = list(p3.subStringMatchOneSub(key, target))
    delete = p2.subStringMatchExact(target, key)

    return recursive_delete(main, delete)


string = 'atgacatgcacaagtatgcat'
key = 'atgc'

print(subStringMatchExactlyOneSub(string, key))
print(subStringMatchExactlyOneSubRecursive(string, key))
