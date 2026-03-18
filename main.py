import sympy as sp

def solve_tasks():
    print("1: Kinetická energie")
    m, v = sp.symbols('m v')
    Ek = (1/2) * m * v**2
    sp.pprint(Ek)

    print("2: Dosazování")
    hodnoty = {m: 1200, v: 25}
    vysledek_2 = Ek.subs(hodnoty)
    print(f"Číselná hodnota: {vysledek_2} J")
    print(f"Numerický výsledek: {vysledek_2.evalf()} J")

    print("3: Zjednodušování")
    A, B = sp.symbols('A B')
    vyraz_3 = (A + B)**2 - (A**2 + 2*A*B)
    print(f"Rozbaleno (expand): {sp.expand(vyraz_3)}")
    print(f"Zjednodušeno (simplify): {sp.simplify(vyraz_3)}")
    # Odpověď: Zůstane B**2.

    print("4: Rozklad výrazu")
    x = sp.symbols('x')
    vyraz_4 = x**2 - 25
    rozklad = sp.factor(vyraz_4)
    print(f"Rozklad: {rozklad}")
    # Odpověď: Připomíná vzorec a^2 - b^2 = (a-b)(a+b).

    print("5: Řešení rovnice")
    s, t = sp.symbols('s t')
    rovnice_5 = sp.Eq(s, v * t)
    t_vyjreno = sp.solve(rovnice_5, t)[0]
    print(f"Vzorec pro t: {t_vyjreno}")
    cas_vysledek = t_vyjreno.subs({s: 150, v: 75})
    print(f"Čas pro 150km při 75km/h: {cas_vysledek} h")

    print("6: Kvadratická rovnice")
    h = sp.symbols('h')
    trajektorie = -5*t**2 + 20*t
    casy = sp.solve(sp.Eq(trajektorie, 0), t)
    print(f"Časy, kdy je výška 0: {casy}")
    # Odpověď: t=0 je start (odkop), t=4 je dopad na zem.

    print("7: Soustava rovnic")
    sesit, tuzka = sp.symbols('s t')
    r1 = sp.Eq(3*sesit + 2*tuzka, 44)
    r2 = sp.Eq(2*sesit + 5*tuzka, 46)
    reseni_7 = sp.solve((r1, r2), (sesit, tuzka))
    print(f"Cena sešitu: {reseni_7[sesit]} Kč, cena tužky: {reseni_7[tuzka]} Kč")

    print("8: Ohmův zákon")
    U, R, I = sp.symbols('U R I')
    ohm = sp.Eq(U, R * I)
    R_vyr = sp.solve(ohm, R)[0]
    I_vyr = sp.solve(ohm, I)[0]
    print(f"R = {R_vyr}, I = {I_vyr}")

    print("9: Hustota")
    rho, V = sp.symbols('rho V')
    rovnice_9 = sp.Eq(rho, m / V)
    m_vyjreno = sp.solve(rovnice_9, m)[0]
    m_vysledek = m_vyjreno.subs({rho: 7800, V: 0.002})
    print(f"Hmotnost: {m_vysledek.evalf()} kg")
    # Odpověď: Hustota 7800 kg/m3 odpovídá oceli nebo železu.

    print("10: Rozvoj výrazu")
    p, q = sp.symbols('p q')
    vyraz_10 = (p + q)**3
    rozvoj = sp.expand(vyraz_10)
    print(f"Rozvoj: {rozvoj}")
    # Odpověď: Výsledný výraz má 4 členy.

    print("11: Ověření rovnosti")
    a, b = sp.symbols('a b')
    vyr_a = (a + b)**2
    vyr_b = a**2 + 2*a*b + b**2
    test = sp.simplify(vyr_a - vyr_b)
    print(f"Rozdíl výrazů (pokud 0, jsou stejné): {test}")
    # Odpověď: Rovnost ověříme odečtením a funkcí simplify().

    print("12: Průměrná rychlost")
    rovnice_12 = sp.Eq(v, s / t)
    s_vyr = sp.solve(rovnice_12, s)[0]
    t_vyr = sp.solve(rovnice_12, t)[0]
    print(f"s = {s_vyr}, t = {t_vyr}")
    # Odpověď: Závislá proměnná je v (rychlost), protože je vyjádřena pomocí s a t.

    print("13: Kontrola řešení")
    rovnice_13 = sp.Eq(3*x + 7, 25)
    x_res = sp.solve(rovnice_13, x)[0]
    kontrola = rovnice_13.subs(x, x_res)
    print(f"Řešení x = {x_res}, Kontrola (True/False): {kontrola}")
    # Odpověď: Kontrola vyloučí chyby při výpočtu nebo numerickou nepřesnost.

    print("14: Model ceny")
    C, d = sp.symbols('C d')
    rovnice_14 = sp.Eq(C, p * q + d)
    q_vyr = sp.solve(rovnice_14, q)[0]
    pocet_kusu = q_vyr.subs({C: 550, p: 45, d: 100})
    print(f"Počet kusů q = {pocet_kusu}")

if __name__ == "__main__":
    solve_tasks()