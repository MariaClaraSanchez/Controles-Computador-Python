from controllers.tela_opcoes import Tela
from controllers.acessar_locais import Locais

def start():
    
    opcao_tela_escolhida = Tela()
    op = opcao_tela_escolhida.opcao_user()

    local_acessado = Locais(op)
    local_acessado.escolha()
    
    #print(opcao.opcao_user())
    


if __name__ == '__main__':
    start()

