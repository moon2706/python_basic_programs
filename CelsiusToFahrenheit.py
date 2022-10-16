def convert(n):
    f=float(n)
    c=(f-32)*5/9  # F=(9/5)*C+32
    return c

print(convert(78))