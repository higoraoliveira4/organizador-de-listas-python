lista_geral = []
lista_par = []
lista_impar = []

while True:
    num = (int(input("Digite um valor: ")))
    lista_geral.append(num)
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)

    continuar = input("Deseja continuar? [S/N]").upper()
    if continuar == "N":
        break
    if continuar == "S":
        continue

print (f"A lista completa é {lista_geral}")
print (f"A lista de pares é {lista_par}")
print (f"A lista de ímpares é {lista_impar}")