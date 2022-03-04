import pyautogui
import pyautogui as posicaoMouse

class Locais:
    def __init__(self,opcao_escolhida:str) -> None:
        """_summary_
            Responsável por direcionar para o aplicativo escolhido 
        Args:
            opcao_escolhida (str): recebe o aplicativo que o usuário recebeu
        """
        self.pesquisa = posicaoMouse.moveTo(x=327, y=1052)
        self.click_pesquisa = posicaoMouse.click(x=327, y=1052)  
        self.time = posicaoMouse.sleep(3)
        self.texto_pesquisa = posicaoMouse.typewrite(opcao_escolhida)
        self.enter = posicaoMouse.press('enter')

    def escolha(self) -> None:
        """
        Chama as varivaeis responsáveis por posicionar o mouse na barra de pesquisa;
        Dar um click na barra de pesquisa;
        Dar um tempo de espera para dar tempo de inserir o texto completamente na barra de pesquisa;
        Insere o texto;
        Após inserir o texto é dado um enter e aplicação abre.
        """
        self.pesquisa 
        self.click_pesquisa
        self.time
        self.texto_pesquisa
        self.enter

