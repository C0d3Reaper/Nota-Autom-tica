import sys 
import datetime
import pyautogui
import time
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox

# Mensagens de alerta iniciais
pyautogui.alert(text="ATENÇÃO: o usuário deve fechar todos os aplicativos que ocupam espaço na barra de tarefas, deixando somente os que são fixos da barra.", title="Bem Vindo ao código de notas automáticas!")
pyautogui.alert(text="DICA: z1 = Corretiva planejada  |  z2 = Corretiva emergencial  |  z3 = Preventiva  |  zm = Requisição de compras  |  z0 = Nota de ação pm  |  z4 = Segurança do trabalho  |  z5 = Preditiva  |  z6 = Melhoria  |  z7 = Análise de falha  |  z8 = Retrabalho  |  z9 = Inspeção  |  zf = Fabricação de peças  |  zp = Projeto |", title="Aqui vai uma dica dos tipos de notas do sap!")

# Função para criar janelas de seleção de opções com botões
def escolher_opcao(titulo, opcoes):
    root = tk.Tk()
    root.title(titulo)
    width, height = 400, 400  # Aumentei a altura da janela
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")
    root.resizable(False, False)

    # Estilo
    style = ttk.Style()
    style.configure('TButton', font=('Arial', 12), padding=10)
    style.configure('TLabel', font=('Arial', 14))
    
    # Layout
    frame = ttk.Frame(root, padding=20)
    frame.pack(expand=True, fill="both")
    
    # Título
    ttk.Label(frame, text=titulo, anchor="center").pack(pady=10)
    
    # Variável para a escolha
    selected_option = [None]

    def selecionar(opcao):
        selected_option[0] = opcao
        root.destroy()

    # Criação de botões (usando pack apenas)
    for opcao in opcoes:
        ttk.Button(frame, text=opcao, command=lambda o=opcao: selecionar(o)).pack(
            pady=5, padx=10, fill="x"
        )
    
    root.mainloop()
    return selected_option[0]


# Função para capturar tipologia
def conj_tipologia():
    tipologias = ['Z0', 'Z1', 'Z2', 'Z3', 'Z4', 'Z5', 'Z6', 'Z7', 'Z8', 'Z9', 'ZF', 'ZM', 'ZP', 
                  'Zf', 'Zm', 'Zp', 'z0', 'z1', 'z2', 'z3', 'z4', 'z5', 'z6', 'z7', 'z8', 'z9', 'zf', 'zm', 'zp']
    
    while True:
        tipologia = pyautogui.prompt(text='Digite o tipo de nota (ex: z1, z2, z3, ...):', title='Tipo de Nota', default='')
        
        if tipologia is None:
            pyautogui.alert("Programa encerrado pelo usuário.", "Encerrando")
            sys.exit()
        
        tipologia = tipologia.strip()
        if tipologia == "":
            pyautogui.alert("Nenhum valor inserido. Por favor, insira uma tipologia válida.", "Aviso")
            continue
        
        if tipologia not in tipologias:
            pyautogui.alert("Tipologia inválida! Por favor, insira uma tipologia válida.", "Erro")
            continue
        
        return tipologia

# Função para capturar o título
def conj_titulo():
    while True:
        titulo = pyautogui.prompt(text='Digite o título da nota:', title='Título da nota', default='')
        if titulo is None:
            pyautogui.alert("Programa encerrado pelo usuário.", "Encerrando")
            sys.exit()
        
        if titulo.strip() == "":
            pyautogui.alert("Nenhum valor inserido. Por favor, insira um título válido.", "Aviso")
            continue
        
        return titulo.strip()
# Função para capturar a descrição com pyautogui.prompt
def conj_descricao():
    
    while True:
        descricao = pyautogui.prompt(text='Descreva a avaria da máquina:', title='Descrição', default='')
        if descricao is None:
            pyautogui.alert("Programa encerrado pelo usuário.", "Encerrando")
            sys.exit()
        
        if descricao.strip() == "":
            pyautogui.alert("Nenhum valor inserido. Por favor, insira uma descrição válida.", "Aviso")
            continue
        return descricao

# Função para capturar setor com botões
def conj_setor():
    setores = ["Embalagem", "Lã de Aço", "Química", "Envase", "Infraestrutura"]
    setor = escolher_opcao('Qual é o setor responsável?', setores)
    if setor is None:
        raise ValueError("Nenhum valor foi fornecido. O programa será encerrado.")
    return setor

# Função para capturar o equipamento com pyautogui.prompt
def conj_equipamento():
    while True:
        equipamento = pyautogui.prompt(text='Qual é o equipamento da avaria? (spo1011, emf1013, ...)', title='Código de identificação da máquina', default='')
        if len(equipamento) < 7:
            pyautogui.alert("Equipamento inválido!")
        elif equipamento is None or equipamento.strip() == "":
            raise ValueError("Nenhum valor foi fornecido. O programa será encerrado.")
        else:
            return equipamento

# Função para capturar centro de trabalho com botões
def conj_ctb():
    ctbs = ["Mecânica", "Elétrica"]
    centro_de_trabalho = escolher_opcao('Qual é o tipo de defeito?', ctbs)
    if centro_de_trabalho is None:
        raise ValueError("Nenhum valor foi fornecido. O programa será encerrado.")
    return centro_de_trabalho

# Função para capturar nome do notificador com pyautogui.prompt
def conj_notficador():
    notificador = pyautogui.prompt(text='Qual é o seu nome?', title='Nome do notificador', default='')
    if notificador is None or notificador.strip() == "":
        raise ValueError("Nenhum valor foi fornecido. O programa será encerrado.")
    return notificador

# Função para capturar se houve parada com botões
def conj_parada():
    paradas = ["Sim", "Não"]
    parada = escolher_opcao('Houve parada na máquina?', paradas)
    if parada is None:
        raise ValueError("Nenhum valor foi fornecido. O programa será encerrado.")
    return parada

# Função para capturar prioridade com botões
def conj_prioridade():
    prioridades = ["Rotina", "Emergencial", "Urgente", "Programável"]
    prioridade = escolher_opcao('Digite a prioridade da nota:', prioridades)
    if prioridade is None:
        raise ValueError("Nenhum valor foi fornecido. O programa será encerrado.")
    return prioridade

# Função para determinar o código de trabalho com base no centro de trabalho e setor
def determinar_codigo(centro_de_trabalho, setor):
    if centro_de_trabalho == "Mecânica" and setor == "Embalagem":
        return "embmeca"
    elif centro_de_trabalho == "Elétrica" and setor == "Embalagem":
        return "embele"
    elif centro_de_trabalho == "Mecânica" and setor == "Lã de Aço":
        return "lacmeca"
    elif centro_de_trabalho == "Elétrica" and setor == "Lã de Aço":
        return "lacelet"
    elif centro_de_trabalho == "Mecânica" and setor == "Infraestrutura":
        return "inframec"
    elif centro_de_trabalho == "Elétrica" and setor == "Infraestrutura":
        return "infraele"
    elif centro_de_trabalho == "Mecânica" and setor == "Química":
        return "quimeca"
    elif centro_de_trabalho == "Elétrica" and setor == "Química":
        return "quielet"
    return ""

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

# Código a ser escrito
codigo_trabalho = determinar_codigo(centro_de_trabalho1, setor1)

# Coordenadas
abre_barra_comandos = (61, 50)
barra_comandos = (119, 53)
clicasap = (845, 742)
janelasap = (941, 637)
barrascrolldown = (1340, 240)
barraprioridade = (491, 539)
barrascrollup = (1340, 240)
barraimprimir = (28, 231)
logoff = (321, 370)
botao_imprimir = (346, 54)

dados = titulo1, descricao1, tipologia1, parada1, equipamento1, notificador1, setor1, prioridade1
print (dados, sep=' ')

pyautogui.PAUSE = 0.9

def criar_nota():
    def sap_aberto():
        pyautogui.click(clicasap)
        time.sleep(0.5)
        pyautogui.click(janelasap)
        time.sleep(1)

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

    def preencher_tipologia():
        pyautogui.press("right", presses=2)
        pyautogui.press("backspace", presses=2)
        pyautogui.write(tipologia1)
        pyautogui.press("enter")
        time.sleep(0.5)

    preencher_tipologia()
    pyautogui.write(titulo1)
    pyautogui.press("enter")

    def preencher_equipamento():
        pyautogui.press('tab', presses=7)
        pyautogui.write(equipamento1)
        pyautogui.press("enter")
    
    preencher_equipamento()

    def preencher_descricao():
        pyautogui.press('tab', presses=13)
        pyautogui.write(descricao1)
        pyautogui.hotkey('ctrl', 'tab')
    
    preencher_descricao()

    def descer_tela():
        pyautogui.click(barrascrolldown)
        time.sleep(0.5) 
        pyautogui.scroll(-500)
    
    descer_tela()

    def definir_prioridade():
        pyautogui.click(barraprioridade)
        time.sleep(0.5)
       

        pyautogui.click(barraprioridade)
        if prioridade1 == "Rotina":
            pyautogui.press("left", presses=1)
        elif prioridade1 == "Programável":
            pyautogui.press("left", presses=2)
        elif prioridade1 == "Urgente":
            pyautogui.press("left", presses=3)
        elif prioridade1 == "Emergencial":
            pyautogui.press("left", presses=4)
   
    definir_prioridade()

    def definir_parada():
        pyautogui.press("tab", presses=3) 
        if parada1 == "Sim":
            pyautogui.press("space")  # Sim
            pyautogui.press("tab", presses=3)
        else:
            pyautogui.press("tab", presses=3)  # Não
   
    
    definir_parada()

    # Centro de trabalho
    pyautogui.write(codigo_trabalho)

    def preencher_notificador():
        pyautogui.press("tab", presses=2)   
        pyautogui.write(notificador1)
        pyautogui.press("enter")
    
    preencher_notificador()

    # Não determinar
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("enter")

    def subir_tela():
        pyautogui.click(barrascrollup)
        time.sleep(0.5) 
        pyautogui.scroll(1500)
    
    subir_tela()


def save_and_print():
    def on_response(response):
        if response == "Sim":
            pyautogui.hotkey("shift", "f1")
            pyautogui.click(botao_imprimir)
            pyautogui.click(barraimprimir)
            pyautogui.press("tab", presses=10)   
            pyautogui.press("enter")

        else:
            pyautogui.click(66, 122)
            time.sleep(1)
            pyautogui.press('enter')


        pyautogui.alert("Fim do código!")

    # Criar janela de confirmação
    root = tk.Tk()
    root.title("Imprimir Nota")
    width = 300
    height = 100
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

    tk.Label(root, text="Deseja imprimir a nota?").pack(pady=10)
    tk.Button(root, text="Sim", command=lambda: [on_response("Sim"), root.destroy()]).pack(side=tk.LEFT, padx=20)
    tk.Button(root, text="Não", command=lambda: [on_response("Não"), root.destroy()]).pack(side=tk.RIGHT, padx=20)

    root.mainloop()

time.sleep (1)
criar_nota()

save_and_print()


# def conj_confirmacao():

#     confirmacao = pyautogui.prompt (text = "Os dados fornecidos foram: Tipologia = {tipologia1}, Título = {titulo1}, Descrição = {descricao1}, equipamento = {equipamento1}, setor = {setor1} Prioridade = {prioridade1}, Parada = {parada1}, Centro de trabalho = {centro_de_trabalho1}, Notificado = {notificador1}", title = "Tem certeza disso?")
#     if confirmacao in ['sim', 'tenho', 'Sim']:
#         criar_nota()
#     elif confirmacao in ["não", 'nao', 'Não', 'Nao']:
#         sys.exit()
# conj_confirmacao()

print("Fim de código")
