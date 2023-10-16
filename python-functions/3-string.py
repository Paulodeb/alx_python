def reverse_string(string):
    return string[slice(None, None, -1)]



print(reverse_string("Hello"))
print(reverse_string(""))
print(reverse_string("madam"))
print(reverse_string("Hello, World!"))