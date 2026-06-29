'''Atividade 5 - Estrutura Condicional e Regra de Negócio
Enunciado: Escreva um programa em Python que resolva o seguinte problema: Um
Supermercado resolveu fazer uma promoção. Determinadas maçãs custam R$ 0,30 cada se
forem compradas menos do que uma dúzia, e R$ 0,25 se forem compradas pelo menos doze.
O programa deverá ler o número de maçãs compradas, calcular e escrever o valor total da
compra.'''

numeroMacaComprada = float(input("Digite o numero de maças compradas: "))

if numeroMacaComprada <12:
    valorTotalCompra = numeroMacaComprada*0.3
elif numeroMacaComprada >=12:
    valorTotalCompra = numeroMacaComprada*0.25

print(f"O valor total da compra foi {valorTotalCompra}")