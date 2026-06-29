'''Atividade 10: Análise de Dados de Telemetria (Aritmética + Comparação +
Repetição)
Cenário: Em arquiteturas de Internet das Coisas (IoT), sistemas de monitoramento realizam a
leitura constante de sensores industriais. Escreva um script que processe um lote fixo de dados
de temperatura de uma sala de servidores.
● O programa deve perguntar inicialmente ao usuário quantas leituras de temperatura
ele deseja registrar neste lote de análise.
● Utilizando um laço de repetição condicionado a essa quantidade, realize a leitura
sequencial das temperaturas (valores float).
● Ao final, o sistema deve computar e exibir: a temperatura média do período, a maior
temperatura registrada no lote e a quantidade exata de vezes em que os limites
críticos de 28°C foram excedidos.'''

quantidadeLeituras = int(input("Quantas leituras deseja registrar?"))

contador = 0
maior = 0
conteCritica = 0
totalTemperatura = 0
while contador <quantidadeLeituras:
    temperatura = float(input("Digite a temperatura"))
    totalTemperatura = totalTemperatura + temperatura
    if temperatura > maior:
        maior = temperatura
    if temperatura > 28:
        conteCritica = conteCritica +1
    contador = contador+1
temperaturaMedia = totalTemperatura / contador

print(f"Temperatura media foi: {temperaturaMedia}")
print(f"A maior temparatura registrada foi: {maior}")
print(f"Quantidade exata de vezes em que os limites críticos de 28°C foram excedidos: {conteCritica}")



