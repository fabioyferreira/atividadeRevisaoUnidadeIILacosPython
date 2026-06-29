'''Atividade 7: Menu de Sistema de Helpdesk (Estrutura match-case)
Cenário: Você está prototipando a interface de texto de um sistema de triagem automática de
chamados de TI (Helpdesk).
Construa um programa que exiba o seguinte menu:
1. Problemas com Internet / Rede
2. Mau funcionamento de Hardware (Mouse, Teclado, Monitor)
3. Instalação ou Erro de Software
4. Troca de Senha / Acesso corporativo
O sistema deve ler a opção digitada (um inteiro) e usar a estrutura de correspondência de
padrões do Python (match-case) para direcionar o usuário exibindo uma mensagem
personalizada para cada caso. Certifique-se de tratar opções inválidas utilizando o caso padrão
(case _:).'''
print("-"*100)
print("Sistema de triagem automática de chamados de TI (Helpdesk)")
print("-"*100)
print("1. Problemas com Internet / Rede")
print("2. Mau funcionamento de Hardware (Mouse, Teclado, Monitor)")
print("3. Instalação ou Erro de Software")
print("4. Troca de Senha / Acesso corporativo \n")
opcao = int(input("Escolha uma opção 1, 2, 3 ou 4: "))

match opcao:
    case 1:
        print("Soluções: Verifique os cabos, reinicie o computador/roteador")
    case 2:
        print("Soluções: desconecte os cabos e conecte-os novamente, reinicie o computador")
    case 3:
        print("Verifique se tem provilégio de administrador,se tem espaço de disco livre")
    case 4:
        print("Verificar se a tecla maiúsculo/menusculo está ligado, troque o teclado")
    case _:
        print("Aguarde para falar com um tecnico TI")