'''Atividade 3 - Análise de Código Python
Enunciado: Observe atentamente o código em Python abaixo:'''

nome = str(input("Digite seu nome completo: "))
idade = int(input("Digite sua idade: "))
sexo = str(input("Digite seu sexo: f para Feminino e m para Masculino"))
print(nome)
if idade < 18:
    print("Você é menor de idade")
else:
    print("Você é maior de idade")
if sexo == "f":
    print("Seu sexo é Feminino")
else:
    print("Seu sexo é Masculino")

'''
Responda às perguntas de acordo com o código anterior:
a) Quais são as variáveis presentes no script e qual é o tipo de dado de cada uma delas?
- Resposta:
    nome, do tipo string (texto). idade do tipo inteiro, sexo. tipo string (texto).
b) Considerando que o usuário do sistema seja você, descreva exatamente qual
resultado será impresso na tela após a execução.
- Resposta:
    Fabio Ferreira
    Você é maior de idade
    Seu sexo é Masculino
'''