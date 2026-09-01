nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)

print("\n===== DADOS DO USUÁRIO =====")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Peso: {peso} kg")
print(f"Altura: {altura} m")

print("\n=====Resultado=====")
print(f"IMC= {round(imc, 2)}")
