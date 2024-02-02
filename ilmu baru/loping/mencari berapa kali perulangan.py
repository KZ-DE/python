def nb_year(p0, percent, aug, p, years=0):
    if p0 < p:
        return nb_year(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1)
    return years


print(nb_year(1000, 2, 50, 1200))


# contoh simpel
def x(a, b, n=0):
    if a < b:
        return x(a+1, b, n+1)
    return n


print(x(1, 5))

# jadi fungsi nya akan di rekursif 4 kali agar nilai a sama dengan nilai b
# sedangkan setian rekursif nilai a di tambah 1
