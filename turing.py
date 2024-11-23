def resumo():
    mensagem = "Grace Hopper foi uma cientista da computação e contra-almirante da Marinha dos Estados Unidos. "
                "Ela é conhecida por seu trabalho pioneiro no desenvolvimento da linguagem de programação COBOL e pela invenção do compilador, "
                "que traduz código de alto nível para linguagem de máquina. Hopper foi uma das primeiras a popularizar o conceito de 'debugging'.")
   return mensagem


def doutorado():
    mensagem = "Grace Hopper obteve seu doutorado em Matemática na Universidade de Yale em 1934, sendo uma das primeiras mulheres a conquistar esse título na área."
    return mensagem


def contribuicoes():
    mensagem = ("Grace Hopper é famosa por seu trabalho no desenvolvimento da linguagem de programação COBOL, "
                "uma das primeiras linguagens de programação de alto nível. Ela também inventou o primeiro compilador, "
                "facilitando a tradução de código fonte para linguagem de máquina.")
    return mensagem


def artigos():
    mensagem = "Grace Hopper escreveu diversos artigos e relatórios sobre computação, incluindo um famoso sobre o conceito de 'bugs' em programas de computador, que se originou de um incidente em 1947 quando ela encontrou uma mariposa presa em um computador."
    return mensagem


def citacoes():
    mensagem = "Grace Hopper é conhecida por várias citações inspiradoras, como: A melhor maneira de prever o futuro é inventá-lo. Além disso, ela popularizou o conceito de debugging ao documentar a remoção de um bug real de um computador."
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Grace Hopper.\n")

continuar = True
while continuar == True:

    opcao = int(
        input(
"""
\nDigite o número correspondente ao menu que você deseja acessar:
1 - Resumo
2 - Doutorado
3 - Contribuições
4 - Principais Artigos
5 - Citações
6 - Sair\n
"""
        )
    )

    if opcao == 1:
        print("1 - Resumo")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Doutorado")
        mensagem = doutorado()

    elif opcao == 3:
        print("3 - Contribuições")
        mensagem = contribuicoes()

    elif opcao == 4:
        print("4 - Principais Artigos")
        mensagem = artigos()

    elif opcao == 5:
        print("5 - Citações")
        mensagem = citacoes()

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)


