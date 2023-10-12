import os
def limpaTela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def existCPF(cpf,cadastrados):
    for elem in cadastrados:
        if elem == cpf:

            return True
    return False

def cadastraJOGs(jogsCad):
    jogsCadastrados ={}
    n = int(input("Digite quantos jogadores irá inserir: "))
    for i in range(n):
        nome = input("Digite o nome:")
        cpf = input("Digite o cpf:")
        while(existCPF(cpf,jogsCad)):
            print(f'CPF JA CADASTRADO')
            cpf = input("Digite o cpf:")
        jogsCad[cpf]= nome
        print(f'Jogador inserido com sucesso!')
        
def imprimeJogs(jogsCad):
    for cpf in jogsCad:
        print(jogsCad[cpf], cpf)

def cadastraApostas(numerosAposta,cpfs,dic):
    dic[numerosAposta] = cpfs

def imprimeApostas(apostas):
    for elem in apostas:
        print(elem , apostas[elem])



    



    
def main():
    menu = '''
SEJA BEM VINDO AO BOLÃO
    MENU DO BOLÃO
    ESCOLHA UMA OPÇÃO(NÚMERO):

    1) CADASTRAR JOGADOR
    2) VISUALIZAR JOGADORES CADASTRADOS
    3) INSERIR NOVA APOSTA
    4) VIZUALIZAR APOSTAS CADASTRADAS
    5) INSERIR RESULTADO E LISTAR APOSTAS VENCEDORAS
    6) SAIR

'''

    print(menu) 
    jogsCad = {}
    apostas = {}
    opcao = int(input())
    while opcao!=6:
        limpaTela()
        if opcao == 1:
            print(f'SESSÃO DE CADASTRO: JOGADOR')
           
            cadastraJOGs(jogsCad)
            print(jogsCad)

        elif opcao == 2:
            
            print(f'JOGADORES CADASTRADOS:')
            imprimeJogs(jogsCad)
    
        elif opcao == 3:
            ljogs= []
            print(f'SESSÃO DE CADASTRO: APOSTA')
            qntdJogs = int(input("Digite quantos jogadores apostaram: "))
            for i in range(qntdJogs):
                jogadores = input("Digite o CPF dos jogadores: ")
                ljogs.append(jogadores)
            numeros = str(input("Digite os numeros escolhidos:  "))

            
            cadastraApostas(numeros,ljogs,apostas)
            print("Jogadores Cadastrados com sucesso")

            
        elif opcao == 4:
            print(f'VISUALIZAR APOSTAS CADASTRADAS')
            imprimeApostas(apostas)
        elif opcao == 5:
            print(f'RESULTADO')
            n = str(input())
            acertos = 0
            if n in apostas:
                print("VENCEDORES:",apostas[n])
            else:
                for elem in apostas : 
                    a = apostas[elem]
                    for i in range (len(a)):
                        if a[i] == n[i]:
                            acertos+=1
                if acertos == 6:
                    print("VENCEDORES:",apostas[n])    

            
        elif opcao != 6 :
            print(f'NÚMERO INVÁLIDO, TENTE NOVAMENTE')
        opcao = int(input())  
    print(f'Sessão finalizada.')



    return 0
if __name__ == "__main__":
    main()
    