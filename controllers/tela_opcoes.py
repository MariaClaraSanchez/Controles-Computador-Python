import pyautogui
import pyautogui as escolha_opcao

class Tela:
    def __init__(self) -> None:
        pass
    def opcao_user(self) -> str:
        """Responsável por incluir o nome dos aplicativos a serem abertos,
        e também por criar uma janela na tela, com botões para que o usuário 
        consiga clicar.

        Returns:
            opcao: retorna uma string com a opção escolhida pelo usuário
        """
        opcao = pyautogui.confirm('Clique no aplicativo que deseja abrir', 
                    buttons = ['Discord', 'Microsoft Teams','Outlook','Visual Studio Code'
                    'Google Chrome','PowerPoint','Excel','Word',
                    'Sophos Connect','AnyDesk','UiPath Studio'])
        return opcao