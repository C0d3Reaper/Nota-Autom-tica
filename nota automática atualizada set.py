
import sys
import datetime
import pyautogui
import time




pyautogui. alert(text = "ATENÇÃO: o usuário deve fechar todos os aplicativos que ocupam espaço na barra de tarefas, deixando somente os que são fixos da barra.", title = "Bem Vindo ao código de notas automáticas!")

pyautogui.alert(text="DICA: z1 = Corretiva planejada  |  z2 = Corretiva emergêncial  |  z3 = Preventiva  |  zm = Requisição de compras  |  z0 = Nota de ação pm  |  z4 = Segurança do trabalho  |  z5 = Preditiva  |  z6 = Melhoria  |  z7 = Análise de falha  |  z8 = Retrabalho  |  z9 = Inspeção  |  zf = Fabricação de peças  |  zp = Projeto  |", title="Aqui vai uma dica dos tipos de notas do sap!")

def conj_tipologia():
    tipologias = ['Z0', 'Z1', 'Z2', 'Z3', 'Z4', 'Z5', 'Z6', 'Z7', 'Z8', 'Z9', 'ZF', 'ZM', 'ZP', 'Zf', 'Zm', 'Zp', 'z0', 'z1', 'z2', 'z3', 'z4', 'z5', 'z6', 'z7', 'z8', 'z9', 'zf', 'zm', 'zp']
    while True:
        tipologia = pyautogui.prompt(text='Qual é o tipo de nota a seguir? (z1,z2,z3...) :', title='Tipologia', default='')
        if tipologia in tipologias:
            return tipologia
        elif tipologia is None or tipologia.strip() == "":
            raise ValueError("Nenhum valor foi fornecido. O programa será encerrado.")
        else:
            pyautogui.alert("Tipologia inválida!")


def conj_titulo():
    titulo = pyautogui.prompt(text='Digite o título da nota:', title='Título da nota', default='')
    if titulo is None or titulo.strip() == "":
        raise ValueError("Nenhum valor foi fornecido. O programa será encerrado.")
    return titulo


def conj_descricao():
    descricao = pyautogui.prompt(text='Descreva a avaria da máquina:', title='Descrição', default='')
    if descricao is None or descricao.strip() == "":
        raise ValueError("Nenhum valor foi fornecido. O programa será encerrado.")
    return descricao


def conj_setor():
    setores = ["embalagem", 'EMBALAGEM', 'EMBALAGENS', 'embalagens', "lã de aço", "la de aco", "lã de aco", "la de aço", 'abrasivos', 'ABRASIVOS', 'lÃ DE AÇO', 'LA DE ACO', 'LA DE AÇO', 'LÃ DE ACO', 'la', 'LA', 'lã', 'LÃ'"química", 'quimica', 'Quimica', 'Química', 'envase', 'Envase', 'infra', 'infraestrutura', 'Infra', 'Infraestrutura']
    while True:
        setor = pyautogui.prompt(text='Qual é o setor responsável? (Embalagem, lã de aço, ...)', title='Setor', default='')
        if setor in setores:
            return setor
        elif setor is None or setor.strip() == "":
            raise ValueError("Nenhum valor foi fornecido. O programa será encerrado.")
        else:
            pyautogui.alert("Setor inválido!")


# def conj_equipamento():
#     while True:
#         equipamento = pyautogui.prompt(text='Qual é o equipamento da avaria?', title='Código de identificação da máquina', default='')
#         if len(equipamento) == 7:
#             return equipamento
#         elif equipamento is None or equipamento.strip() == "":
#             raise ValueError("Nenhum valor foi fornecido. O programa será encerrado.")
#         else:
#             pyautogui.alert("Equipamento inválido!")

def conj_equipamento():
    while True:
        equipamento = pyautogui.prompt(text='Qual é o equipamento da avaria? (spo1011, emf1013, ...)', title='Código de identificação da máquina', default='')
        if len(equipamento)  <7:
            pyautogui.alert("Equipamento inválido!")
        
        elif equipamento is None or equipamento.strip() == "":
            raise ValueError("Nenhum valor foi fornecido. O programa será encerrado.")
        else:
            return equipamento


def conj_ctb():
    ctbs = ["mecanica", "mecânica", "Mecanica", "Mecânica", "mecanico", "mecânico", "Mecanico", "Mecânico", "eletrica", "elétrica", 'ELETRICA', 'ELÉTRICA', "eletrico", "elétrico", 'ELETRICO', 'ELÉTRICO']
    while True:
        centro_de_trabalho = pyautogui.prompt(text='A máquina apresenta um defeito mecânico, ou elétrico?', title='Defeito mecânico ou elétrico', default='')
        if centro_de_trabalho in ctbs:
            return centro_de_trabalho
        elif centro_de_trabalho is None or centro_de_trabalho.strip() == "":
            raise ValueError("Nenhum valor foi fornecido. O programa será encerrado.")
        else:
            pyautogui.alert("Centro de trabalho inválido!")


def conj_notficador():
    while True:
        notificador = pyautogui.prompt(text='Qual é o seu nome?', title='Nome do notificador', default='')
        if notificador is None or notificador.strip() == "":
            raise ValueError("Nenhum valor foi fornecido. O programa será encerrado.")
        else:
            return notificador


def conj_parada():
    paradas = ["sim", 'SIM', 'Sim', "não", "nao", 'NAO', 'Não', 'Nao']
    while True:
        parada = pyautogui.prompt(text='Houve parada na máquina?', title='Parada', default='')
        if parada in paradas:
            return parada
        elif parada is None or parada.strip() == "":
            raise ValueError("Nenhum valor foi fornecido. O programa será encerrado.")
        else:
            pyautogui.alert("Parada inválida!")


def conj_prioridade():
    prioridades = ["rotina", "Rotina", "emergencia", "emergência", "emergencial", "Emergêncial", "Emergência", "Emergencia", "urgencia", "urgência", "urgente", 'Urgente', "Urgencia", "Urgência", "programavel", "programável"]
    while True:
        prioridade = pyautogui.prompt(text='Digite a prioridade da nota: (emergencia, rotina, urgencia ou programável)', title='Prioridade da nota', default='')
        if prioridade in prioridades:
            return prioridade
        elif prioridade is None or prioridade.strip() == "":
            raise ValueError("Nenhum valor foi fornecido. O programa será encerrado.")
        else:
            pyautogui.alert("Prioridade inválida!")



# Capturando as informações
tipologia1 = conj_tipologia()
titulo1 = conj_titulo()
descricao1 = conj_descricao()
equipamento1 = conj_equipamento()
setor1 = conj_setor()
prioridade1 = conj_prioridade()
parada1 = conj_parada()
centro_de_trabalho1 = conj_ctb()
notificador1 = conj_notficador()

def conj_press():
    # Definir press
    if prioridade1 in ["rotina", "Rotina"]:
        press = 1 
    elif prioridade1 in ["programavel", "programável"]:
        press = 2
    elif prioridade1 in ["urgencia", "urgência", "urgente", 'Urgente', "Urgencia", "Urgência"]:
        press = 3 
    elif prioridade1 in ["emergencia", "emergência", "emergencial", "Emergêncial", "Emergência", "Emergencia"]:
        press = 4
    return press
press = conj_press()

def conj_espaço():
    # Definir espaço
    if parada1 in ["sim", 'SIM', 'Sim']:
        espaco = 1
    elif parada1 in ["não", "nao", 'NAO', 'Não', 'Nao']:
        espaco = 2
    else:
        raise ValueError("Parada inválida!")
    return espaco
espaco = conj_espaço()

def conj_ctb():
        
    # Definir ctb
    if setor1 in ["embalagem", 'EMBALAGEM', 'EMBALAGENS', 'embalagens'] and centro_de_trabalho1 in ["mecanico", "mecânico", "Mecanico", "Mecânico"]:
        ctb = "embmeca"
    elif setor1 in ["embalagem", 'EMBALAGEM', 'EMBALAGENS', 'embalagens'] and centro_de_trabalho1 in ["eletrico", "elétrico", 'ELETRICO', 'ELÉTRICO']:
        ctb = "embelet"
    elif setor1 in ["lã de aço", "la de aco", "lã de aco", "la de aço", 'abrasivos', 'ABRASIVOS', 'lÃ DE AÇO', 'LA DE ACO', 'LA DE AÇO', 'LÃ DE ACO', 'la', 'LA', 'lã', 'LÃ'] and centro_de_trabalho1 in ["mecanico", "mecânico", "Mecanico", "Mecânico"]:
        ctb = "lacmeca"
    elif setor1 in ["lã de aço", "la de aco", "lã de aco", "la de aço", 'abrasivos', 'ABRASIVOS', 'lÃ DE AÇO', 'LA DE ACO', 'LA DE AÇO', 'LÃ DE ACO', 'la', 'LA', 'lã', 'LÃ'] and centro_de_trabalho1 in ["eletrico", "elétrico"]:
        ctb = "lacelet"
    elif setor1 in ["química", 'quimica', 'Quimica', 'Química', 'envase', 'Envase'] and centro_de_trabalho1 in ["mecanico", "mecânico", "Mecanico", "Mecânico"]:
        ctb = "quimeca"
    elif setor1 in ["química", 'quimica', 'Quimica', 'Química', 'envase', 'Envase'] and centro_de_trabalho1 in ["eletrico", "elétrico", 'ELETRICO', 'ELÉTRICO']:
        ctb = "quielet"
    elif setor1 in ['infra', 'infraestrutura', 'Infra', 'Infraestrutura'] and centro_de_trabalho1 in ["mecanico", "mecânico", "Mecanico", "Mecânico"]:
        ctb = "inframec"
    elif setor1 in  ['infra', 'infraestrutura', 'Infra', 'Infraestrutura'] and centro_de_trabalho1 in ["eletrico", "elétrico", 'ELETRICO', 'ELÉTRICO']:
        ctb = "infraelet"
    else:
        raise ValueError("Setor e centro de trabalho não correspondem.")
    return ctb 
ctb = conj_ctb()


# Coordenadas
abre_barra_comandos = (76, 73) #
barra_comandos = (153, 75) #
clicasap = (951, 1045) #
janelasap = (1052, 915) #
barrascrolldown = (1887, 389) #
barraprioridade = (858, 757) #
barrascrollup = (1887, 389) #
barraimprimir = (40, 319) #
logoff = (549, 527) #


pyautogui.PAUSE = 0.6

def criar_nota():


    def sap_aberto():

        pyautogui.click(clicasap)
        time.sleep(0.5)
        pyautogui.click(janelasap)
        time.sleep(1)

    # def sap():

    #     lista_sap = ['Aberto', 'aberto', 'fechado', 'Fechado']
    #     sap1 = pyautogui.prompt (text = "o SAP está aberto ou fechado no momento?")
    #     if sap1 in lista_sap:
    #       return sap1
    #     elif sap1  is None or tipologia.strip() == "":
    #       raise ValueError("Nenhum valor foi fornecido. O programa será encerrado.")
    #     else:
    #         pyautogui.alert("Resposta inválida")

    #     if sap1 in ['Aberto', 'aberto',]:
    #         pyautogui.click(clicasap)
    #         time.sleep(0.5)
    #         pyautogui.click(janelasap)
    #         time.sleep(1)

    #     elif sap1 in ['fechado', 'Fechado']:
    #         usuário = pyautogui.prompt (text = "Digite seu usuário :", title = "Usuário")
    #         senha = pyautogui.prompt (text = "Digite sua senha :", title = "Senha")
    #         pyautogui.press ("win")
    #         pyautogui.write ("sap")
    #         pyautogui.press ("enter")
    #         time.sleep (1)
    #         pyautogui.press ("enter")
    #         pyautogui.write (usuário)
    #         pyautogui.press("tab")
    #         pyautogui.write(senha)
    #         pyautogui.press ("enter")


    sap_aberto()

    def iw21():
        pyautogui.hotkey('shift', 'f3')
        time.sleep(1)
        pyautogui.click(logoff)
        time.sleep(1)
        pyautogui.click(abre_barra_comandos)
        pyautogui.click(barra_comandos)
        pyautogui.write("iw21")
        pyautogui.press("enter")
    
    iw21()

    def tipologia():
        pyautogui.press("right", presses=2)
        pyautogui.press("backspace", presses=2)
        pyautogui.write (tipologia1)
        pyautogui.press ("enter")
        time.sleep (0.5)
    
    tipologia()
    pyautogui.write (titulo1)
    pyautogui.press ("enter")

    def equipamento():
        #pyautogui.click (x=259, y=312)
        pyautogui.press ('tab', presses=7)
        pyautogui.write (equipamento1)
        pyautogui.press ("enter")
    
    equipamento()

    def descricao():
        #descrição

        #pyautogui.click (x=203, y=468)   
        pyautogui.press ('tab', presses=13)
        pyautogui.write(descricao1)
        pyautogui.hotkey ('ctrl', 'tab')
    
    descricao()

    def descer_tela():
        #descer a tela

        pyautogui.click (barrascrolldown)
        time.sleep (0.5) 
        pyautogui.scroll (-500)
    
    descer_tela()

    def prioridade():
        # prioridade
        pyautogui.click (barraprioridade)
        time.sleep(0.5)
        pyautogui.click (barraprioridade)
        pyautogui.press("left", presses=press) 
   
    prioridade()
        
    def parada():
    
        print (parada1)
        # parada
        pyautogui.press ("tab", presses=3) 
        pyautogui.press ("space",presses = espaco) 
        pyautogui.press ("tab", presses=3) 
    
    parada()

    # centro de trabalho
    pyautogui.write(ctb)  

    def notificador():
        # notificador

        pyautogui.press ("tab", presses=2)   
        pyautogui.write(notificador1)
        pyautogui.press ("enter")
    
    notificador()

    # não determinar
    pyautogui.press ("tab")
    pyautogui.press ("enter")
    time.sleep(1)
    pyautogui.press ("enter")

    def subir_tela():

        # subir a tela

        pyautogui.click (barrascrollup)
        time.sleep (0.5) 
        pyautogui.scroll (1500)
    
    subir_tela()

    def save_and_print():

        imprimir = pyautogui.prompt(text = 'deseja imprimir a nota?', title = 'imprimir', default= '')
        if imprimir is None or imprimir.strip() == " ":
            raise ValueError ("nenhum valor foi fornecido. O programa será encerrado.")
        pyautogui.prompt
        if imprimir.lower() in ["sim"]:
            pyautogui.hotkey("shift", "f1")
            pyautogui.hotkey("ctrl", "p")
            pyautogui.click (barraimprimir)
            pyautogui.press ("tab", presses=10)   
            pyautogui.press("enter")
            imagem = pyautogui.screenshot()  # captura um screenshot da tela atual
            imagem.save("print nota automática.png")  # salva a imagem como um arquivo PNG
            pyautogui.alert ("Print salvo!")
            pyautogui.alert ("Fim do código!")
        else:
            pyautogui.hotkey("shift", "f1")
            pyautogui.hotkey("ctrl", "s")
            imagem = pyautogui.screenshot()  # captura um screenshot da tela atual
            imagem.save ("print") (titulo1) ("nota automática.png")  # salva a imagem como um arquivo PNG
            pyautogui.alert ("Print salvo!")
            pyautogui.alert ("Fim do código!")
    
    save_and_print()


# def conj_confirmacao():

#     confirmacao = pyautogui.prompt (text = "Os dados fornecidos foram: Tipologia = {tipologia1}, Título = {titulo1}, Descrição = {descricao1}, equipamento = {equipamento1}, setor = {setor1} Prioridade = {prioridade1}, Parada = {parada1}, Centro de trabalho = {centro_de_trabalho1}, Notificado = {notificador1}", title = "Tem certeza disso?")
#     if confirmacao in ['sim', 'tenho', 'Sim']:
#         criar_nota()
#     elif confirmacao in ["não", 'nao', 'Não', 'Nao']:
#         sys.exit()
# conj_confirmacao()

criar_nota()

print("Fim de código")