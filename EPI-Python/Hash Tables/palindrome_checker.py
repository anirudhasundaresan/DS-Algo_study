from collections import Counter


# this function is O(n) and space complexity is O(c) where c is the number of unique/ distinct chars in the word
def palindrome_checker(word):
    return len([x for x in Counter(word).values() if x % 2 != 0]) <= 1


print(palindrome_checker('edified'))
print(palindrome_checker('barabooffoo'))
print(palindrome_checker('levelrotator'))
