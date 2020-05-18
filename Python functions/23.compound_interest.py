'''
3. Calculate the amount obtained by investing the principal (P) for (N) years
at the rate of (R). The following formula is used for the conversion:
A = P * (1 + R) ^ N
'''


def compound_interest(p, r, n):
    return p * (1 + r) ** n

principal = 1000
rate = 0.1
years = 2

interest = compound_interest(principal, rate, years)

print (interest)

