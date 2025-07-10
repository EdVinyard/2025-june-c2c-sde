#--------------------------------------------------------------------
# (1) What will the following code print?

string_value = 'orange'
try:
    float_value = float(string_value)
    print('valid floating point value')
except ValueError:
    print('invalid floating point value')


#--------------------------------------------------------------------
# (2) What will the following code print?

def tax_included(subtotal, tax_rate):
    tax_amount = subtotal * tax_rate
    total = subtotal + tax_amount
    return total

total = tax_included(100.00, 0.08)
print(total)
