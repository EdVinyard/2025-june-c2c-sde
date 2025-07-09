gradebook = [
    {'Name': 'Sule', 'Ratios Quiz': 90, 'Fractions HW': 100},
    {'Name': 'Maria', 'Ratios Quiz': 100, 'Fractions HW': 100},
    {'Name': 'Kirtan', 'Ratios Quiz': 95, 'Fractions HW': 100},
    {'Name': 'Lee', 'Ratios Quiz': 91, 'Fractions HW': 'Missing'},
    ]

for student in gradebook:
    print('~~~~~~~~~~~~')
    for key, value in student.items():
        print(f'{key}: {value}')
