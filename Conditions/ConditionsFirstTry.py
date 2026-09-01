n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))

media = (n1 + n2) / 2

print("\n===== RESULTADO ======")
print(f"Nota 1: {n1} e Nota 2: {n2}")
print(f"Média: {media:.1f}")

if media >= 6:
  print("Situaçâo: Aprovado!")
else:
    print("Situação: Reprovado!")
