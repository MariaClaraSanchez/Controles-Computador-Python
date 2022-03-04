# Abrir Aplicativos área de trabalho

Essa solução foi desenvolvida utilizando puramente a linguagem de programação Python com algumas bibliotecas, o objetivo dessa automação é apenas treinar python, com ela foi possível selecionar alguns aplicativos que tenho no meu computador aí a pessoa só clica no botão e ele abre automaticamente o aplicativo, é algo simples, mas com o intuito de poupar tempo na hora da pesquisa dos aplicativos que mais utilizo no meu dia a dia.
  
# Configuração
## Máquina Virtual
Caso queira executar o projeto separadamente da onde fica seus documentos python é preciso cria uma máquina virtual e para isso precisa da os seguintes passos:
<br>
1º Instalar o env em sua máquina para isso utilize o comando :
```
pip install venv
```
2º Criar sua máquina virtual:
```
python3 -m venv nome_maquina_virtual-env
```
3º Escolha o comando de acordo com seu sistema opercional:
#### Para Windows:
```
nome_maquina_virtual-env\Scripts\activate.bat
```
#### Para Unix ou no MacOS:
```
source nome_maquina_virtual-env/bin/activate
```

## Instalando Dependências
Use o gerenciado de pacote [pip](https://pip.pypa.io/en/stable/) para instalar as dependências.
```bash
pip install -r requirements.txt
```

## Observação:
Usei um arquivo de teste para obter as coordenadas da minha barra de pesquisa do Windows, mas o valor pode variar de computador para computador. 
Para obter essas coordenadas só criar um arquivo e escrever esste código dentro dele:

```py
#Importa a biblioteca do pyautogui
import pyautogui as posicaoMouse

#Tempo de espera para posicionar o mouse,
#quando esse tempo acabar, ele vai imprimir
#a posição onde você posicionou seu mouse
#e o valor pode ser mudado também
posicaoMouse.sleep(7)

#Imprime a posição usando a função position()
print(posicaoMouse.position())
```
Quando você executar esse código acima ele vai aguardar 7 segundos até que você posicione o cursor do mouse onde você deseja obter o valor das coordenadas, com esse valor sendo impressor, só copiar ele e substituir no arquivo 'acessar_locais.py' onde estiver escrito X e Y

# Inicializando

Para executar o robô basta executar o comando :

```
pyhton main.py
```
