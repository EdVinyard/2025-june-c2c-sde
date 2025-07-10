#----------------------------------------------------------------
# (1) What will the following code print?

string_value = 'orange'
try:
    float_value = float(string_value)       # raise ValueError
    print('valid floating point value')     # never runs!
except ValueError:
    print('invalid floating point value')   # skip to this line


#----------------------------------------------------------------
# (2) What will the following code print?

def tax_included(subtotal, tax_rate):
    tax_amount = subtotal * tax_rate    # 100.00 * 0.08 => 8.0
    total = subtotal + tax_amount       # 100.00 + 8.00 => 108.0
    return total

total = tax_included(100.00, 0.08)
print(total) # prints "108.0"
