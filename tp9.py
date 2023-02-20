tips = input("introduzca nombres de paises separados por una coma:\n ")

pais = [paises for  paises in tips.split(" , ")]

print(list(set(sorted(pais))))