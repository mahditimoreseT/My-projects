def mohasebe_moadel(nomarat):
    return sum(nomarat) / len(nomarat)

tedad_dars = int(input("tedad_dars_ha: "))


nomarat = []
for i in range(tedad_dars):
    nomre = float(input(f" nomrh_dars {i + 1} vardkon: "))
    nomarat.append(nomre)

moadel = mohasebe_moadel(nomarat)


print(f" moadel : {moadel:.2f}")

if moadel >= 17:
    print("good:")
elif moadel >= 10:
    print("ok:")
else:
    print("oh no:")
