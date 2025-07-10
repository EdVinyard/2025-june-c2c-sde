def reverse_string(s):
    reversed_str = ''
    for i in range(len(s)-1, -1, -1):
        reversed_str += s[i]
    return reversed_str

print(reverse_string(''))
print(reverse_string('x'))
print(reverse_string('01'))
print(reverse_string('This is a test.'))
