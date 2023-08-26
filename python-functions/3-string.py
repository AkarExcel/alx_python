#!/usr/bin/env python3
#string reversal function
def reverse_string(string:str):
    word = string[::-1]
    return word

print(reverse_string("Hello"))
print(reverse_string(""))
print(reverse_string("madam"))
print(reverse_string("Hello, World!"))