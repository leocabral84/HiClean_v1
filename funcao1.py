def func1():
    import pandas as pd

    xp = pd.read_excel("carros da Jeep 1.xlsx")

    qtd_linhaspl = xp['Placa'].count()
    for ix in range((qtd_linhaspl - 1), -1, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x0 = '{}-{}'.format(inicio0, final0)

        celula_m = xp.loc[ix, 'Modelo']
        md02 = celula_m.upper()

        celula_v = xp.loc[0, 'Valor']
        valorp = '{} {}'.format('R$', float(celula_v))

        if xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

            # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

            # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('LAV. SIMPLES'))

            # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

            # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

            # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] == '' and xp.loc[0, 'Poli'] == '' and xp.loc[0, 'Vip'] == '':

            serv0 = ('{}'.format('POLIMENTO'))


        r2 = '{}{:^10}{}{:^10}{}{:^15}{}'.format(x0, '', md02,'',valorp, '', serv0)



        return r2
func1()

def func2():
    import pandas as pd

    xp = pd.read_excel("carros da Jeep 1.xlsx")

    qtd_linhaspl = xp['Placa'].count()
    for ix in range((qtd_linhaspl - 1), -1, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x0 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 0, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x1 = '{}-{}'.format(inicio0, final0)

        celula_m = xp.loc[0, 'Modelo']
        modelos02 = celula_m.upper()
        celula_m1 = xp.loc[1, 'Modelo']
        modelos05 = celula_m1.upper()

        celula_v = xp.loc[0, 'Valor']
        vp1 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[1, 'Valor']
        vp2 = '{} {}'.format('R$', float(celula_v))

        if xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

            # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

            # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('LAV. SIMPLES'))

            # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

            # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

            # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] == '' and xp.loc[0, 'Poli'] == '' and xp.loc[0, 'Vip'] == '':

            serv0 = ('{}'.format('POLIMENTO'))

            #######################

            # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

            # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

            # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('LAV. SIMPLES'))

            # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

            # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

            # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] == '' and xp.loc[1, 'Poli'] == '' and xp.loc[1, 'Vip'] == '':

            serv1 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))


        r2 = '{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}'.format(x0, '', modelos02, '', vp1,'',serv0, x1, '', modelos05, '', vp2,'',serv1)


        return r2
func2()



def func3():
    import pandas as pd

    xp = pd.read_excel("carros da Jeep 1.xlsx")
    qtd_linhaspl = xp['Placa'].count()
    for ix in range((qtd_linhaspl - 1), -1, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x0 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 0, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x1 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 1, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x2 = '{}-{}'.format(inicio0, final0)

        celula_m = xp.loc[0, 'Modelo']
        md02 = celula_m.upper()
        celula_m1 = xp.loc[1, 'Modelo']
        md05 = celula_m1.upper()
        celula_m2 = xp.loc[2, 'Modelo']
        md06 = celula_m2.upper()

        celula_v = xp.loc[0, 'Valor']
        vp1 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[1, 'Valor']
        vp2 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[2, 'Valor']
        vp3 = '{} {}'.format('R$', float(celula_v))

        if xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] == '' and xp.loc[0, 'Poli'] == '' and xp.loc[0, 'Vip'] == '':

            serv0 = ('{}'.format('POLIMENTO'))

        #######################

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] == '' and xp.loc[1, 'Poli'] == '' and xp.loc[1, 'Vip'] == '':

            serv1 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        #########################

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] == '' and xp.loc[2, 'Poli'] == '' and xp.loc[2, 'Vip'] == '':

            serv2 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))


        r2 = '{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}'.format(x0, '', md02, '', vp1, '', serv0, x1, '',
                        md05, '', vp2, '', serv1, x2, '', md06, '', vp3,'',serv2)


        return r2
func3()



def func4():
    import pandas as pd

    xp = pd.read_excel("carros da Jeep 1.xlsx")
    qtd_linhaspl = xp['Placa'].count()
    for ix in range((qtd_linhaspl - 1), -1, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x0 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 0, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x1  = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 1, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x2 = '{}-{}'.format(inicio0, final0)


    for ix in range((qtd_linhaspl - 1), 2, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x3 = '{}-{}'.format(inicio0, final0)

        celula_m = xp.loc[0, 'Modelo']
        md02 = celula_m.upper()
        celula_m1 = xp.loc[1, 'Modelo']
        md05 = celula_m1.upper()
        celula_m2 = xp.loc[2, 'Modelo']
        md06 = celula_m2.upper()
        celula_m3 = xp.loc[3, 'Modelo']
        md07 = celula_m3.upper()

        celula_v = xp.loc[0, 'Valor']
        vp1 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[1, 'Valor']
        vp2 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[2, 'Valor']
        vp3 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[3, 'Valor']
        vp4 = '{} {}'.format('R$', float(celula_v))

        if xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] == '' and xp.loc[0, 'Poli'] == '' and xp.loc[0, 'Vip'] == '':

            serv0 = ('{}'.format('POLIMENTO'))

        #######################

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] == '' and xp.loc[1, 'Poli'] == '' and xp.loc[1, 'Vip'] == '':

            serv1 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        #########################

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] == '' and xp.loc[2, 'Poli'] == '' and xp.loc[2, 'Vip'] == '':

            serv2 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        ############################

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] == '' and xp.loc[3, 'Poli'] == '' and xp.loc[3, 'Vip'] == '':

            serv3 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))




        r2 = '{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}'.format(x0, '', md02, '', vp1, '', serv0, x1, '',
                        md05, '', vp2, '', serv1, x2, '', md06, '', vp3,'',serv2, x3, '', md07, '', vp4,'',serv3)

        return r2
func4()



def func5():
    import pandas as pd

    xp = pd.read_excel("carros da Jeep 1.xlsx")

    qtd_linhaspl = xp['Placa'].count()
    for ix in range((qtd_linhaspl - 1), -1, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x0 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 0, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x1  = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 1, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x2 = '{}-{}'.format(inicio0, final0)


    for ix in range((qtd_linhaspl - 1), 2, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x3 = '{}-{}'.format(inicio0, final0)


    for ix in range((qtd_linhaspl - 1), 3, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x4 = '{}-{}'.format(inicio0, final0)

        celula_m = xp.loc[0, 'Modelo']
        md02 = celula_m.upper()
        celula_m1 = xp.loc[1, 'Modelo']
        md05 = celula_m1.upper()
        celula_m2 = xp.loc[2, 'Modelo']
        md06 = celula_m2.upper()
        celula_m3 = xp.loc[3, 'Modelo']
        md07 = celula_m3.upper()
        celula_m4 = xp.loc[4, 'Modelo']
        md08 = celula_m4.upper()

        celula_v = xp.loc[0, 'Valor']
        vp1 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[1, 'Valor']
        vp2 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[2, 'Valor']
        vp3 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[3, 'Valor']
        vp4 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[4, 'Valor']
        vp5 = '{} {}'.format('R$', float(celula_v))

        if xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] == '' and xp.loc[0, 'Poli'] == '' and xp.loc[0, 'Vip'] == '':

            serv0 = ('{}'.format('POLIMENTO'))

        #######################

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] == '' and xp.loc[1, 'Poli'] == '' and xp.loc[1, 'Vip'] == '':

            serv1 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        #########################

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] == '' and xp.loc[2, 'Poli'] == '' and xp.loc[2, 'Vip'] == '':

            serv2 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        ############################

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] == '' and xp.loc[3, 'Poli'] == '' and xp.loc[3, 'Vip'] == '':

            serv3 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))
        ##########################
        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[4, 'Lavagem simples'] == 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] == 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] == 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] != 'x' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] != 'X' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[4, 'Lavagem simples'] == 'X' and xp.loc[4, 'Poli'] != 'x' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[4, 'Lavagem simples'] == 'X' and xp.loc[4, 'Poli'] != 'X' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] != 'x' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] != 'X' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] != 'X' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] != 'x' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] != 'X' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] != 'x' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] == '' and xp.loc[4, 'Poli'] == '' and xp.loc[4, 'Vip'] == '':

            serv4 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))


        r2 = '{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}'.format(x0, '', md02, '', vp1, '', serv0, x1, '',
    md05, '', vp2, '', serv1, x2, '', md06, '', vp3,'',serv2, x3,
    '', md07, '', vp4,'',serv3, x4, '', md08, '', vp5,'', serv4)


        return r2
func5()



def func6():
    import pandas as pd

    xp = pd.read_excel("carros da Jeep 1.xlsx")

    qtd_linhaspl = xp['Placa'].count()
    for ix in range((qtd_linhaspl - 1), -1, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x0 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 0, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x1 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 1, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x2 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 2, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x3 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 3, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x4 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 4, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x5 = '{}-{}'.format(inicio0, final0)

        celula_m = xp.loc[0, 'Modelo']
        md02 = celula_m.upper()
        celula_m1 = xp.loc[1, 'Modelo']
        md05 = celula_m1.upper()
        celula_m2 = xp.loc[2, 'Modelo']
        md06 = celula_m2.upper()
        celula_m3 = xp.loc[3, 'Modelo']
        md07 = celula_m3.upper()
        celula_m4 = xp.loc[4, 'Modelo']
        md08 = celula_m4.upper()
        celula_m5 = xp.loc[5, 'Modelo']
        md09 = celula_m5.upper()

        celula_v = xp.loc[0, 'Valor']
        vp1 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[1, 'Valor']
        vp2 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[2, 'Valor']
        vp3 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[3, 'Valor']
        vp4 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[4, 'Valor']
        vp5 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[5, 'Valor']
        vp6 = '{} {}'.format('R$', float(celula_v))

        if xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] == '' and xp.loc[0, 'Poli'] == '' and xp.loc[0, 'Vip'] == '':

            serv0 = ('{}'.format('POLIMENTO'))

        #######################

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] == '' and xp.loc[1, 'Poli'] == '' and xp.loc[1, 'Vip'] == '':

            serv1 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        #########################

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] == '' and xp.loc[2, 'Poli'] == '' and xp.loc[2, 'Vip'] == '':

            serv2 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        ############################

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] == '' and xp.loc[3, 'Poli'] == '' and xp.loc[3, 'Vip'] == '':

            serv3 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))
        ##########################
        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[4, 'Lavagem simples'] == 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] == 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] == 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] != 'x' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] != 'X' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[4, 'Lavagem simples'] == 'X' and xp.loc[4, 'Poli'] != 'x' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[4, 'Lavagem simples'] == 'X' and xp.loc[4, 'Poli'] != 'X' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] != 'x' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] != 'X' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] != 'X' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] != 'x' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] != 'X' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] != 'x' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] == '' and xp.loc[4, 'Poli'] == '' and xp.loc[4, 'Vip'] == '':

            serv4 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'X':

            serv5 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[5, 'Lavagem simples'] == 'X' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] == 'X' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] == 'X' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] != 'x' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] != 'X' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[5, 'Lavagem simples'] == 'X' and xp.loc[5, 'Poli'] != 'x' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[5, 'Lavagem simples'] == 'X' and xp.loc[5, 'Poli'] != 'X' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'X':

            serv5 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'X':

            serv5 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] != 'x' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] != 'X' and xp.loc[5, 'Vip'] == 'X':

            serv5 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] != 'X' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] != 'x' and xp.loc[5, 'Vip'] == 'X':

            serv5 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] != 'X' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] != 'x' and xp.loc[5, 'Vip'] == 'X':

            serv5 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}'.format('POLIMENTO'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}'.format('POLIMENTO'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}'.format('POLIMENTO'))

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}'.format('POLIMENTO'))

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}'.format('POLIMENTO'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}'.format('POLIMENTO'))

        elif xp.loc[5, 'Lavagem simples'] == '' and xp.loc[5, 'Poli'] == '' and xp.loc[5, 'Vip'] == '':

            serv5 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        r2 = '{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}'.format(x0, '', md02, '', vp1, '', serv0, x1, '',
    md05, '', vp2, '', serv1, x2, '', md06, '', vp3,'',serv2, x3,
    '', md07, '', vp4,'',serv3, x4, '', md08, '', vp5,'', serv4, x5, '', md09, '', vp6,'',serv5)

        return r2

func6()



def func7():
    import pandas as pd

    xp = pd.read_excel("carros da Jeep 1.xlsx")

    qtd_linhaspl = xp['Placa'].count()
    for ix in range((qtd_linhaspl - 1), -1, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x0 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 0, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x1 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 1, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x2 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 2, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x3 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 3, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x4 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 4, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x5 = '{}-{}'.format(inicio0, final0)


    for ix in range((qtd_linhaspl - 1), 5, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x6 = '{}-{}'.format(inicio0, final0)

        celula_m = xp.loc[0, 'Modelo']
        md02 = celula_m.upper()
        celula_m1 = xp.loc[1, 'Modelo']
        md05 = celula_m1.upper()
        celula_m2 = xp.loc[2, 'Modelo']
        md06 = celula_m2.upper()
        celula_m3 = xp.loc[3, 'Modelo']
        md07 = celula_m3.upper()
        celula_m4 = xp.loc[4, 'Modelo']
        md08 = celula_m4.upper()
        celula_m5 = xp.loc[5, 'Modelo']
        md09 = celula_m5.upper()
        celula_m6 = xp.loc[6, 'Modelo']
        md10 = celula_m6.upper()

        celula_v = xp.loc[0, 'Valor']
        vp1 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[1, 'Valor']
        vp2 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[2, 'Valor']
        vp3 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[3, 'Valor']
        vp4 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[4, 'Valor']
        vp5 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[5, 'Valor']
        vp6 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[6, 'Valor']
        vp7 = '{} {}'.format('R$', float(celula_v))

        if xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] == '' and xp.loc[0, 'Poli'] == '' and xp.loc[0, 'Vip'] == '':

            serv0 = ('{}'.format('POLIMENTO'))

        #######################

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] == '' and xp.loc[1, 'Poli'] == '' and xp.loc[1, 'Vip'] == '':

            serv1 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        #########################

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] == '' and xp.loc[2, 'Poli'] == '' and xp.loc[2, 'Vip'] == '':

            serv2 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        ############################

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] == '' and xp.loc[3, 'Poli'] == '' and xp.loc[3, 'Vip'] == '':

            serv3 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))
        ##########################
        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[4, 'Lavagem simples'] == 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] == 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] == 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] != 'x' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] != 'X' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[4, 'Lavagem simples'] == 'X' and xp.loc[4, 'Poli'] != 'x' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[4, 'Lavagem simples'] == 'X' and xp.loc[4, 'Poli'] != 'X' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] != 'x' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] != 'X' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] != 'X' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] != 'x' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] != 'X' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] != 'x' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] == '' and xp.loc[4, 'Poli'] == '' and xp.loc[4, 'Vip'] == '':

            serv4 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'X':

            serv5 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[5, 'Lavagem simples'] == 'X' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] == 'X' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] == 'X' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] != 'x' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] != 'X' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[5, 'Lavagem simples'] == 'X' and xp.loc[5, 'Poli'] != 'x' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[5, 'Lavagem simples'] == 'X' and xp.loc[5, 'Poli'] != 'X' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'X':

            serv5 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'X':

            serv5 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] != 'x' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] != 'X' and xp.loc[5, 'Vip'] == 'X':

            serv5 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] != 'X' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] != 'x' and xp.loc[5, 'Vip'] == 'X':

            serv5 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] != 'X' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] != 'x' and xp.loc[5, 'Vip'] == 'X':

            serv5 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}'.format('POLIMENTO'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}'.format('POLIMENTO'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}'.format('POLIMENTO'))

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}'.format('POLIMENTO'))

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}'.format('POLIMENTO'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}'.format('POLIMENTO'))

        elif xp.loc[5, 'Lavagem simples'] == '' and xp.loc[5, 'Poli'] == '' and xp.loc[5, 'Vip'] == '':

            serv5 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))
        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] == 'X':

            serv6 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] == 'X' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[6, 'Lavagem simples'] == 'X' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] != 'x':

            serv6 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] != 'X':

            serv6 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] == 'X' and xp.loc[6, 'Vip'] != 'x':

            serv6 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] == 'X' and xp.loc[6, 'Vip'] != 'X':

            serv6 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] == 'X' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] != 'x':

            serv6 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] == 'X' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] != 'X':

            serv6 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] != 'x' and xp.loc[6, 'Vip'] != 'x':

            serv6 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] != 'X' and xp.loc[6, 'Vip'] != 'X':

            serv6 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[6, 'Lavagem simples'] == 'X' and xp.loc[6, 'Poli'] != 'x' and xp.loc[6, 'Vip'] != 'X':

            serv6 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[6, 'Lavagem simples'] == 'X' and xp.loc[6, 'Poli'] != 'X' and xp.loc[6, 'Vip'] != 'x':

            serv6 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] == 'X' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] == 'X' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] == 'X':

            serv6 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] == 'X':

            serv6 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] != 'x' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] != 'X' and xp.loc[6, 'Vip'] == 'X':

            serv6 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] != 'X' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] != 'x' and xp.loc[6, 'Vip'] == 'X':

            serv6 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] != 'X' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] != 'x' and xp.loc[6, 'Vip'] == 'X':

            serv6 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] != 'x':

            serv6 = ('{}'.format('POLIMENTO'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] == 'X' and xp.loc[6, 'Vip'] != 'X':

            serv6 = ('{}'.format('POLIMENTO'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] != 'X':

            serv6 = ('{}'.format('POLIMENTO'))

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] == 'X' and xp.loc[6, 'Vip'] != 'x':

            serv6 = ('{}'.format('POLIMENTO'))

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] != 'X':

            serv6 = ('{}'.format('POLIMENTO'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] == 'X' and xp.loc[6, 'Vip'] != 'x':

            serv6 = ('{}'.format('POLIMENTO'))

        elif xp.loc[6, 'Lavagem simples'] == '' and xp.loc[6, 'Poli'] == '' and xp.loc[6, 'Vip'] == '':

            serv6 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))


        r2 = '{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}'.format(x0, '', md02, '', vp1, '', serv0, x1, '',
    md05, '', vp2, '', serv1, x2, '', md06, '', vp3,'',serv2, x3,
    '', md07, '', vp4,'',serv3, x4, '', md08, '', vp5,'', serv4, x5, '', md09, '', vp6,'',serv5, x6, '', md10, '', vp7,'',serv6)

        return r2


func7()



def func8():
    import pandas as pd

    xp = pd.read_excel("carros da Jeep 1.xlsx")

    qtd_linhaspl = xp['Placa'].count()
    for ix in range((qtd_linhaspl - 1), -1, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x0 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 0, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x1 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 1, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x2 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 2, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x3 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 3, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x4 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 4, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x5 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 5, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x6 = '{}-{}'.format(inicio0, final0)


    for ix in range((qtd_linhaspl - 1), 6, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x7 = '{}-{}'.format(inicio0, final0)

        celula_m = xp.loc[0, 'Modelo']
        md02 = celula_m.upper()
        celula_m1 = xp.loc[1, 'Modelo']
        md05 = celula_m1.upper()
        celula_m2 = xp.loc[2, 'Modelo']
        md06 = celula_m2.upper()
        celula_m3 = xp.loc[3, 'Modelo']
        md07 = celula_m3.upper()
        celula_m4 = xp.loc[4, 'Modelo']
        md08 = celula_m4.upper()
        celula_m5 = xp.loc[5, 'Modelo']
        md09 = celula_m5.upper()
        celula_m6 = xp.loc[6, 'Modelo']
        md10 = celula_m6.upper()
        celula_m7 = xp.loc[7, 'Modelo']
        md11 = celula_m7.upper()

        celula_v = xp.loc[0, 'Valor']
        vp1 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[1, 'Valor']
        vp2 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[2, 'Valor']
        vp3 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[3, 'Valor']
        vp4 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[4, 'Valor']
        vp5 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[5, 'Valor']
        vp6 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[6, 'Valor']
        vp7 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[7, 'Valor']
        vp8 = '{} {}'.format('R$', float(celula_v))

        if xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] == '' and xp.loc[0, 'Poli'] == '' and xp.loc[0, 'Vip'] == '':

            serv0 = ('{}'.format('POLIMENTO'))

        #######################

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] == '' and xp.loc[1, 'Poli'] == '' and xp.loc[1, 'Vip'] == '':

            serv1 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        #########################

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] == '' and xp.loc[2, 'Poli'] == '' and xp.loc[2, 'Vip'] == '':

            serv2 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        ############################

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] == '' and xp.loc[3, 'Poli'] == '' and xp.loc[3, 'Vip'] == '':

            serv3 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))
        ##########################
        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[4, 'Lavagem simples'] == 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] == 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] == 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] != 'x' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] != 'X' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[4, 'Lavagem simples'] == 'X' and xp.loc[4, 'Poli'] != 'x' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[4, 'Lavagem simples'] == 'X' and xp.loc[4, 'Poli'] != 'X' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] != 'x' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] != 'X' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] != 'X' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] != 'x' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] != 'X' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] != 'x' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] == '' and xp.loc[4, 'Poli'] == '' and xp.loc[4, 'Vip'] == '':

            serv4 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'X':

            serv5 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[5, 'Lavagem simples'] == 'X' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] == 'X' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] == 'X' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] != 'x' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] != 'X' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[5, 'Lavagem simples'] == 'X' and xp.loc[5, 'Poli'] != 'x' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[5, 'Lavagem simples'] == 'X' and xp.loc[5, 'Poli'] != 'X' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'X':

            serv5 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'X':

            serv5 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] != 'x' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] != 'X' and xp.loc[5, 'Vip'] == 'X':

            serv5 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] != 'X' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] != 'x' and xp.loc[5, 'Vip'] == 'X':

            serv5 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] != 'X' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] != 'x' and xp.loc[5, 'Vip'] == 'X':

            serv5 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}'.format('POLIMENTO'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}'.format('POLIMENTO'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}'.format('POLIMENTO'))

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}'.format('POLIMENTO'))

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}'.format('POLIMENTO'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}'.format('POLIMENTO'))

        elif xp.loc[5, 'Lavagem simples'] == '' and xp.loc[5, 'Poli'] == '' and xp.loc[5, 'Vip'] == '':

            serv5 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))
        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] == 'X':

            serv6 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] == 'X' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[6, 'Lavagem simples'] == 'X' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] != 'x':

            serv6 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] != 'X':

            serv6 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] == 'X' and xp.loc[6, 'Vip'] != 'x':

            serv6 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] == 'X' and xp.loc[6, 'Vip'] != 'X':

            serv6 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] == 'X' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] != 'x':

            serv6 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] == 'X' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] != 'X':

            serv6 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] != 'x' and xp.loc[6, 'Vip'] != 'x':

            serv6 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] != 'X' and xp.loc[6, 'Vip'] != 'X':

            serv6 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[6, 'Lavagem simples'] == 'X' and xp.loc[6, 'Poli'] != 'x' and xp.loc[6, 'Vip'] != 'X':

            serv6 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[6, 'Lavagem simples'] == 'X' and xp.loc[6, 'Poli'] != 'X' and xp.loc[6, 'Vip'] != 'x':

            serv6 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] == 'X' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] == 'X' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] == 'X':

            serv6 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] == 'X':

            serv6 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] != 'x' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] != 'X' and xp.loc[6, 'Vip'] == 'X':

            serv6 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] != 'X' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] != 'x' and xp.loc[6, 'Vip'] == 'X':

            serv6 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] != 'X' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] != 'x' and xp.loc[6, 'Vip'] == 'X':

            serv6 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] != 'x':

            serv6 = ('{}'.format('POLIMENTO'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] == 'X' and xp.loc[6, 'Vip'] != 'X':

            serv6 = ('{}'.format('POLIMENTO'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] != 'X':

            serv6 = ('{}'.format('POLIMENTO'))

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] == 'X' and xp.loc[6, 'Vip'] != 'x':

            serv6 = ('{}'.format('POLIMENTO'))

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] != 'X':

            serv6 = ('{}'.format('POLIMENTO'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] == 'X' and xp.loc[6, 'Vip'] != 'x':

            serv6 = ('{}'.format('POLIMENTO'))

        elif xp.loc[6, 'Lavagem simples'] == '' and xp.loc[6, 'Poli'] == '' and xp.loc[6, 'Vip'] == '':

            serv6 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[7, 'Lavagem simples'] == 'x' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] == 'x':

            serv7 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[7, 'Lavagem simples'] == 'x' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] == 'X':

            serv7 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[7, 'Lavagem simples'] == 'x' and xp.loc[7, 'Poli'] == 'X' and xp.loc[7, 'Vip'] == 'x':

            serv7 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[7, 'Lavagem simples'] == 'X' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] == 'x':

            serv7 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[7, 'Lavagem simples'] == 'x' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] != 'x':

            serv7 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[7, 'Lavagem simples'] == 'x' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] != 'X':

            serv7 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[7, 'Lavagem simples'] == 'x' and xp.loc[7, 'Poli'] == 'X' and xp.loc[7, 'Vip'] != 'x':

            serv7 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[7, 'Lavagem simples'] == 'x' and xp.loc[7, 'Poli'] == 'X' and xp.loc[7, 'Vip'] != 'X':

            serv7 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[7, 'Lavagem simples'] == 'X' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] != 'x':

            serv7 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[7, 'Lavagem simples'] == 'X' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] != 'X':

            serv7 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[7, 'Lavagem simples'] == 'x' and xp.loc[7, 'Poli'] != 'x' and xp.loc[7, 'Vip'] != 'x':

            serv7 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[7, 'Lavagem simples'] == 'x' and xp.loc[7, 'Poli'] != 'X' and xp.loc[7, 'Vip'] != 'X':

            serv7 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[7, 'Lavagem simples'] == 'X' and xp.loc[7, 'Poli'] != 'x' and xp.loc[7, 'Vip'] != 'X':

            serv7 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[7, 'Lavagem simples'] == 'X' and xp.loc[7, 'Poli'] != 'X' and xp.loc[7, 'Vip'] != 'x':

            serv7 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[7, 'Lavagem simples'] != 'x' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] == 'x':

            serv7 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[7, 'Lavagem simples'] != 'X' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] == 'x':

            serv7 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[7, 'Lavagem simples'] != 'x' and xp.loc[7, 'Poli'] == 'X' and xp.loc[7, 'Vip'] == 'x':

            serv7 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[7, 'Lavagem simples'] != 'X' and xp.loc[7, 'Poli'] == 'X' and xp.loc[7, 'Vip'] == 'x':

            serv7 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[7, 'Lavagem simples'] != 'x' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] == 'X':

            serv7 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[7, 'Lavagem simples'] != 'X' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] == 'X':

            serv7 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[7, 'Lavagem simples'] != 'x' and xp.loc[7, 'Poli'] != 'x' and xp.loc[7, 'Vip'] == 'x':

            serv7 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[7, 'Lavagem simples'] != 'X' and xp.loc[7, 'Poli'] != 'X' and xp.loc[7, 'Vip'] == 'X':

            serv7 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[7, 'Lavagem simples'] != 'X' and xp.loc[7, 'Poli'] != 'X' and xp.loc[7, 'Vip'] == 'x':

            serv7 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[7, 'Lavagem simples'] != 'x' and xp.loc[7, 'Poli'] != 'x' and xp.loc[7, 'Vip'] == 'X':

            serv7 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[7, 'Lavagem simples'] != 'x' and xp.loc[7, 'Poli'] != 'X' and xp.loc[7, 'Vip'] == 'x':

            serv7 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[7, 'Lavagem simples'] != 'X' and xp.loc[7, 'Poli'] != 'x' and xp.loc[7, 'Vip'] == 'X':

            serv7 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[7, 'Lavagem simples'] != 'x' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] != 'x':

            serv7 = ('{}'.format('POLIMENTO'))

        elif xp.loc[7, 'Lavagem simples'] != 'X' and xp.loc[7, 'Poli'] == 'X' and xp.loc[7, 'Vip'] != 'X':

            serv7 = ('{}'.format('POLIMENTO'))

        elif xp.loc[7, 'Lavagem simples'] != 'X' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] != 'X':

            serv7 = ('{}'.format('POLIMENTO'))

        elif xp.loc[7, 'Lavagem simples'] != 'x' and xp.loc[7, 'Poli'] == 'X' and xp.loc[7, 'Vip'] != 'x':

            serv7 = ('{}'.format('POLIMENTO'))

        elif xp.loc[7, 'Lavagem simples'] != 'x' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] != 'X':

            serv7 = ('{}'.format('POLIMENTO'))

        elif xp.loc[7, 'Lavagem simples'] != 'X' and xp.loc[7, 'Poli'] == 'X' and xp.loc[7, 'Vip'] != 'x':

            serv7 = ('{}'.format('POLIMENTO'))

        elif xp.loc[7, 'Lavagem simples'] == '' and xp.loc[7, 'Poli'] == '' and xp.loc[7, 'Vip'] == '':

            serv7 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        r2 = '{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}'.format(x0, '', md02, '', vp1, '', serv0, x1, '',
    md05, '', vp2, '', serv1, x2, '', md06, '', vp3,'',serv2, x3,
    '', md07, '', vp4,'',serv3, x4, '', md08, '', vp5,'', serv4, x5, '',
      md09, '', vp6,'',serv5, x6, '', md10, '', vp7,'',serv6, x7, '', md11, '', vp8,'',serv7)

        return r2


func8()


def func9():
    import pandas as pd

    xp = pd.read_excel("carros da Jeep 1.xlsx")

    qtd_linhaspl = xp['Placa'].count()
    for ix in range((qtd_linhaspl - 1), -1, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x0 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 0, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x1 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 1, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x2 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 2, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x3 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 3, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x4 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 4, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x5 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 5, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x6 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 6, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x7 = '{}-{}'.format(inicio0, final0)


    for ix in range((qtd_linhaspl - 1), 7, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x8 = '{}-{}'.format(inicio0, final0)

        celula_m = xp.loc[0, 'Modelo']
        md02 = celula_m.upper()
        celula_m1 = xp.loc[1, 'Modelo']
        md05 = celula_m1.upper()
        celula_m2 = xp.loc[2, 'Modelo']
        md06 = celula_m2.upper()
        celula_m3 = xp.loc[3, 'Modelo']
        md07 = celula_m3.upper()
        celula_m4 = xp.loc[4, 'Modelo']
        md08 = celula_m4.upper()
        celula_m5 = xp.loc[5, 'Modelo']
        md09 = celula_m5.upper()
        celula_m6 = xp.loc[6, 'Modelo']
        md10 = celula_m6.upper()
        celula_m7 = xp.loc[7, 'Modelo']
        md11 = celula_m7.upper()
        celula_m8 = xp.loc[8, 'Modelo']
        md12 = celula_m8.upper()

        celula_v = xp.loc[0, 'Valor']
        vp1 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[1, 'Valor']
        vp2 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[2, 'Valor']
        vp3 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[3, 'Valor']
        vp4 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[4, 'Valor']
        vp5 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[5, 'Valor']
        vp6 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[6, 'Valor']
        vp7 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[7, 'Valor']
        vp8 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[8, 'Valor']
        vp9 = '{} {}'.format('R$', float(celula_v))

        if xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] == '' and xp.loc[0, 'Poli'] == '' and xp.loc[0, 'Vip'] == '':

            serv0 = ('{}'.format('POLIMENTO'))

        #######################

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] == '' and xp.loc[1, 'Poli'] == '' and xp.loc[1, 'Vip'] == '':

            serv1 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        #########################

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] == '' and xp.loc[2, 'Poli'] == '' and xp.loc[2, 'Vip'] == '':

            serv2 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        ############################

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] == '' and xp.loc[3, 'Poli'] == '' and xp.loc[3, 'Vip'] == '':

            serv3 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))
        ##########################
        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[4, 'Lavagem simples'] == 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] == 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] == 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] != 'x' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] != 'X' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[4, 'Lavagem simples'] == 'X' and xp.loc[4, 'Poli'] != 'x' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[4, 'Lavagem simples'] == 'X' and xp.loc[4, 'Poli'] != 'X' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] != 'x' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] != 'X' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] != 'X' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] != 'x' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] != 'X' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] != 'x' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] == '' and xp.loc[4, 'Poli'] == '' and xp.loc[4, 'Vip'] == '':

            serv4 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'X':

            serv5 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[5, 'Lavagem simples'] == 'X' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] == 'X' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] == 'X' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] != 'x' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] != 'X' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[5, 'Lavagem simples'] == 'X' and xp.loc[5, 'Poli'] != 'x' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[5, 'Lavagem simples'] == 'X' and xp.loc[5, 'Poli'] != 'X' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'X':

            serv5 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'X':

            serv5 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] != 'x' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] != 'X' and xp.loc[5, 'Vip'] == 'X':

            serv5 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] != 'X' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] != 'x' and xp.loc[5, 'Vip'] == 'X':

            serv5 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] != 'X' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] != 'x' and xp.loc[5, 'Vip'] == 'X':

            serv5 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}'.format('POLIMENTO'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}'.format('POLIMENTO'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}'.format('POLIMENTO'))

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}'.format('POLIMENTO'))

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}'.format('POLIMENTO'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}'.format('POLIMENTO'))

        elif xp.loc[5, 'Lavagem simples'] == '' and xp.loc[5, 'Poli'] == '' and xp.loc[5, 'Vip'] == '':

            serv5 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))
        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] == 'X':

            serv6 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] == 'X' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[6, 'Lavagem simples'] == 'X' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] != 'x':

            serv6 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] != 'X':

            serv6 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] == 'X' and xp.loc[6, 'Vip'] != 'x':

            serv6 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] == 'X' and xp.loc[6, 'Vip'] != 'X':

            serv6 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] == 'X' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] != 'x':

            serv6 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] == 'X' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] != 'X':

            serv6 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] != 'x' and xp.loc[6, 'Vip'] != 'x':

            serv6 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] != 'X' and xp.loc[6, 'Vip'] != 'X':

            serv6 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[6, 'Lavagem simples'] == 'X' and xp.loc[6, 'Poli'] != 'x' and xp.loc[6, 'Vip'] != 'X':

            serv6 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[6, 'Lavagem simples'] == 'X' and xp.loc[6, 'Poli'] != 'X' and xp.loc[6, 'Vip'] != 'x':

            serv6 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] == 'X' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] == 'X' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] == 'X':

            serv6 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] == 'X':

            serv6 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] != 'x' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] != 'X' and xp.loc[6, 'Vip'] == 'X':

            serv6 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] != 'X' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] != 'x' and xp.loc[6, 'Vip'] == 'X':

            serv6 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] != 'X' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] != 'x' and xp.loc[6, 'Vip'] == 'X':

            serv6 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] != 'x':

            serv6 = ('{}'.format('POLIMENTO'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] == 'X' and xp.loc[6, 'Vip'] != 'X':

            serv6 = ('{}'.format('POLIMENTO'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] != 'X':

            serv6 = ('{}'.format('POLIMENTO'))

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] == 'X' and xp.loc[6, 'Vip'] != 'x':

            serv6 = ('{}'.format('POLIMENTO'))

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] != 'X':

            serv6 = ('{}'.format('POLIMENTO'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] == 'X' and xp.loc[6, 'Vip'] != 'x':

            serv6 = ('{}'.format('POLIMENTO'))

        elif xp.loc[6, 'Lavagem simples'] == '' and xp.loc[6, 'Poli'] == '' and xp.loc[6, 'Vip'] == '':

            serv6 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[7, 'Lavagem simples'] == 'x' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] == 'x':

            serv7 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[7, 'Lavagem simples'] == 'x' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] == 'X':

            serv7 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[7, 'Lavagem simples'] == 'x' and xp.loc[7, 'Poli'] == 'X' and xp.loc[7, 'Vip'] == 'x':

            serv7 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[7, 'Lavagem simples'] == 'X' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] == 'x':

            serv7 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[7, 'Lavagem simples'] == 'x' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] != 'x':

            serv7 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[7, 'Lavagem simples'] == 'x' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] != 'X':

            serv7 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[7, 'Lavagem simples'] == 'x' and xp.loc[7, 'Poli'] == 'X' and xp.loc[7, 'Vip'] != 'x':

            serv7 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[7, 'Lavagem simples'] == 'x' and xp.loc[7, 'Poli'] == 'X' and xp.loc[7, 'Vip'] != 'X':

            serv7 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[7, 'Lavagem simples'] == 'X' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] != 'x':

            serv7 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[7, 'Lavagem simples'] == 'X' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] != 'X':

            serv7 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[7, 'Lavagem simples'] == 'x' and xp.loc[7, 'Poli'] != 'x' and xp.loc[7, 'Vip'] != 'x':

            serv7 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[7, 'Lavagem simples'] == 'x' and xp.loc[7, 'Poli'] != 'X' and xp.loc[7, 'Vip'] != 'X':

            serv7 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[7, 'Lavagem simples'] == 'X' and xp.loc[7, 'Poli'] != 'x' and xp.loc[7, 'Vip'] != 'X':

            serv7 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[7, 'Lavagem simples'] == 'X' and xp.loc[7, 'Poli'] != 'X' and xp.loc[7, 'Vip'] != 'x':

            serv7 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[7, 'Lavagem simples'] != 'x' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] == 'x':

            serv7 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[7, 'Lavagem simples'] != 'X' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] == 'x':

            serv7 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[7, 'Lavagem simples'] != 'x' and xp.loc[7, 'Poli'] == 'X' and xp.loc[7, 'Vip'] == 'x':

            serv7 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[7, 'Lavagem simples'] != 'X' and xp.loc[7, 'Poli'] == 'X' and xp.loc[7, 'Vip'] == 'x':

            serv7 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[7, 'Lavagem simples'] != 'x' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] == 'X':

            serv7 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[7, 'Lavagem simples'] != 'X' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] == 'X':

            serv7 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[7, 'Lavagem simples'] != 'x' and xp.loc[7, 'Poli'] != 'x' and xp.loc[7, 'Vip'] == 'x':

            serv7 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[7, 'Lavagem simples'] != 'X' and xp.loc[7, 'Poli'] != 'X' and xp.loc[7, 'Vip'] == 'X':

            serv7 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[7, 'Lavagem simples'] != 'X' and xp.loc[7, 'Poli'] != 'X' and xp.loc[7, 'Vip'] == 'x':

            serv7 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[7, 'Lavagem simples'] != 'x' and xp.loc[7, 'Poli'] != 'x' and xp.loc[7, 'Vip'] == 'X':

            serv7 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[7, 'Lavagem simples'] != 'x' and xp.loc[7, 'Poli'] != 'X' and xp.loc[7, 'Vip'] == 'x':

            serv7 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[7, 'Lavagem simples'] != 'X' and xp.loc[7, 'Poli'] != 'x' and xp.loc[7, 'Vip'] == 'X':

            serv7 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[7, 'Lavagem simples'] != 'x' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] != 'x':

            serv7 = ('{}'.format('POLIMENTO'))

        elif xp.loc[7, 'Lavagem simples'] != 'X' and xp.loc[7, 'Poli'] == 'X' and xp.loc[7, 'Vip'] != 'X':

            serv7 = ('{}'.format('POLIMENTO'))

        elif xp.loc[7, 'Lavagem simples'] != 'X' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] != 'X':

            serv7 = ('{}'.format('POLIMENTO'))

        elif xp.loc[7, 'Lavagem simples'] != 'x' and xp.loc[7, 'Poli'] == 'X' and xp.loc[7, 'Vip'] != 'x':

            serv7 = ('{}'.format('POLIMENTO'))

        elif xp.loc[7, 'Lavagem simples'] != 'x' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] != 'X':

            serv7 = ('{}'.format('POLIMENTO'))

        elif xp.loc[7, 'Lavagem simples'] != 'X' and xp.loc[7, 'Poli'] == 'X' and xp.loc[7, 'Vip'] != 'x':

            serv7 = ('{}'.format('POLIMENTO'))

        elif xp.loc[7, 'Lavagem simples'] == '' and xp.loc[7, 'Poli'] == '' and xp.loc[7, 'Vip'] == '':

            serv7 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[8, 'Lavagem simples'] == 'x' and xp.loc[8, 'Poli'] == 'x' and xp.loc[8, 'Vip'] == 'x':

            serv8 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[8, 'Lavagem simples'] == 'x' and xp.loc[8, 'Poli'] == 'x' and xp.loc[8, 'Vip'] == 'X':

            serv8 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[8, 'Lavagem simples'] == 'x' and xp.loc[8, 'Poli'] == 'X' and xp.loc[8, 'Vip'] == 'x':

            serv8 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[8, 'Lavagem simples'] == 'X' and xp.loc[8, 'Poli'] == 'x' and xp.loc[8, 'Vip'] == 'x':

            serv8 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[8, 'Lavagem simples'] == 'x' and xp.loc[8, 'Poli'] == 'x' and xp.loc[8, 'Vip'] != 'x':

            serv8 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[8, 'Lavagem simples'] == 'x' and xp.loc[8, 'Poli'] == 'x' and xp.loc[8, 'Vip'] != 'X':

            serv8 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[8, 'Lavagem simples'] == 'x' and xp.loc[8, 'Poli'] == 'X' and xp.loc[8, 'Vip'] != 'x':

            serv8 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[8, 'Lavagem simples'] == 'x' and xp.loc[8, 'Poli'] == 'X' and xp.loc[8, 'Vip'] != 'X':

            serv8 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[8, 'Lavagem simples'] == 'X' and xp.loc[8, 'Poli'] == 'x' and xp.loc[8, 'Vip'] != 'x':

            serv8 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[8, 'Lavagem simples'] == 'X' and xp.loc[8, 'Poli'] == 'x' and xp.loc[8, 'Vip'] != 'X':

            serv8 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[8, 'Lavagem simples'] == 'x' and xp.loc[8, 'Poli'] != 'x' and xp.loc[8, 'Vip'] != 'x':

            serv8 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[8, 'Lavagem simples'] == 'x' and xp.loc[8, 'Poli'] != 'X' and xp.loc[8, 'Vip'] != 'X':

            serv8 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[8, 'Lavagem simples'] == 'X' and xp.loc[8, 'Poli'] != 'x' and xp.loc[8, 'Vip'] != 'X':

            serv8 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[8, 'Lavagem simples'] == 'X' and xp.loc[8, 'Poli'] != 'X' and xp.loc[8, 'Vip'] != 'x':

            serv8 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[8, 'Lavagem simples'] != 'x' and xp.loc[8, 'Poli'] == 'x' and xp.loc[8, 'Vip'] == 'x':

            serv8 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[8, 'Lavagem simples'] != 'X' and xp.loc[8, 'Poli'] == 'x' and xp.loc[8, 'Vip'] == 'x':

            serv8 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[8, 'Lavagem simples'] != 'x' and xp.loc[8, 'Poli'] == 'X' and xp.loc[8, 'Vip'] == 'x':

            serv8 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[8, 'Lavagem simples'] != 'X' and xp.loc[8, 'Poli'] == 'X' and xp.loc[8, 'Vip'] == 'x':

            serv8 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[8, 'Lavagem simples'] != 'x' and xp.loc[8, 'Poli'] == 'x' and xp.loc[8, 'Vip'] == 'X':

            serv8 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[8, 'Lavagem simples'] != 'X' and xp.loc[8, 'Poli'] == 'x' and xp.loc[8, 'Vip'] == 'X':

            serv8 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[8, 'Lavagem simples'] != 'x' and xp.loc[8, 'Poli'] != 'x' and xp.loc[8, 'Vip'] == 'x':

            serv8 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[8, 'Lavagem simples'] != 'X' and xp.loc[8, 'Poli'] != 'X' and xp.loc[8, 'Vip'] == 'X':

            serv8 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[8, 'Lavagem simples'] != 'X' and xp.loc[8, 'Poli'] != 'X' and xp.loc[8, 'Vip'] == 'x':

            serv8 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[8, 'Lavagem simples'] != 'x' and xp.loc[8, 'Poli'] != 'x' and xp.loc[8, 'Vip'] == 'X':

            serv8 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[8, 'Lavagem simples'] != 'x' and xp.loc[8, 'Poli'] != 'X' and xp.loc[8, 'Vip'] == 'x':

            serv8 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[8, 'Lavagem simples'] != 'X' and xp.loc[8, 'Poli'] != 'x' and xp.loc[8, 'Vip'] == 'X':

            serv8 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[8, 'Lavagem simples'] != 'x' and xp.loc[8, 'Poli'] == 'x' and xp.loc[8, 'Vip'] != 'x':

            serv8 = ('{}'.format('POLIMENTO'))

        elif xp.loc[8, 'Lavagem simples'] != 'X' and xp.loc[8, 'Poli'] == 'X' and xp.loc[8, 'Vip'] != 'X':

            serv8 = ('{}'.format('POLIMENTO'))

        elif xp.loc[8, 'Lavagem simples'] != 'X' and xp.loc[8, 'Poli'] == 'x' and xp.loc[8, 'Vip'] != 'X':

            serv8 = ('{}'.format('POLIMENTO'))

        elif xp.loc[8, 'Lavagem simples'] != 'x' and xp.loc[8, 'Poli'] == 'X' and xp.loc[8, 'Vip'] != 'x':

            serv8 = ('{}'.format('POLIMENTO'))

        elif xp.loc[8, 'Lavagem simples'] != 'x' and xp.loc[8, 'Poli'] == 'x' and xp.loc[8, 'Vip'] != 'X':

            serv8 = ('{}'.format('POLIMENTO'))

        elif xp.loc[8, 'Lavagem simples'] != 'X' and xp.loc[8, 'Poli'] == 'X' and xp.loc[8, 'Vip'] != 'x':

            serv8 = ('{}'.format('POLIMENTO'))

        elif xp.loc[8, 'Lavagem simples'] == '' and xp.loc[8, 'Poli'] == '' and xp.loc[8, 'Vip'] == '':

            serv8 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        r2 = '{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}'.format(x0, '', md02, '', vp1, '', serv0, x1, '',
    md05, '', vp2, '', serv1, x2, '', md06, '', vp3,'',serv2, x3,
    '', md07, '', vp4,'',serv3, x4, '', md08, '', vp5,'', serv4, x5, '',
      md09, '', vp6,'',serv5, x6, '', md10, '', vp7,'',serv6, x7, '',
     md11, '', vp8,'',serv7, x8, '', md12, '', vp9,'',serv8)

        return r2


func9()



def func10():
    import pandas as pd

    xp = pd.read_excel("carros da Jeep 1.xlsx")

    qtd_linhaspl = xp['Placa'].count()
    for ix in range((qtd_linhaspl - 1), -1, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x0 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 0, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x1 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 1, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x2 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 2, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x3 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 3, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x4 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 4, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x5 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 5, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x6 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 6, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x7 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 7, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x8 = '{}-{}'.format(inicio0, final0)


    for ix in range((qtd_linhaspl - 1), 8, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x9 = '{}-{}'.format(inicio0, final0)

        celula_m = xp.loc[0, 'Modelo']
        md02 = celula_m.upper()
        celula_m1 = xp.loc[1, 'Modelo']
        md05 = celula_m1.upper()
        celula_m2 = xp.loc[2, 'Modelo']
        md06 = celula_m2.upper()
        celula_m3 = xp.loc[3, 'Modelo']
        md07 = celula_m3.upper()
        celula_m4 = xp.loc[4, 'Modelo']
        md08 = celula_m4.upper()
        celula_m5 = xp.loc[5, 'Modelo']
        md09 = celula_m5.upper()
        celula_m6 = xp.loc[6, 'Modelo']
        md10 = celula_m6.upper()
        celula_m7 = xp.loc[7, 'Modelo']
        md11 = celula_m7.upper()
        celula_m8 = xp.loc[8, 'Modelo']
        md12 = celula_m8.upper()
        celula_m9 = xp.loc[9, 'Modelo']
        md13 = celula_m9.upper()

        celula_v = xp.loc[0, 'Valor']
        vp1 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[1, 'Valor']
        vp2 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[2, 'Valor']
        vp3 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[3, 'Valor']
        vp4 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[4, 'Valor']
        vp5 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[5, 'Valor']
        vp6 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[6, 'Valor']
        vp7 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[7, 'Valor']
        vp8 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[8, 'Valor']
        vp9 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[9, 'Valor']
        vp10 = '{} {}'.format('R$', float(celula_v))

        if xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[0, 'Lavagem simples'] == 'x' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[0, 'Lavagem simples'] == 'X' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] != 'X' and xp.loc[0, 'Vip'] == 'x':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] != 'x' and xp.loc[0, 'Vip'] == 'X':

            serv0 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'x' and xp.loc[0, 'Poli'] == 'x' and xp.loc[0, 'Vip'] != 'X':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] != 'X' and xp.loc[0, 'Poli'] == 'X' and xp.loc[0, 'Vip'] != 'x':

            serv0 = ('{}'.format('POLIMENTO'))

        elif xp.loc[0, 'Lavagem simples'] == '' and xp.loc[0, 'Poli'] == '' and xp.loc[0, 'Vip'] == '':

            serv0 = ('{}'.format('POLIMENTO'))

        #######################

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[1, 'Lavagem simples'] == 'x' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[1, 'Lavagem simples'] == 'X' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] != 'X' and xp.loc[1, 'Vip'] == 'x':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] != 'x' and xp.loc[1, 'Vip'] == 'X':

            serv1 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'x' and xp.loc[1, 'Poli'] == 'x' and xp.loc[1, 'Vip'] != 'X':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] != 'X' and xp.loc[1, 'Poli'] == 'X' and xp.loc[1, 'Vip'] != 'x':

            serv1 = ('{}'.format('POLIMENTO'))

        elif xp.loc[1, 'Lavagem simples'] == '' and xp.loc[1, 'Poli'] == '' and xp.loc[1, 'Vip'] == '':

            serv1 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        #########################

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[2, 'Lavagem simples'] == 'x' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[2, 'Lavagem simples'] == 'X' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] != 'X' and xp.loc[2, 'Vip'] == 'x':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] != 'x' and xp.loc[2, 'Vip'] == 'X':

            serv2 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'x' and xp.loc[2, 'Poli'] == 'x' and xp.loc[2, 'Vip'] != 'X':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] != 'X' and xp.loc[2, 'Poli'] == 'X' and xp.loc[2, 'Vip'] != 'x':

            serv2 = ('{}'.format('POLIMENTO'))

        elif xp.loc[2, 'Lavagem simples'] == '' and xp.loc[2, 'Poli'] == '' and xp.loc[2, 'Vip'] == '':

            serv2 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        ############################

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[3, 'Lavagem simples'] == 'x' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[3, 'Lavagem simples'] == 'X' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] != 'X' and xp.loc[3, 'Vip'] == 'x':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] != 'x' and xp.loc[3, 'Vip'] == 'X':

            serv3 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'x' and xp.loc[3, 'Poli'] == 'x' and xp.loc[3, 'Vip'] != 'X':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] != 'X' and xp.loc[3, 'Poli'] == 'X' and xp.loc[3, 'Vip'] != 'x':

            serv3 = ('{}'.format('POLIMENTO'))

        elif xp.loc[3, 'Lavagem simples'] == '' and xp.loc[3, 'Poli'] == '' and xp.loc[3, 'Vip'] == '':

            serv3 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))
        ##########################
        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[4, 'Lavagem simples'] == 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] == 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] == 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] != 'x' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[4, 'Lavagem simples'] == 'x' and xp.loc[4, 'Poli'] != 'X' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[4, 'Lavagem simples'] == 'X' and xp.loc[4, 'Poli'] != 'x' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[4, 'Lavagem simples'] == 'X' and xp.loc[4, 'Poli'] != 'X' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] != 'x' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] != 'X' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] != 'X' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] != 'x' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] != 'X' and xp.loc[4, 'Vip'] == 'x':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] != 'x' and xp.loc[4, 'Vip'] == 'X':

            serv4 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] != 'x' and xp.loc[4, 'Poli'] == 'x' and xp.loc[4, 'Vip'] != 'X':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] != 'X' and xp.loc[4, 'Poli'] == 'X' and xp.loc[4, 'Vip'] != 'x':

            serv4 = ('{}'.format('POLIMENTO'))

        elif xp.loc[4, 'Lavagem simples'] == '' and xp.loc[4, 'Poli'] == '' and xp.loc[4, 'Vip'] == '':

            serv4 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'X':

            serv5 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[5, 'Lavagem simples'] == 'X' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] == 'X' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] == 'X' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] != 'x' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[5, 'Lavagem simples'] == 'x' and xp.loc[5, 'Poli'] != 'X' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[5, 'Lavagem simples'] == 'X' and xp.loc[5, 'Poli'] != 'x' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[5, 'Lavagem simples'] == 'X' and xp.loc[5, 'Poli'] != 'X' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'X':

            serv5 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] == 'X':

            serv5 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] != 'x' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] != 'X' and xp.loc[5, 'Vip'] == 'X':

            serv5 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] != 'X' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] != 'x' and xp.loc[5, 'Vip'] == 'X':

            serv5 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] != 'X' and xp.loc[5, 'Vip'] == 'x':

            serv5 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] != 'x' and xp.loc[5, 'Vip'] == 'X':

            serv5 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}'.format('POLIMENTO'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}'.format('POLIMENTO'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}'.format('POLIMENTO'))

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}'.format('POLIMENTO'))

        elif xp.loc[5, 'Lavagem simples'] != 'x' and xp.loc[5, 'Poli'] == 'x' and xp.loc[5, 'Vip'] != 'X':

            serv5 = ('{}'.format('POLIMENTO'))

        elif xp.loc[5, 'Lavagem simples'] != 'X' and xp.loc[5, 'Poli'] == 'X' and xp.loc[5, 'Vip'] != 'x':

            serv5 = ('{}'.format('POLIMENTO'))

        elif xp.loc[5, 'Lavagem simples'] == '' and xp.loc[5, 'Poli'] == '' and xp.loc[5, 'Vip'] == '':

            serv5 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))
        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] == 'X':

            serv6 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] == 'X' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[6, 'Lavagem simples'] == 'X' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] != 'x':

            serv6 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] != 'X':

            serv6 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] == 'X' and xp.loc[6, 'Vip'] != 'x':

            serv6 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] == 'X' and xp.loc[6, 'Vip'] != 'X':

            serv6 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] == 'X' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] != 'x':

            serv6 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] == 'X' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] != 'X':

            serv6 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] != 'x' and xp.loc[6, 'Vip'] != 'x':

            serv6 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[6, 'Lavagem simples'] == 'x' and xp.loc[6, 'Poli'] != 'X' and xp.loc[6, 'Vip'] != 'X':

            serv6 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[6, 'Lavagem simples'] == 'X' and xp.loc[6, 'Poli'] != 'x' and xp.loc[6, 'Vip'] != 'X':

            serv6 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[6, 'Lavagem simples'] == 'X' and xp.loc[6, 'Poli'] != 'X' and xp.loc[6, 'Vip'] != 'x':

            serv6 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] == 'X' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] == 'X' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] == 'X':

            serv6 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] == 'X':

            serv6 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] != 'x' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] != 'X' and xp.loc[6, 'Vip'] == 'X':

            serv6 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] != 'X' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] != 'x' and xp.loc[6, 'Vip'] == 'X':

            serv6 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] != 'X' and xp.loc[6, 'Vip'] == 'x':

            serv6 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] != 'x' and xp.loc[6, 'Vip'] == 'X':

            serv6 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] != 'x':

            serv6 = ('{}'.format('POLIMENTO'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] == 'X' and xp.loc[6, 'Vip'] != 'X':

            serv6 = ('{}'.format('POLIMENTO'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] != 'X':

            serv6 = ('{}'.format('POLIMENTO'))

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] == 'X' and xp.loc[6, 'Vip'] != 'x':

            serv6 = ('{}'.format('POLIMENTO'))

        elif xp.loc[6, 'Lavagem simples'] != 'x' and xp.loc[6, 'Poli'] == 'x' and xp.loc[6, 'Vip'] != 'X':

            serv6 = ('{}'.format('POLIMENTO'))

        elif xp.loc[6, 'Lavagem simples'] != 'X' and xp.loc[6, 'Poli'] == 'X' and xp.loc[6, 'Vip'] != 'x':

            serv6 = ('{}'.format('POLIMENTO'))

        elif xp.loc[6, 'Lavagem simples'] == '' and xp.loc[6, 'Poli'] == '' and xp.loc[6, 'Vip'] == '':

            serv6 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[7, 'Lavagem simples'] == 'x' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] == 'x':

            serv7 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[7, 'Lavagem simples'] == 'x' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] == 'X':

            serv7 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[7, 'Lavagem simples'] == 'x' and xp.loc[7, 'Poli'] == 'X' and xp.loc[7, 'Vip'] == 'x':

            serv7 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[7, 'Lavagem simples'] == 'X' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] == 'x':

            serv7 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[7, 'Lavagem simples'] == 'x' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] != 'x':

            serv7 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[7, 'Lavagem simples'] == 'x' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] != 'X':

            serv7 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[7, 'Lavagem simples'] == 'x' and xp.loc[7, 'Poli'] == 'X' and xp.loc[7, 'Vip'] != 'x':

            serv7 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[7, 'Lavagem simples'] == 'x' and xp.loc[7, 'Poli'] == 'X' and xp.loc[7, 'Vip'] != 'X':

            serv7 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[7, 'Lavagem simples'] == 'X' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] != 'x':

            serv7 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[7, 'Lavagem simples'] == 'X' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] != 'X':

            serv7 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[7, 'Lavagem simples'] == 'x' and xp.loc[7, 'Poli'] != 'x' and xp.loc[7, 'Vip'] != 'x':

            serv7 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[7, 'Lavagem simples'] == 'x' and xp.loc[7, 'Poli'] != 'X' and xp.loc[7, 'Vip'] != 'X':

            serv7 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[7, 'Lavagem simples'] == 'X' and xp.loc[7, 'Poli'] != 'x' and xp.loc[7, 'Vip'] != 'X':

            serv7 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[7, 'Lavagem simples'] == 'X' and xp.loc[7, 'Poli'] != 'X' and xp.loc[7, 'Vip'] != 'x':

            serv7 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[7, 'Lavagem simples'] != 'x' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] == 'x':

            serv7 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[7, 'Lavagem simples'] != 'X' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] == 'x':

            serv7 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[7, 'Lavagem simples'] != 'x' and xp.loc[7, 'Poli'] == 'X' and xp.loc[7, 'Vip'] == 'x':

            serv7 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[7, 'Lavagem simples'] != 'X' and xp.loc[7, 'Poli'] == 'X' and xp.loc[7, 'Vip'] == 'x':

            serv7 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[7, 'Lavagem simples'] != 'x' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] == 'X':

            serv7 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[7, 'Lavagem simples'] != 'X' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] == 'X':

            serv7 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[7, 'Lavagem simples'] != 'x' and xp.loc[7, 'Poli'] != 'x' and xp.loc[7, 'Vip'] == 'x':

            serv7 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[7, 'Lavagem simples'] != 'X' and xp.loc[7, 'Poli'] != 'X' and xp.loc[7, 'Vip'] == 'X':

            serv7 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[7, 'Lavagem simples'] != 'X' and xp.loc[7, 'Poli'] != 'X' and xp.loc[7, 'Vip'] == 'x':

            serv7 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[7, 'Lavagem simples'] != 'x' and xp.loc[7, 'Poli'] != 'x' and xp.loc[7, 'Vip'] == 'X':

            serv7 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[7, 'Lavagem simples'] != 'x' and xp.loc[7, 'Poli'] != 'X' and xp.loc[7, 'Vip'] == 'x':

            serv7 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[7, 'Lavagem simples'] != 'X' and xp.loc[7, 'Poli'] != 'x' and xp.loc[7, 'Vip'] == 'X':

            serv7 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[7, 'Lavagem simples'] != 'x' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] != 'x':

            serv7 = ('{}'.format('POLIMENTO'))

        elif xp.loc[7, 'Lavagem simples'] != 'X' and xp.loc[7, 'Poli'] == 'X' and xp.loc[7, 'Vip'] != 'X':

            serv7 = ('{}'.format('POLIMENTO'))

        elif xp.loc[7, 'Lavagem simples'] != 'X' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] != 'X':

            serv7 = ('{}'.format('POLIMENTO'))

        elif xp.loc[7, 'Lavagem simples'] != 'x' and xp.loc[7, 'Poli'] == 'X' and xp.loc[7, 'Vip'] != 'x':

            serv7 = ('{}'.format('POLIMENTO'))

        elif xp.loc[7, 'Lavagem simples'] != 'x' and xp.loc[7, 'Poli'] == 'x' and xp.loc[7, 'Vip'] != 'X':

            serv7 = ('{}'.format('POLIMENTO'))

        elif xp.loc[7, 'Lavagem simples'] != 'X' and xp.loc[7, 'Poli'] == 'X' and xp.loc[7, 'Vip'] != 'x':

            serv7 = ('{}'.format('POLIMENTO'))

        elif xp.loc[7, 'Lavagem simples'] == '' and xp.loc[7, 'Poli'] == '' and xp.loc[7, 'Vip'] == '':

            serv7 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[8, 'Lavagem simples'] == 'x' and xp.loc[8, 'Poli'] == 'x' and xp.loc[8, 'Vip'] == 'x':

            serv8 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[8, 'Lavagem simples'] == 'x' and xp.loc[8, 'Poli'] == 'x' and xp.loc[8, 'Vip'] == 'X':

            serv8 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[8, 'Lavagem simples'] == 'x' and xp.loc[8, 'Poli'] == 'X' and xp.loc[8, 'Vip'] == 'x':

            serv8 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[8, 'Lavagem simples'] == 'X' and xp.loc[8, 'Poli'] == 'x' and xp.loc[8, 'Vip'] == 'x':

            serv8 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[8, 'Lavagem simples'] == 'x' and xp.loc[8, 'Poli'] == 'x' and xp.loc[8, 'Vip'] != 'x':

            serv8 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[8, 'Lavagem simples'] == 'x' and xp.loc[8, 'Poli'] == 'x' and xp.loc[8, 'Vip'] != 'X':

            serv8 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[8, 'Lavagem simples'] == 'x' and xp.loc[8, 'Poli'] == 'X' and xp.loc[8, 'Vip'] != 'x':

            serv8 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[8, 'Lavagem simples'] == 'x' and xp.loc[8, 'Poli'] == 'X' and xp.loc[8, 'Vip'] != 'X':

            serv8 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[8, 'Lavagem simples'] == 'X' and xp.loc[8, 'Poli'] == 'x' and xp.loc[8, 'Vip'] != 'x':

            serv8 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[8, 'Lavagem simples'] == 'X' and xp.loc[8, 'Poli'] == 'x' and xp.loc[8, 'Vip'] != 'X':

            serv8 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[8, 'Lavagem simples'] == 'x' and xp.loc[8, 'Poli'] != 'x' and xp.loc[8, 'Vip'] != 'x':

            serv8 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[8, 'Lavagem simples'] == 'x' and xp.loc[8, 'Poli'] != 'X' and xp.loc[8, 'Vip'] != 'X':

            serv8 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[8, 'Lavagem simples'] == 'X' and xp.loc[8, 'Poli'] != 'x' and xp.loc[8, 'Vip'] != 'X':

            serv8 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[8, 'Lavagem simples'] == 'X' and xp.loc[8, 'Poli'] != 'X' and xp.loc[8, 'Vip'] != 'x':

            serv8 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[8, 'Lavagem simples'] != 'x' and xp.loc[8, 'Poli'] == 'x' and xp.loc[8, 'Vip'] == 'x':

            serv8 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[8, 'Lavagem simples'] != 'X' and xp.loc[8, 'Poli'] == 'x' and xp.loc[8, 'Vip'] == 'x':

            serv8 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[8, 'Lavagem simples'] != 'x' and xp.loc[8, 'Poli'] == 'X' and xp.loc[8, 'Vip'] == 'x':

            serv8 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[8, 'Lavagem simples'] != 'X' and xp.loc[8, 'Poli'] == 'X' and xp.loc[8, 'Vip'] == 'x':

            serv8 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[8, 'Lavagem simples'] != 'x' and xp.loc[8, 'Poli'] == 'x' and xp.loc[8, 'Vip'] == 'X':

            serv8 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[8, 'Lavagem simples'] != 'X' and xp.loc[8, 'Poli'] == 'x' and xp.loc[8, 'Vip'] == 'X':

            serv8 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[8, 'Lavagem simples'] != 'x' and xp.loc[8, 'Poli'] != 'x' and xp.loc[8, 'Vip'] == 'x':

            serv8 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[8, 'Lavagem simples'] != 'X' and xp.loc[8, 'Poli'] != 'X' and xp.loc[8, 'Vip'] == 'X':

            serv8 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[8, 'Lavagem simples'] != 'X' and xp.loc[8, 'Poli'] != 'X' and xp.loc[8, 'Vip'] == 'x':

            serv8 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[8, 'Lavagem simples'] != 'x' and xp.loc[8, 'Poli'] != 'x' and xp.loc[8, 'Vip'] == 'X':

            serv8 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[8, 'Lavagem simples'] != 'x' and xp.loc[8, 'Poli'] != 'X' and xp.loc[8, 'Vip'] == 'x':

            serv8 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[8, 'Lavagem simples'] != 'X' and xp.loc[8, 'Poli'] != 'x' and xp.loc[8, 'Vip'] == 'X':

            serv8 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[8, 'Lavagem simples'] != 'x' and xp.loc[8, 'Poli'] == 'x' and xp.loc[8, 'Vip'] != 'x':

            serv8 = ('{}'.format('POLIMENTO'))

        elif xp.loc[8, 'Lavagem simples'] != 'X' and xp.loc[8, 'Poli'] == 'X' and xp.loc[8, 'Vip'] != 'X':

            serv8 = ('{}'.format('POLIMENTO'))

        elif xp.loc[8, 'Lavagem simples'] != 'X' and xp.loc[8, 'Poli'] == 'x' and xp.loc[8, 'Vip'] != 'X':

            serv8 = ('{}'.format('POLIMENTO'))

        elif xp.loc[8, 'Lavagem simples'] != 'x' and xp.loc[8, 'Poli'] == 'X' and xp.loc[8, 'Vip'] != 'x':

            serv8 = ('{}'.format('POLIMENTO'))

        elif xp.loc[8, 'Lavagem simples'] != 'x' and xp.loc[8, 'Poli'] == 'x' and xp.loc[8, 'Vip'] != 'X':

            serv8 = ('{}'.format('POLIMENTO'))

        elif xp.loc[8, 'Lavagem simples'] != 'X' and xp.loc[8, 'Poli'] == 'X' and xp.loc[8, 'Vip'] != 'x':

            serv8 = ('{}'.format('POLIMENTO'))

        elif xp.loc[8, 'Lavagem simples'] == '' and xp.loc[8, 'Poli'] == '' and xp.loc[8, 'Vip'] == '':

            serv8 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[9, 'Lavagem simples'] == 'x' and xp.loc[9, 'Poli'] == 'x' and xp.loc[9, 'Vip'] == 'x':

            serv9 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[9, 'Lavagem simples'] == 'x' and xp.loc[9, 'Poli'] == 'x' and xp.loc[9, 'Vip'] == 'X':

            serv9 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[9, 'Lavagem simples'] == 'x' and xp.loc[9, 'Poli'] == 'X' and xp.loc[9, 'Vip'] == 'x':

            serv9 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[9, 'Lavagem simples'] == 'X' and xp.loc[9, 'Poli'] == 'x' and xp.loc[9, 'Vip'] == 'x':

            serv9 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[9, 'Lavagem simples'] == 'x' and xp.loc[9, 'Poli'] == 'x' and xp.loc[9, 'Vip'] != 'x':

            serv9 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[9, 'Lavagem simples'] == 'x' and xp.loc[9, 'Poli'] == 'x' and xp.loc[9, 'Vip'] != 'X':

            serv9 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[9, 'Lavagem simples'] == 'x' and xp.loc[9, 'Poli'] == 'X' and xp.loc[9, 'Vip'] != 'x':

            serv9 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[9, 'Lavagem simples'] == 'x' and xp.loc[9, 'Poli'] == 'X' and xp.loc[9, 'Vip'] != 'X':

            serv9 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[9, 'Lavagem simples'] == 'X' and xp.loc[9, 'Poli'] == 'x' and xp.loc[9, 'Vip'] != 'x':

            serv9 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[9, 'Lavagem simples'] == 'X' and xp.loc[9, 'Poli'] == 'x' and xp.loc[9, 'Vip'] != 'X':

            serv9 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[9, 'Lavagem simples'] == 'x' and xp.loc[9, 'Poli'] != 'x' and xp.loc[9, 'Vip'] != 'x':

            serv9 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[9, 'Lavagem simples'] == 'x' and xp.loc[9, 'Poli'] != 'X' and xp.loc[9, 'Vip'] != 'X':

            serv9 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[9, 'Lavagem simples'] == 'X' and xp.loc[9, 'Poli'] != 'x' and xp.loc[9, 'Vip'] != 'X':

            serv9 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[9, 'Lavagem simples'] == 'X' and xp.loc[9, 'Poli'] != 'X' and xp.loc[9, 'Vip'] != 'x':

            serv9 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[9, 'Lavagem simples'] != 'x' and xp.loc[9, 'Poli'] == 'x' and xp.loc[9, 'Vip'] == 'x':

            serv9 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[9, 'Lavagem simples'] != 'X' and xp.loc[9, 'Poli'] == 'x' and xp.loc[9, 'Vip'] == 'x':

            serv9 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[9, 'Lavagem simples'] != 'x' and xp.loc[9, 'Poli'] == 'X' and xp.loc[9, 'Vip'] == 'x':

            serv9 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[9, 'Lavagem simples'] != 'X' and xp.loc[9, 'Poli'] == 'X' and xp.loc[9, 'Vip'] == 'x':

            serv9 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[9, 'Lavagem simples'] != 'x' and xp.loc[9, 'Poli'] == 'x' and xp.loc[9, 'Vip'] == 'X':

            serv9 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[9, 'Lavagem simples'] != 'X' and xp.loc[9, 'Poli'] == 'x' and xp.loc[9, 'Vip'] == 'X':

            serv9 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[9, 'Lavagem simples'] != 'x' and xp.loc[9, 'Poli'] != 'x' and xp.loc[9, 'Vip'] == 'x':

            serv9 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[9, 'Lavagem simples'] != 'X' and xp.loc[9, 'Poli'] != 'X' and xp.loc[9, 'Vip'] == 'X':

            serv9 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[9, 'Lavagem simples'] != 'X' and xp.loc[9, 'Poli'] != 'X' and xp.loc[9, 'Vip'] == 'x':

            serv9 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[9, 'Lavagem simples'] != 'x' and xp.loc[9, 'Poli'] != 'x' and xp.loc[9, 'Vip'] == 'X':

            serv9 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[9, 'Lavagem simples'] != 'x' and xp.loc[9, 'Poli'] != 'X' and xp.loc[9, 'Vip'] == 'x':

            serv9 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[9, 'Lavagem simples'] != 'X' and xp.loc[9, 'Poli'] != 'x' and xp.loc[9, 'Vip'] == 'X':

            serv9 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[9, 'Lavagem simples'] != 'x' and xp.loc[9, 'Poli'] == 'x' and xp.loc[9, 'Vip'] != 'x':

            serv9 = ('{}'.format('POLIMENTO'))

        elif xp.loc[9, 'Lavagem simples'] != 'X' and xp.loc[9, 'Poli'] == 'X' and xp.loc[9, 'Vip'] != 'X':

            serv9 = ('{}'.format('POLIMENTO'))

        elif xp.loc[9, 'Lavagem simples'] != 'X' and xp.loc[9, 'Poli'] == 'x' and xp.loc[9, 'Vip'] != 'X':

            serv9 = ('{}'.format('POLIMENTO'))

        elif xp.loc[9, 'Lavagem simples'] != 'x' and xp.loc[9, 'Poli'] == 'X' and xp.loc[9, 'Vip'] != 'x':

            serv9 = ('{}'.format('POLIMENTO'))

        elif xp.loc[9, 'Lavagem simples'] != 'x' and xp.loc[9, 'Poli'] == 'x' and xp.loc[9, 'Vip'] != 'X':

            serv9 = ('{}'.format('POLIMENTO'))

        elif xp.loc[9, 'Lavagem simples'] != 'X' and xp.loc[9, 'Poli'] == 'X' and xp.loc[9, 'Vip'] != 'x':

            serv9 = ('{}'.format('POLIMENTO'))

        elif xp.loc[9, 'Lavagem simples'] != 'x' and xp.loc[9, 'Poli'] != 'x' and xp.loc[9, 'Vip'] != 'x':

            serv9 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        r2 = '{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}'.format(x0, '', md02, '', vp1, '', serv0, x1, '',
    md05, '', vp2, '', serv1, x2, '', md06, '', vp3,'',serv2, x3, '', md07, '', vp4,'',serv3, x4, '', md08, '', vp5,'', serv4, x5, '',
      md09, '', vp6,'',serv5, x6, '', md10, '', vp7,'',serv6, x7, '', md11, '',
     vp8,'',serv7, x8, '', md12, '', vp9,'',serv8, x9, '', md13, '', vp10,'',serv9)


        return r2


func10()

