valor_hora = float(input("Digite o valor da hora: "))
hora_trabalhada = float(input("Digite a quantidade de horas trabalhadas: "))

salario = valor_hora*hora_trabalhada

if salario <= 2112:
    imposto = 0
elif salario <= 2826.65:
    imposto = salario*0.075
elif salario <= 3757.05:
    imposto = salario*0.27
else:
    imposto = salario*0.27

print("salario: ", salario)
print("Imposto a pagar: ",imposto)
