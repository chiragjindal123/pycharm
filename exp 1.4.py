#1.	Python program to check whether the string is Symmetrical or Palindrome
def is_palindrome(string):
    for i in range(len(string) // 2):
        if string[i] != string[-i-1]:
            return False
    return True


def is_symmetrical(string):
    n = len(string)

    left = 0
    right = n - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


string = "ababa"
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

if is_symmetrical(string):
    print("The string is symmetrical.")
else:
    print("The string is not symmetrical.")


#3.	Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. Example:- Sample String : 'abc' Expected Result : 'abcing' Sample String : 'string' Expected Result : 'stringly'

# def add_suffix(string):
#     if len(string) < 3:
#         return string
#     elif string[-3:] == 'ing':
#         return string + 'ly'
#     else:
#         return string + 'ing'
#
#
# string1 = 'abc'
# string2 = 'string'
# string3 = 'do'
#
# print(add_suffix(string1))
# print(add_suffix(string2))
# print(add_suffix(string3))


# string1 = input("Enter the first string: ")
# string2 = input("Enter the second string: ")
# words1 = string1.split()
# words2 = string2.split()
# uncommon_words = set(words1).symmetric_difference(set(words2))
# print("Uncommon words: ", end="")
# for word in uncommon_words: print(word, end=" ")
#
