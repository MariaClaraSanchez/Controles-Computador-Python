from controllers.tela_opcoes import Opcoes
from controllers.acessar_locais import Locais

def start():
    
    opcao = Opcoes()
    op = opcao.opcao_user()

    if(op == 'Discord'):
        local = Locais()
        local.discord()
    #print(opcao.opcao_user())
    


if __name__ == '__main__':
    start()

