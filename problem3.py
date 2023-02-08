# Problem 3
# Write a function, called contrainedMatchPair which takes three arguments: a tuple
# representing starting points for the first substring, a tuple representing starting points for the second
# substring, and the length of the first substring. The function should return a tuple of all members (call
# it n) of the first tuple for which there is an element in the second tuple (call it k) such that n + m + 1 = k,
# where m is the length of the first substring.

# To test this function, we have provided a function called subStringMatchOneSub, which takes two
# arguments: a target string and a key string. This function will return a tuple of all starting points of
# matches of the key to the target, such that at most one element of the key is incorrectly matched to the
# target.

import problem2 as p2


def constrainedMatchPair(firstMatch, secondMatch, length):
    storage = ()

    for a in firstMatch:
        for b in secondMatch:
            if a + length + 1 == b:
                storage = storage + (a,)

    return storage


def check_secondMatch(element, secondMatch, length):
    for i in range(len(secondMatch)):
        if element + length + 1 == secondMatch[i]:
            return True

    return False


def constrainedMatchPairRecursive(firstMatch, secondMatch, length):
    if len(firstMatch) <= 0:
        return ()

    if check_secondMatch(firstMatch[0], secondMatch, length) is True:
        return (firstMatch[0],) + constrainedMatchPairRecursive(firstMatch[1:], secondMatch, length)
    else:
        return constrainedMatchPairRecursive(firstMatch[1:], secondMatch, length)


def subStringMatchOneSub(key, target):
    """ search for all locations of key in target, with one substitution """
    allAnswers = ()
    for miss in range(len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss + 1:]
        print('breaking key', str(key), 'into', str(key1), str(key2))
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = p2.subStringMatchExact(target, key1)
        match2 = p2.subStringMatchExact(target, key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPairRecursive(match1, match2, len(key1))
        allAnswers = allAnswers + filtered
        print('match1', match1)
        print('match2', match2)
        print('possible matches for', str(key1), str(key2), 'start at', str(filtered))

    return allAnswers


string = 'atgacatgcacaagtatgcat'
key = 'atgc'

print(subStringMatchOneSub(key, string))
