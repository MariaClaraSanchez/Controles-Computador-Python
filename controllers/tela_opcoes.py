import pyautogui
import pyautogui as escolha_opcao

class Tela:
    def __init__(self) -> None:
        pass

    def opcao_user(self) -> str:
        opcao = pyautogui.confirm('Clique no botão desejado', 
                    buttons = ['Discord', 'Microsoft Teams','Outlook','Visual Studio Code'
                    'Google Chrome','PowerPoint','Excel','Word',
                    'Sophos Connect','AnyDesk','UiPath Studio'])
        return opcao