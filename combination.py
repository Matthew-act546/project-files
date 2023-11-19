n = int(input("Enter the nth term: "))
r = int(input("Enter the common ratio: "))

nr = (n - r)

nth = 1
for i in range(n):
    nth *= n
print(nth)
nrr = 1
for i in range(nr):
    nrr *= nr
print(nrr)
rth = 1
for i in range(r):
    rth *= r
print(rth)

formula = nth / (nrr * rth)

print(formula)
