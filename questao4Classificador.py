'''
Atividade 4: Classificador de Clientes (Estrutura elif Encadeada)
Cenário: Um e-commerce parceiro quer categorizar seus clientes com base no valor total de
compras acumulado no último ano para oferecer cupons de desconto proporcionais.
Implemente um programa que leia o valor gasto pelo cliente (um número real) e exiba sua
categoria seguindo as regras abaixo:
● Gasto menor que R$ 1.000,00: Categoria Bronze (Sem desconto).
● Gasto de R$ 1.000,00 até R$ 2.999,99: Categoria Prata (5% de desconto).
● Gasto de R$ 3.000,00 até R$ 4.999,99: Categoria Ouro (10% de desconto).
● Gasto de R$ 5.000,00 ou mais: Categoria Platinum (15% de desconto).
'''

valorGasto = float(input("Digite o valor gasto"))

if valorGasto < 1000:
    print("Sem desconto")
elif valorGasto >=1000 and valorGasto <=2999.99:
    print("Categoria prata, 5% de desconto")
elif valorGasto >= 3000 and valorGasto <=4999.99:
    print ("Categoria Ouro, 10% de desconto")
elif valorGasto >=5000:
    print("Categoria platinum, 15% de desconto")