print('CALCULADORA DE IMC')
print('.'*20)
idade = int(input('Coloque aqui a sua idade:'))
print('.'*20)
peso = float(input('Coloque aqui o seu peso:'))
print('.'*20)
altura = float(input('Coloque aqui a sua altura:'))
print('.'*20)
print(peso / (altura ** 2))
print('.'*20)


imc = peso / (altura ** 2)

if imc > 0 and imc < 18.5:
  print('BAIXO PESO!')

if imc > 18.5 and imc < 24.99:
  print('PESO NORMAL!')

if imc > 24.99 and imc < 29.99:
  print('SOBREPESO!')

if imc > 30:
  print('OBESIDADE!')



