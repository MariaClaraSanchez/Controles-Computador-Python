from turtle import pos
import pyautogui
import pyautogui as posicaoMouse

class Locais:
    def __init__(self,opcao_escolhida:str) -> None:
        self.pesquisa = posicaoMouse.moveTo(x=327, y=1052)
        self.click_pesquisa = posicaoMouse.click(x=327, y=1052)  
        self.time = posicaoMouse.sleep(3)
        self.texto_pesquisa = posicaoMouse.typewrite(opcao_escolhida)
        self.enter = posicaoMouse.press('enter')

    def escolha(self) -> None:
        self.pesquisa 
        self.click_pesquisa
        self.time
        self.texto_pesquisa
        self.enter

