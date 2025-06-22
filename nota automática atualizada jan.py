import sys
import pyautogui
import time
import tkinter as tk
from tkinter import ttk
import keyboard


# Coordenadas
abre_barra_comandos = (61, 50)
barra_comandos = (119, 53)
clicasap = (845, 742)
janelasap = (941, 637)
barrascrolldown = (1325, 275)
barraprioridade = (491, 539)
barraimprimir = (28, 231)
logoff = (321, 370)
botao_imprimir = (346, 54)

# Variáveis globais
tipologia1 = ""
parada = ""

# Mensagens de alerta iniciais
pyautogui.alert(
    text="ATENÇÃO: O usuário deve fechar todos os aplicativos que ocupam espaço na barra de tarefas, deixando somente os que são fixos da barra.",
    title="Bem Vindo ao código de notas automáticas!"
)

# Função para criar janelas de seleção de opções com botões
def escolher_opcao(titulo, opcoes):
    root = tk.Tk()
    root.title(titulo)
    width, height = 500, 400
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")
    root.resizable(False, False)

    style = ttk.Style()
    style.configure('TButton', font=('Arial', 12), padding=10)
    style.configure('TLabel', font=('Arial', 14))

    frame = ttk.Frame(root, padding=20)
    frame.pack(expand=True, fill="both")

    ttk.Label(frame, text=titulo, anchor="center").pack(pady=10)

    selected_option = [None]

    def selecionar(opcao):
        selected_option[0] = opcao
        root.destroy()

    for opcao in opcoes:
        ttk.Button(frame, text=opcao, command=lambda o=opcao: selecionar(o)).pack(
            pady=5, padx=10, fill="x"
        )

    root.mainloop()
    return selected_option[0]

# Funções para capturar tipologia
def pergunta1():
    global parada, tipologia1
    alternativas1 = ["Sim", "Não"]
    evento1 = escolher_opcao('Linha parada ou risco de segurança?', alternativas1)
    if evento1 is None:
        raise ValueError("Nenhum valor foi fornecido. O programa será encerrado.")
    
    if evento1 == "Sim":
        alternativas2 = ["Segurança", "Máquina parada"]
        entrada2 = escolher_opcao('Selecione uma das alternativas abaixo.', alternativas2)
        if entrada2 == "Segurança":
            tipologia1 = "Z4"
            parada = "não"
        else:
            tipologia1 = "Z2"
            parada = "sim"
    return evento1

def pergunta2():
    global tipologia1
    if not tipologia1:  
        alternativas1 = ["Sim", "Não"]
        evento1 = escolher_opcao('É retrabalho?', alternativas1)
        if evento1 is None:
            raise ValueError("Nenhum valor foi fornecido. O programa será encerrado.")
        
        if evento1 == "Sim":
            tipologia1 = "Z8"
        
        return evento1

def pergunta3():
    global tipologia1
    if not tipologia1:
        alternativas1 = ["Sim", "Não"]
        evento1 = escolher_opcao('É uma melhoria na máquina ou no processo?', alternativas1)
        
        if evento1 is None:
            raise ValueError("Nenhum valor foi fornecido. O programa será encerrado.")
        
        if evento1 == "Sim":
            tipologia1 = "Z6"
        else:
            tipologia1 = "Z1"
        
        return evento1

# Função para seleção de equipamento
def conj_equipamento():
    # Lista organizada em ordem alfabética conforme você forneceu:
    todas_tags = {
        'Embalagem': [
            'AE01', 'AF01', 'AI01', 'AI02', 'AI03', 'AI04', 'AI05', 'AI06', 'AR01',
            'AS05', 'AS06', 'AS10', 'AS15', 'AS25', 'AS32', 'AS33', 'AS34', 'AS35',
            'AS38', 'AS41', 'AS42', 'AS45', 'AS46', 'AS48', 'AS50', 'AS51', 'AS52',
            'AS54', 'AS55', 'AS56', 'AS57', 'AS58', 'AS59', 'AS60', 'AS61', 'AS62',
            'AS63', 'AS64', 'AS65', 'AS66', 'AS67', 'AS67', 'AS68', 'AS70', 'MT01',
            'MT02', 'MT03', 'MT04'
        ],
        'Lã de Aço': ['LA01', 'LA02', 'LA03'],
        'Química': ['QA01', 'QA02'],
        'Envase': ['EN01', 'EN02'],
        'Infraestrutura': ['INF01', 'INF02']
    }
    
    setor_selecionado = None
    maquina_selecionada = None

    def filtra_tags(event, tag_combobox, setor_combobox):
        setor = setor_combobox.get()
        tags_filtradas = todas_tags.get(setor, [])
        tag_combobox['values'] = tags_filtradas
        tag_combobox.set('')

    def finalizar_selecao(root, setor_combobox, tag_combobox):
        nonlocal setor_selecionado, maquina_selecionada
        setor_selecionado = setor_combobox.get()
        maquina_selecionada = tag_combobox.get().upper()  # Convertendo para maiúsculas
        
        # Verificações antes de destruir a janela
        if not setor_selecionado:
            pyautogui.alert(title="ATENÇÃO", text="Por favor, selecione um setor!")
            return
            
        if not maquina_selecionada:
            pyautogui.alert(title="ATENÇÃO", text="Por favor, selecione uma máquina!")
            return
            
        if setor_selecionado not in todas_tags:
            pyautogui.alert(title="ATENÇÃO", text="Setor inválido!")
            return
            
        if maquina_selecionada not in todas_tags.get(setor_selecionado, []):
            pyautogui.alert(title="ATENÇÃO", text="Máquina inválida para o setor selecionado!")
            return
            
        # Se tudo estiver correto, destrua a janela
        root.destroy()

    root = tk.Tk()
    root.geometry("500x300")
    root.title("Seleção de Setor e Máquina")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - 300 / 2)
    position_right = int(screen_width / 2 - 500 / 2)
    root.geometry(f"500x300+{position_right}+{position_top}")

    # Combobox para setor
    setor_combobox = ttk.Combobox(root, values=list(todas_tags.keys()))
    setor_combobox.pack(pady=20)

    # Combobox para máquina (será preenchido conforme o setor selecionado)
    tag_combobox = ttk.Combobox(root)
    tag_combobox.pack(pady=20)

    # Botão para finalizar seleção
    finalizar_button = tk.Button(
        root, 
        text="Finalizar Seleção", 
        command=lambda: finalizar_selecao(root, setor_combobox, tag_combobox)
    )
    finalizar_button.pack(pady=20)

    # Vincular evento de seleção de setor para filtrar máquinas
    setor_combobox.bind('<<ComboboxSelected>>', lambda event: filtra_tags(event, tag_combobox, setor_combobox))

    root.mainloop()
    
    # Retorna os valores selecionados (ou None se o usuário fechar a janela sem selecionar)
    return setor_selecionado, maquina_selecionada

    

# Função para substituir o código da máquina
def substituir_codigo(equipamento):
    mapeamento_codigos = {
        'AE01': 'EXT1002',
        'AF01': 'AFC1001',
        'AI01': 'IJA1001',
        'AI02': 'IJA1002',
        'AI03': 'IJA1003',
        'AI04': 'IJA1004',
        'AI05': 'IJA1005',
        'AI06': 'IJA1006',
        'AR01': 'REB1001',
        'AS05': 'SPO1005',
        'AS06': 'SPO1006',
        'AS10': 'SPO1010',
        'AS15': 'SPO1015',
        'AS25': 'SPO1025',
        'AS32': 'SPO1032',
        'AS33': 'SPO1033',
        'AS34': 'SPO1034',
        'AS35': 'SPO1035',
        'AS38': 'SPO1038',
        'AS41': 'SPO1041',
        'AS42': 'SPO1042',
        'AS45': 'SPO1045',
        'AS46': 'SPO1046',
        'AS48': 'SPO1048',
        'AS50': 'SPO1050',
        'AS51': 'SPO1051',
        'AS52': 'SPO1052',
        'AS54': 'SPO1054',
        'AS55': 'SPO1055',
        'AS56': 'SPO1056',
        'AS57': 'SPO1057',
        'AS58': 'SPO1058',
        'AS59': 'SPO1059',
        'AS60': 'SPO1060',
        'AS61': 'SPO1061',
        'AS62': 'SPO1062',
        'AS63': 'SPO1063',
        'AS64': 'SPO1064',
        'AS65': 'SPO1065',
        'AS66': 'SPO1066',
        'AS67': 'SPO1067',
        'AS68': 'SPO1068',
        'AS70': 'SPO1070',
        'MT01': 'MTN1001',
        'MT02': 'MTN1002',
        'MT03': 'MTN1003',
        'MT04': 'MTN1004'
    }


    return mapeamento_codigos.get(equipamento, equipamento)

# Funções para capturar título e descrição
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

def conj_descricao():
    while True:
        descricao = pyautogui.prompt(text='Descreva a avaria da máquina com no mínimo 30 caracteres:', title='Descrição', default='')
        if descricao is None:
            pyautogui.alert("Programa encerrado pelo usuário.", "Encerrando")
            sys.exit()
        if len(descricao) < 30:
            pyautogui.alert("A descrição deve ter pelo menos 30 caracteres. Tente novamente.")
            continue
        if descricao.strip() == "":
            pyautogui.alert("Nenhum valor inserido. Por favor, insira uma descrição válida.", "Aviso")
            continue
        return descricao

# Função para capturar tipo de defeito
def conj_ctb():
    ctbs = ["Mecânica", "Elétrica"]
    centro_de_trabalho = escolher_opcao('Qual é o tipo de defeito?', ctbs)
    if centro_de_trabalho is None:
        raise ValueError("Nenhum valor foi fornecido. O programa será encerrado.")
    return centro_de_trabalho

# Função para determinar código de trabalho
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

# Função para capturar nome do notificador
def conj_notficador():
    notificador = pyautogui.prompt(text='Qual é o seu nome?', title='Nome do notificador', default='')
    if notificador is None or notificador.strip() == "":
        raise ValueError("Nenhum valor foi fornecido. O programa será encerrado.")
    return notificador

# Função para determinar prioridade
def conj_prioridade():
    if tipologia1 == "Z2":
        prioridade1 = "Emergencial"
    elif tipologia1 == "Z1":
        prioridade1 = "Urgente"
    else:
        prioridade1 = "Programável"
    return prioridade1

# Execução das perguntas e captura de dados
pergunta1()
pergunta2()
pergunta3()

setor_selecionado, equipamento1 = conj_equipamento()
equipamento1 = substituir_codigo(equipamento1)
print(f"Setor selecionado: {setor_selecionado}")
print(f"Equipamento selecionado após substituição: {equipamento1}")

titulo1 = conj_titulo()
descricao1 = conj_descricao()
prioridade1 = conj_prioridade()
centro_de_trabalho1 = conj_ctb()
notificador1 = conj_notficador()

codigo_trabalho = determinar_codigo(centro_de_trabalho1, setor_selecionado)

dados = titulo1, descricao1, tipologia1, parada, equipamento1, notificador1, setor_selecionado, prioridade1
print(dados, sep=' ')

pyautogui.PAUSE = 1.5

def criar_nota():
    def sap_aberto():
        pyautogui.click(clicasap)
        time.sleep(0.5)
        pyautogui.click(janelasap)
        time.sleep(1)

    def iw21():
        pyautogui.hotkey('shift', 'f3')
        time.sleep(1)
        pyautogui.click(logoff)
        time.sleep(1)
        pyautogui.click(abre_barra_comandos)
        pyautogui.click(barra_comandos)
        pyautogui.write("iw21")
        pyautogui.press("enter")
    
    def preencher_tipologia():
        pyautogui.press("right", presses=2)
        pyautogui.press("backspace", presses=2)
        pyautogui.write(tipologia1)
        pyautogui.press("enter")
        time.sleep(0.5)

    def preencher_equipamento():
        pyautogui.press('tab', presses=7)
        pyautogui.write(equipamento1)
        pyautogui.press("enter")
    
    def preencher_descricao():
        pyautogui.press('tab', presses=13)
        keyboard.write(descricao1)
        pyautogui.hotkey('ctrl', 'tab')
    
    def descer_tela():
        pyautogui.click(barrascrolldown)
        time.sleep(0.5) 
        pyautogui.scroll(-500)
    
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
   
    def definir_parada():
        pyautogui.press("tab", presses=3) 
        if parada == "sim":
            pyautogui.press("space")
            pyautogui.press("tab", presses=3)
        else:
            pyautogui.press("tab", presses=3)
    
    def preencher_notificador():
        pyautogui.press("tab", presses=2)   
        keyboard.write(notificador1)
        pyautogui.press("enter")
    
    def subir_tela():
        pyautogui.press("PgUp")
    
    sap_aberto()
    iw21()
    preencher_tipologia()
    keyboard.write(titulo1)
    pyautogui.press("enter")
    preencher_equipamento()
    preencher_descricao()

    print(descricao1)

    descer_tela()
    definir_prioridade()
    definir_parada()
    pyautogui.write(codigo_trabalho)
    preencher_notificador()
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("enter")
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

time.sleep(1)
criar_nota()
save_and_print()

pyautogui.alert(title="Fim de operação.", text="Obrigado por utilizar!")
