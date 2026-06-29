'''Atividade 6: Validação de Acesso (Estrutura if-else Básica)
Cenário: Você está desenvolvendo o módulo de segurança de um sistema de controle de
ponto corporativo. O sistema deve ler a idade de um funcionário e o seu tempo de empresa
(em anos).
Regra de Negócio: Um funcionário tem direito ao "Acesso Premium" ao clube de benefícios se
ele tiver pelo menos 18 anos de idade E mais de 2 anos de empresa. Caso contrário, ele
terá o "Acesso Standard". Escreva o programa correspondente.
Dica: Utilize o operador lógico and para validar ambas as condições simultaneamente.'''

idade = int(input("Digite a idade do funcionario: "))
anosNaEmpresa = int(input("Digite a quantidade de anos desse funcionario na empresa: "))

if idade >= 18 and anosNaEmpresa >2:
    print("Acesso Premium")
else:
    print("Acesso Standard")