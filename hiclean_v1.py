import pandas as pd
import openpyxl
import PySimpleGUI as sg
import pyperclip

from funcao1 import func1
from funcao1 import func2
from funcao1 import func3
from funcao1 import func4
from funcao1 import func5
from funcao1 import func6
from funcao1 import func7
from funcao1 import func8
from funcao1 import func9
from funcao1 import func10
from funcao2 import func11
from funcao2 import func12
from funcao2 import func13
from funcao2 import func14
from funcao2 import func15
from funcao2 import func16
from funcao2 import func17
from funcao2 import func18
from funcao2 import func19
from funcao2 import func20
from funcao3 import func21
from funcao3 import func22
from funcao3 import func23
from funcao3 import func24
from funcao3 import func25
from funcao3 import func26
from funcao3 import func27
from funcao3 import func28
from funcao3 import func29
from funcao3 import func30
from funcao4 import func31
from funcao4 import func32
from funcao4 import func33
from funcao4 import func34
from funcao4 import func35
from funcao4 import func36
from funcao4 import func37
from funcao4 import func38
from funcao4 import func39
from funcao4 import func40


xp = pd.read_excel("carros da Jeep 1.xlsx")

qtd_linhaspl = xp['Placa'].count()

if qtd_linhaspl == 1:
    x0 = (func1())
elif qtd_linhaspl == 2:
    x0 = (func2())
elif qtd_linhaspl == 3:
    x0 = (func3())
elif qtd_linhaspl == 4:
    x0 = (func4())
elif qtd_linhaspl == 5:
    x0 = (func5())
elif qtd_linhaspl == 6:
    x0 = (func6())
elif qtd_linhaspl == 7:
    x0 = (func7())
elif qtd_linhaspl == 8:
    x0 = (func8())
elif qtd_linhaspl == 9:
    x0 = (func9())
elif qtd_linhaspl == 10:
    x0 = (func10())
elif qtd_linhaspl == 11:
    x0 = (func11())
elif qtd_linhaspl == 12:
    x0 = (func12())
elif qtd_linhaspl == 13:
    x0 = (func13())
elif qtd_linhaspl == 14:
    x0 = (func14())
elif qtd_linhaspl == 15:
    x0 = (func15())
elif qtd_linhaspl == 16:
    x0 = (func16())
elif qtd_linhaspl == 17:
    x0 = (func17())
elif qtd_linhaspl == 18:
    x0 = (func18())
elif qtd_linhaspl == 19:
    x0 = (func19())
elif qtd_linhaspl == 20:
    x0 = (func20())
elif qtd_linhaspl == 21:
    x0 = (func21())
elif qtd_linhaspl == 22:
    x0 = (func22())
elif qtd_linhaspl == 23:
    x0 = (func23())
elif qtd_linhaspl == 24:
    x0 = (func24())
elif qtd_linhaspl == 25:
    x0 = (func25())
elif qtd_linhaspl == 26:
    x0 = (func26())
elif qtd_linhaspl == 27:
    x0 = (func27())
elif qtd_linhaspl == 28:
    x0 = (func28())
elif qtd_linhaspl == 29:
    x0 = (func29())
elif qtd_linhaspl == 30:
    x0 = (func30())
elif qtd_linhaspl == 31:
    x0 = (func31())
elif qtd_linhaspl == 32:
    x0 = (func32())
elif qtd_linhaspl == 33:
    x0 = (func33())
elif qtd_linhaspl == 34:
    x0 = (func34())
elif qtd_linhaspl == 35:
    x0 = (func35())
elif qtd_linhaspl == 36:
    x0 = (func36())
elif qtd_linhaspl == 37:
    x0 = (func37())
elif qtd_linhaspl == 38:
    x0 = (func38())
elif qtd_linhaspl == 39:
    x0 = (func39())
elif qtd_linhaspl == 40:
    x0 = (func40())


xx1 = '{}'.format(x0)


def mostra_descricao():


        esp1 = ''
        wy = 'DADOS BANCÁRIOS PARA CRÉDITO EM CONTA:'
        ey = 'AGÊNCIA: 0000'
        ry = 'CONTA: 00000000-0'
        ty = 'BANCO: 0000'
        uy = 'NU PAGAMENTOS S.A- INSTITUIÇÃO DE PAGAMENTO'
        dy = 'XXXXXXXXXX XXXXXX XX XXXXX'
        fy = 'CNPJ: 00.000.000/0000-00'
        gy = 'CPF: 00000000000'
        ny = 'VALOR TOTAL: "R$'
        total = '{:.2f}'.format(xp['Valor'].sum())

        # SEPARADOR DE PLACAS E MODELOS



        desc = '\n{}{:^20}{}{:^17}{}{:^17}{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{} {}{}'.format(
            'PLACA','','MODELO','', 'VALOR','', 'SERVIÇO', esp1,
            xx1, '', '', wy, ey, ry, ty, uy, dy, fy,
            gy, ny, total, '"')




        return desc


mostra_descricao()

sg.theme("Black")
Layout = [
    [sg.Text('Programa feito para gerar descrição de 40 itens. \nNesta versão é necessário que o programa e a planilha estejam na mesma pasta. \nA planilha deve ter exatamente este nome: "carros da Jeep 1.xlsx"\n', font=("Helvetica", 14))],
    #[#sg.In(key = 'Arquivo'), #sg.FileBrowse(key="-IN-"), #sg.Button('Submeter Arquivo')],
    [sg.Button('Gerar Descrição'), sg.Button('Copiar'), sg.Button('Limpar')],
    [sg.Multiline('', key = 'texto_descricao', size=(100,70))]

]
janela = sg.Window('Hi Clean v1.0 by LeoCabral', Layout, resizable = True)

while True:

    evento, valores = janela.read()
    #if evento == 'Submeter Arquivo':
        #endereco_arq = (valores["-IN-"]) # Para pegar o endereço do arquivo atravez da busca

    if evento == sg.WIN_CLOSED:
       break

    if evento == 'Gerar Descrição':
        descricao = mostra_descricao()
        janela['texto_descricao'].update(f'{descricao}')

    if evento == 'Copiar':
        pyperclip.copy(mostra_descricao())

    if evento == 'Limpar':
        descricao = ''
        janela['texto_descricao'].update(f'{descricao}')



janela.close()

#def endereco_arquivo(): # Função para distribuir o endereço pego anteriormente, para as outras funções do programa.

    #copia_endereco = endereco_arq
    #copia_endereco2 = copia_endereco.replace('/',"\g")
    #copia_endereco3 = copia_endereco2.replace('g','')
    #copia_endereco4 = '{}{}{}'.format('"',copia_endereco3,'"')
    #xp0 = pd.read_excel(copia_endereco4)

    #return xp0

#endereco_arquivo()












