import inflect


def function():
    p = inflect.engine()
    print('Enter a number')
    user_number = input()
    print(p.ordinal(user_number))


function()




