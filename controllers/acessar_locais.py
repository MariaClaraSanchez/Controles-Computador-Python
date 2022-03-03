import pyautogui
import pyautogui as posicaoMouse

class Locais:
    def __init__(self) -> None:
        pass

    def discord(self) -> None:

        #Mover o mouse para coordenada onde fica o meu discord
        posicaoMouse.moveTo(x=2928, y=1325)

        #click onde está essa coordenada
        posicaoMouse.click(x=2928, y=1325)
       

