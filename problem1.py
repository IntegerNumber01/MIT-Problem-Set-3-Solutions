# Problem 1
# Write two functions, called countSubStringMatch and countSubStringMatchRecursive that
# take two arguments, a key string and a target string. These functions iteratively and recursively count
# the number of instances of the key in the target string.

def countSubStringMatch(target, key):
    number = 0
    i = 0

    while i <= len(target):
        if not target.find(key, i) == -1:
            i = target.find(key, i)
            number += 1

        i += 1

    return number


def countSubStringMatchRecursive(target, key):
    i = target.find(key, 0)

    if not i == -1:
        return countSubStringMatchRecursive(target[i + 1:], key) + 1
    else:
        return 0


target = 'atgacatgcacaagtatgcat'
key = 'atgc'

print(countSubStringMatch(target, key))
print(countSubStringMatchRecursive(target, key))
