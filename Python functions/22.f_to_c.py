'''
2. Read in a Fahrenheit temperature. Calculate and display the equivalent
centigrade temperature. The following formula is used for the conversion:
C = (5 / 9) * (F – 32)
'''


def f_to_c(f):
    c = (5 / 9) * (f - 32)
    print("{0} fahrenheit is {1} centigrade".format(f, c))
f_to_c(86)


