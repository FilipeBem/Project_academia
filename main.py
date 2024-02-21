import tkinter as tk
from tkinter import messagebox
import PySimpleGUI as sg
import sqlite3


def salvar_dados(tabela, dados):
    try:
        # Criar conexão com o banco de dados
        conexao = sqlite3.connect('academia.db')
        cursor = conexao.cursor()

        # Verificar se a tabela já existe
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{tabela}'")
        if cursor.fetchone():
            # Se a tabela já existe, atualizar os dados
            cursor.execute(f"UPDATE {tabela} SET nome=:nome, email=:email, telefone=:telefone WHERE id=:id", dados)
        else:
            # Se a tabela não existe, criar a tabela e inserir os dados
            cursor.execute(f"CREATE TABLE {tabela} (id INTEGER PRIMARY KEY, nome TEXT, email TEXT, telefone TEXT)")
            cursor.execute(f"INSERT INTO {tabela} (nome, email, telefone) VALUES (:nome, :email, :telefone)", dados)

        # Salvar as alterações e fechar a conexão
        conexao.commit()
        conexao.close()

        # Exibir mensagem de sucesso
        sg.popup("Dados salvos com sucesso!")

    except Exception as ex:
        handle_exception(ex)

def cadastro_aluno():
    layout_aluno = [
        [sg.Text('Nome:'), sg.Input(key='nome_aluno')],
        [sg.Text('Data de Nascimento:'), sg.Input(key='data_nascimento_aluno')],
        [sg.Text('Sexo:'), sg.Combo(['Masculino', 'Feminino'], key='sexo_aluno')],
        [sg.Text('Telefone:'), sg.Input(key='telefone_aluno')],
        [sg.Text('CPF:'), sg.Input(key='cpf_aluno')],
        [sg.Text('Endereço:'), sg.Input(key='endereco_aluno')],
        [sg.Button('Cadastrar'), sg.Button('Cancelar')]
    ]

    window_aluno = sg.Window('Cadastro de Aluno', layout_aluno)

    while True:
        event, values = window_aluno.read()

        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break

        if event == 'Cadastrar':
            try:
                nome = values['nome_aluno']
                data_nascimento = values['data_nascimento_aluno']
                sexo = values['sexo_aluno']
                telefone = values['telefone_aluno']
                cpf = values['cpf_aluno']
                endereco = values['endereco_aluno']

                if not nome:
                    sg.popup('Erro: Nome é obrigatório.')
                elif not cpf:
                    sg.popup('Erro: CPF é obrigatório.')
                elif not sexo:
                    sg.popup('Erro: Sexo é obrigatório.')
                elif not telefone:
                    sg.popup('Erro: Telefone é obrigatório.')
                else:
                    

                    # Chamar o método salvar_dados
                    salvar_dados('alunos', {
                        'nome': nome,
                        'data_nascimento': data_nascimento or None,
                        'sexo': sexo,
                        'telefone': telefone,
                        'cpf': cpf,
                        'endereco': endereco  or None
                    })
                    sg.popup('Aluno cadastrado com sucesso!')
                    break

            except Exception as ex:
                sg.popup('Erro: ' + str(ex))

    window_aluno.close()

def cadastro_funcionario():
    layout_funcionario = [
        [sg.Text('Nome:'), sg.Input(key='nome_funcionario')],
        [sg.Text('Data de Nascimento:'), sg.Input(key='data_nascimento_funcionario')],
        [sg.Text('Sexo:'), sg.Combo(['Masculino', 'Feminino'], key='sexo_funcionario')],
        [sg.Text('Telefone:'), sg.Input(key='telefone_funcionario')],
        [sg.Text('CPF:'), sg.Input(key='cpf_funcionario')],
        [sg.Text('Endereço:'), sg.Input(key='endereco_funcionario')],
        [sg.Button('Cadastrar'), sg.Button('Cancelar')]
    ]

    window_funcionario = sg.Window('Cadastro de Funcionário', layout_funcionario)

    while True:
        event, values = window_funcionario.read()

        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break

        if event == 'Cadastrar':
            try:
                nome = values['nome_funcionario']
                data_nascimento = values['data_nascimento_funcionario']
                sexo = values['sexo_funcionario']
                telefone = values['telefone_funcionario']
                cpf = values['cpf_funcionario']
                endereco = values['endereco_funcionario']

                if not nome:
                    sg.popup('Erro: Nome é obrigatório.')
                elif not cpf:
                    sg.popup('Erro: CPF é obrigatório.')
                elif not sexo:
                    sg.popup('Erro: Sexo é obrigatório.')
                elif not telefone:
                    sg.popup('Erro: Telefone é obrigatório.')
                else:
                    # Insira aqui o código para salvar o funcionário no banco de dados
                    sg.popup('Funcionário cadastrado com sucesso!')
                    break

            except Exception as ex:
                sg.popup('Erro: ' + str(ex))

    window_funcionario.close()

def cadastro_donos():
    layout_dono = [
        [sg.Text('Nome:'), sg.Input(key='nome_dono')],
        [sg.Text('CPF:'), sg.Input(key='cpf_dono')],
        [sg.Text('Data de Nascimento:'), sg.Input(key='data_nascimento_dono')],
        [sg.Text('Sexo:'), sg.Combo(['Masculino', 'Feminino'], key='sexo_dono')],
        [sg.Text('Telefone:'), sg.Input(key='telefone_dono')],
        [sg.Text('Endereço:'), sg.Input(key='endereco_dono')],
        [sg.Button('Cadastrar'), sg.Button('Cancelar')]
    ]

    window_dono = sg.Window('Cadastro de Donos/Sócios', layout_dono)

    while True:
        event, values = window_dono.read()

        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break

        if event == 'Cadastrar':
            try:
                nome = values['nome_dono']
                cpf = values['cpf_dono']
                data_nascimento = values['data_nascimento_dono']
                sexo = values['sexo_dono']
                telefone = values['telefone_dono']
                endereco = values['endereco_dono']

                if not nome:
                    sg.popup('Erro: Nome é obrigatório.')
                elif not cpf:
                    sg.popup('Erro: CPF é obrigatório.')
                elif not data_nascimento:
                    sg.popup('Erro: Data de Nascimento é obrigatória.')
                elif not sexo:
                    sg.popup('Erro: Sexo é obrigatório.')
                elif not telefone:
                    sg.popup('Erro: Telefone é obrigatório.')
                else:
                    # Insira aqui o código para salvar o dono/sócio no banco de dados
                    sg.popup('Dono/Sócio cadastrado com sucesso!')
                    break

            except Exception as ex:
                sg.popup('Erro: ' + str(ex))

    window_dono.close()
    
    
def descadastro():
    pass

def controle_mensalidades():
    # code for controlling monthly fees
    pass

def fluxo_caixa():
    # code for cash flow control
    pass


def gerar_relatorios():
    # code for generating reports
    def controle_frequencia():
     pass

# Function for handling logout
def logoff():
     sg.Window.close_all()


#Manual
def user_manual_window():
    user_manual_text = """Bem-vindo ao Sistema de Controle da Academia!

Aqui estão algumas instruções para você começar:

1. Cadastre novos alunos selecionando 'Cadastros' e depois 'Alunos' na barra de menu.
2. Controle as mensalidades selecionando ‘Controle de Mensalidades’ no menu ‘Cadastros’.
3. Gerencie vendas e estoque selecionando 'Controle de Vendas e Estoque' no menu 'Movimentação'.
4. Monitore aniversários selecionando 'Controle de Aniversariantes' no menu 'Cadastros'.
5. Visualize o fluxo de caixa selecionando ‘Fluxo de Caixa’ no menu ‘Financeiro’.
6. Imprima os contratos selecionando 'Impressão de Contrato' no menu 'Cadastros'.
7. Imprima as planilhas de treinamento selecionando 'Impressão de Ficha de Treino' no menu 'Cadastros'.
8. Controle as despesas selecionando 'Controle de Despesas' no menu 'Financeiro'.
9. Controle o atendimento selecionando 'Controle de Frequência' no menu 'Cadastros'.
10. Gere relatórios selecionando 'Gerar Relatórios' no menu 'Relatórios'."""
    messagebox.showinfo("User Manual", user_manual_text)

# Function for handling exception
def handle_exception(ex):
    messagebox.showerror("Error", ex)


menu_definition = [
    ['Arquivos', ['Backup', 'Sair']],
    ['Cadastros', ['Alunos', 'Funcionarios','Donos/Sócios']],
    ['Descadastrar', [' Aluno', 'Funcionario','Donos/Sócios']],
    ['Financeiro', ['Fluxo de Caixa', 'Lançar Despesa', 'Baixa de Parcelas']],
    ['Relatórios', ['Informativo Financeiro', 'Inadiplentes', 'Quadro de Ocupação', 'Gerar Relatórios']],
    ['Help', ['User Manual']],
]


# Define the window's contents
layout = [
    [sg.Menu(menu_definition, tearoff=False)],
    [sg.Text("Bem-vindo ao Sistema de Controle da Academia!")],
    [sg.Button('Imprimir')], 
    [sg.Multiline(key='resultado', size=(90, 25), disabled=True, background_color='grey', text_color='black')],
]

# Create the window
window = sg.Window('Sistema de Controle da Academia!', layout, size=(600, 400), resizable=True, finalize=True)

# Display and interact with the Window
while True:
    event, values = window.read()
    try:
        if event == "Alunos":
                cadastro_aluno()
        if event == 'Funcionarios':
                cadastro_funcionario()
        if event == 'Donos/Sócios':
                cadastro_donos()
        elif event == "Descadastrar":
            if values['Alunos']:
                pass
            elif values['Funcionario']:
                pass
        elif event == "Financeiro":
            if values['Fluxo de Caixa']:
                fluxo_caixa()
            elif values['Lançar Despesa']:
                pass
            elif values['Baixa de Parcelas']:
                pass
        elif event == "Relatórios":
            if values['Informativo Financeiro']:
                pass
            elif values['Inadiplentes']:
                pass
            elif values['Quadro de Ocupação']:
                pass
            elif values['Gerar Relatórios']:
                pass
        if event == "Imprimir":
           print("Algum texto de exemplo")

        elif event == 'User Manual':
                user_manual_window()
        elif event == "Sair":
            window.close()
            break
        elif event == sg.WIN_CLOSED:
            break
    except Exception as ex:
        handle_exception(ex)

# Finish up by removing from the screen
window.close()
