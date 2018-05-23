def is_anagram(first, second):
    if len(first) != len(second):
        return False
    for letter in first.lower():
        if letter not in second.lower():
            return False
    for letter in second.lower():
        if letter not in first.lower():
            return False
    return True

print(is_anagram('Mary', 'army'));