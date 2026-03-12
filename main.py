import sympy as sp

# 1
m, v = sp.symbols('m v')
E_kin = (1/2) * m * v**2

print("Vzorec pro kinetickou energii:")
sp.pprint(E_kin)
print("\n")


# 2
vysledek_symbolicky = E_kin.subs({m: 1200, v: 25})
vysledek_numericky = vysledek_symbolicky.evalf()

print(f"Kinetická energie pro m=1200kg a v=25m/s:")
print(f"Symbolický/přesný výsledek: {vysledek_symbolicky} J")
print(f"Numerický výsledek (.evalf()): {vysledek_numericky} J")
print("\n")


# 3
A, B = sp.symbols('A B')
vyraz = (A + B)**2 - (A**2 + 2*A*B)

rozvinuty_vyraz = sp.expand(vyraz)
zjednoduseny_vyraz = sp.simplify(vyraz)

print(f"Původní výraz: (A + B)^2 - (A^2 + 2AB)")
print(f"Po expand(): {rozvinuty_vyraz}")
print(f"Po simplify(): {zjednoduseny_vyraz}")
print("\n")


# 4
x = sp.symbols('x')
polynom = x**2 - 2*x + 1

rozklad = sp.factor(polynom)

print(f"Výraz: {polynom}")
print(f"Rozklad (factor): {rozklad}")
# 5
# 6
# 7
