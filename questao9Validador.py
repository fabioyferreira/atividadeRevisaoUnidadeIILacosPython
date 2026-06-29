'''Atividade 9: Validador de Acesso de Segurança (Comparação + Repetição for)
Cenário: Proteger o acesso contra ataques de força bruta é um requisito fundamental no
desenvolvimento de software. Você deve criar o script de validação de login de um servidor
seguro.
● A senha correta já está definida internamente no sistema como uma constante (ex:
"Admin@2026").
● O usuário possui no máximo 3 tentativas consecutivas para acertar a credencial.
● Utilize um laço para combinar com a função range() para gerenciar o número de
tentativas. Se o usuário acertar, exiba o acesso concedido e interrompa o laço (break).
Caso esgote as chances, informe o bloqueio temporário da conta.'''



contador = 0
for tentativa in range(3): 
    nomeUsuario = input("Digite o nome do usuario")
    senha = str (input("Digite a senha:"))
    if senha == "Admin@2026":
        print("Bem vindo")  
        break 
    else:
        if senha != "Admin@2026":
            print("Senha inválida")
    contador = contador+1
    if contador == 3:
        print("Você excedeu o numero de tentativas, conta temporariamente bloqueada")    
