import pyautogui
import pyautogui as escolha_opcao

class Opcoes:
    def __init__(self) -> None:
        pass

    def opcao_user(self) -> str:
        opcao = pyautogui.confirm('Clique no botão desejado', buttons = ['Discord', 'Microsoft Teams', "Notepad"])
        return opcao