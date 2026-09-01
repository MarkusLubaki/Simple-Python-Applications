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

print("\n=====Situação=====")

if imc < 18.5:
      print("Você está abaixo do peso")
elif imc < 25:
      print("Você está com peso normal")
elif imc < 30:
      print("Você está acima do peso")
elif imc < 35:
      print("Você está obeso 1")
elif imc < 40:
      print("Você está obeso 2")
else:
      print("Você está obeso mórbido")
