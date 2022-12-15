def calc_salt(value):
    try:
        a = int(value)/100
        return a
    except ValueError:
        print(f'invalid literal for int() with base 10: {value}')


print(calc_salt(2000))
print(calc_salt('2000'))
print(calc_salt('abc'))
