# Problem 2
# Write the function subStringMatchExact. This function takes two arguments: a target string,
# and a key string. It should return a tuple of the starting points of matches of the key string in the target
# string, when indexing starts at 0.
# Test your function on each combination of key and target string


def subStringMatchExact(target, key):
    storage = []
    i = 0

    while i <= len(target):
        if not target.find(key, i) == -1:
            i = target.find(key, i)
            storage.append(i)

        i += 1

    return storage


def subStringMatchExactRecursive(target, key):
    i = target.find(key, 0)

    if i == -1: return []

    return subStringMatchExactRecursive(target[i + 1:], key) + [len(target[i + 1:])]


target = 'atgacatgcacaagtatgcat'
key = 'atgc'
key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

print(subStringMatchExact(target, key10))
print(subStringMatchExactRecursive(target, key10))
