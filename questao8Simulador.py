'''Atividade 8: Simulador de Caixa Eletrônico (Aritmética + Repetição while)
Cenário: Desenvolva a lógica de entrega de cédulas de um terminal de autoatendimento
bancário.
● O programa deve solicitar ao usuário um valor de saque. Por limitações técnicas do
terminal, o sistema só aceita valores que sejam múltiplos de R$ 10,00.
● Utilize um laço while que continue solicitando o valor do saque caso o usuário digite uma
entrada inválida (não múltipla de 10), menor ou igual a zero.
● Assim que um valor válido for fornecido, o programa deve calcular e exibir a menor
quantidade possível de cédulas para aquele valor, priorizando as notas maiores. O
banco trabalha exclusivamente com cédulas de R$ 50, R$ 20 e R$ 10'''


while True:
    print("-"*100)
    valorSaque = int(input("Digite o valor a ser sacado"))
    print("-"*100)


    if valorSaque %10 != 0 or valorSaque<=0:
        print("Entrada inválida")
    else:
        notas50 = valorSaque //50
        valorSaque %=50

        notas20 = valorSaque//20
        valorSaque %=20

        notas10 = valorSaque //10

        print("\nCédulas a sacar:")
        print(f"Quantidade de notas de 50: {notas50}")
        print(f"Quantidade de notas de 20: {notas20}")
        print(f"Quantidade de notas de 10: {notas10}")

