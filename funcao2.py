def func11():
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


    for ix in range((qtd_linhaspl - 1), 9, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x10 = '{}-{}'.format(inicio0, final0)

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
        celula_m10 = xp.loc[10, 'Modelo']
        md14 = celula_m10.upper()

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
        celula_v = xp.loc[10, 'Valor']
        vp11 = '{} {}'.format('R$', float(celula_v))

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

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] == '' and xp.loc[10, 'Poli'] == '' and xp.loc[10, 'Vip'] == '':

            serv10 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        r2 = '{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}'.format(x0, '', md02, '', vp1, '', serv0, x1, '',
    md05, '', vp2, '', serv1, x2, '', md06, '', vp3,'',serv2, x3, '', md07, '', vp4,'',serv3, x4, '', md08, '', vp5,'', serv4, x5, '',
      md09, '', vp6,'',serv5, x6, '', md10, '', vp7,'',serv6, x7, '', md11, '',
     vp8,'',serv7, x8, '', md12, '', vp9,'',serv8, x9, '', md13, '', vp10,'',serv9, x10, '', md14, '', vp11,'',serv10)

        return r2


func11()



def func12():
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


    for ix in range((qtd_linhaspl - 1), 9, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x10 = '{}-{}'.format(inicio0, final0)


    for ix in range((qtd_linhaspl - 1), 10, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x11 = '{}-{}'.format(inicio0, final0)

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
        celula_m10 = xp.loc[10, 'Modelo']
        md14 = celula_m10.upper()
        celula_m11 = xp.loc[11, 'Modelo']
        md15 = celula_m11.upper()

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
        celula_v = xp.loc[10, 'Valor']
        vp11 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[11, 'Valor']
        vp12 = '{} {}'.format('R$', float(celula_v))

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

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] == '' and xp.loc[10, 'Poli'] == '' and xp.loc[10, 'Vip'] == '':

            serv10 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] == '' and xp.loc[11, 'Poli'] == '' and xp.loc[11, 'Vip'] == '':

            serv11 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        r2 = '{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}'.format(x0, '', md02, '', vp1, '', serv0, x1, '',
    md05, '', vp2, '', serv1, x2, '', md06, '', vp3,'',serv2, x3, '', md07, '', vp4,'',serv3, x4, '', md08, '', vp5,'', serv4, x5, '',
      md09, '', vp6,'',serv5, x6, '', md10, '', vp7,'',serv6, x7, '', md11, '',
     vp8,'',serv7, x8, '', md12, '', vp9,'',serv8, x9, '', md13, '', vp10,'',serv9,
     x10, '', md14, '', vp11,'',serv10, x11, '', md15, '', vp12,'',serv11)


        return r2


func12()



def func13():
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

    for ix in range((qtd_linhaspl - 1), 9, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x10 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 10, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x11 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 11, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x12 = '{}-{}'.format(inicio0, final0)

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
        celula_m10 = xp.loc[10, 'Modelo']
        md14 = celula_m10.upper()
        celula_m11 = xp.loc[11, 'Modelo']
        md15 = celula_m11.upper()
        celula_m12 = xp.loc[12, 'Modelo']
        md16 = celula_m12.upper()

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
        celula_v = xp.loc[10, 'Valor']
        vp11 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[11, 'Valor']
        vp12 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[12, 'Valor']
        vp13 = '{} {}'.format('R$', float(celula_v))

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

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] == '' and xp.loc[10, 'Poli'] == '' and xp.loc[10, 'Vip'] == '':

            serv10 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] == '' and xp.loc[11, 'Poli'] == '' and xp.loc[11, 'Vip'] == '':

            serv11 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] == '' and xp.loc[12, 'Poli'] == '' and xp.loc[12, 'Vip'] == '':

            serv12 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        r2 = '{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}'.format(x0, '', md02, '', vp1, '', serv0, x1, '',
    md05, '', vp2, '', serv1, x2, '', md06, '', vp3,'',serv2, x3, '', md07, '', vp4,'',serv3, x4, '', md08, '', vp5,'', serv4, x5, '',
      md09, '', vp6,'',serv5, x6, '', md10, '', vp7,'',serv6, x7, '', md11, '',
     vp8,'',serv7, x8, '', md12, '', vp9,'',serv8, x9, '', md13, '', vp10,'',serv9,
     x10, '', md14, '', vp11,'',serv10, x11, '', md15, '', vp12,'',serv11, x12, '', md16, '', vp13,'',serv12)

        return r2


func13()


def func14():
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

    for ix in range((qtd_linhaspl - 1), 9, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x10 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 10, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x11 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 11, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x12 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 12, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x13 = '{}-{}'.format(inicio0, final0)

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
        celula_m10 = xp.loc[10, 'Modelo']
        md14 = celula_m10.upper()
        celula_m11 = xp.loc[11, 'Modelo']
        md15 = celula_m11.upper()
        celula_m12 = xp.loc[12, 'Modelo']
        md16 = celula_m12.upper()
        celula_m13 = xp.loc[13, 'Modelo']
        md17 = celula_m13.upper()

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
        celula_v = xp.loc[10, 'Valor']
        vp11 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[11, 'Valor']
        vp12 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[12, 'Valor']
        vp13 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[13, 'Valor']
        vp14 = '{} {}'.format('R$', float(celula_v))

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

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] == '' and xp.loc[10, 'Poli'] == '' and xp.loc[10, 'Vip'] == '':

            serv10 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] == '' and xp.loc[11, 'Poli'] == '' and xp.loc[11, 'Vip'] == '':

            serv11 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] == '' and xp.loc[12, 'Poli'] == '' and xp.loc[12, 'Vip'] == '':

            serv12 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] == '' and xp.loc[13, 'Poli'] == '' and xp.loc[13, 'Vip'] == '':

            serv13 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        r2 = '{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}'.format(x0, '', md02, '', vp1, '', serv0, x1, '',
    md05, '', vp2, '', serv1, x2, '', md06, '', vp3,'',serv2, x3, '', md07, '', vp4,'',serv3, x4, '', md08, '', vp5,'', serv4, x5, '',
      md09, '', vp6,'',serv5, x6, '', md10, '', vp7,'',serv6, x7, '', md11, '',
     vp8,'',serv7, x8, '', md12, '', vp9,'',serv8, x9, '', md13, '', vp10,'',serv9,
     x10, '', md14, '', vp11,'',serv10, x11, '', md15, '', vp12,'',serv11,
     x12, '', md16, '', vp13,'',serv12, x13, '', md17, '', vp14,'',serv13)


        return r2


func14()



def func15():
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

    for ix in range((qtd_linhaspl - 1), 9, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x10 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 10, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x11 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 11, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x12 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 12, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x13 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 13, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x14 = '{}-{}'.format(inicio0, final0)

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
        celula_m10 = xp.loc[10, 'Modelo']
        md14 = celula_m10.upper()
        celula_m11 = xp.loc[11, 'Modelo']
        md15 = celula_m11.upper()
        celula_m12 = xp.loc[12, 'Modelo']
        md16 = celula_m12.upper()
        celula_m13 = xp.loc[13, 'Modelo']
        md17 = celula_m13.upper()
        celula_m14 = xp.loc[14, 'Modelo']
        md18 = celula_m14.upper()

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
        celula_v = xp.loc[10, 'Valor']
        vp11 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[11, 'Valor']
        vp12 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[12, 'Valor']
        vp13 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[13, 'Valor']
        vp14 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[14, 'Valor']
        vp15 = '{} {}'.format('R$', float(celula_v))

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

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] == '' and xp.loc[10, 'Poli'] == '' and xp.loc[10, 'Vip'] == '':

            serv10 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] == '' and xp.loc[11, 'Poli'] == '' and xp.loc[11, 'Vip'] == '':

            serv11 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] == '' and xp.loc[12, 'Poli'] == '' and xp.loc[12, 'Vip'] == '':

            serv12 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] == '' and xp.loc[13, 'Poli'] == '' and xp.loc[13, 'Vip'] == '':

            serv13 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

            # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[14, 'Lavagem simples'] == 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] == 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] == 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] != 'x' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] != 'X' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[14, 'Lavagem simples'] == 'X' and xp.loc[14, 'Poli'] != 'x' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[14, 'Lavagem simples'] == 'X' and xp.loc[14, 'Poli'] != 'X' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] != 'x' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] != 'X' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] != 'X' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] != 'x' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] != 'X' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] != 'x' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] == '' and xp.loc[14, 'Poli'] == '' and xp.loc[14, 'Vip'] == '':

            serv14 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        r2 = '{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}'.format(x0, '', md02, '', vp1, '', serv0, x1, '',
    md05, '', vp2, '', serv1, x2, '', md06, '', vp3,'',serv2, x3, '', md07, '', vp4,'',serv3, x4, '', md08, '', vp5,'', serv4, x5, '',
      md09, '', vp6,'',serv5, x6, '', md10, '', vp7,'',serv6, x7, '', md11, '',
     vp8,'',serv7, x8, '', md12, '', vp9,'',serv8, x9, '', md13, '', vp10,'',serv9,
     x10, '', md14, '', vp11,'',serv10, x11, '', md15, '', vp12,'',serv11,
     x12, '', md16, '', vp13,'',serv12, x13, '', md17, '', vp14,'',serv13, x14, '', md18, '', vp15,'',serv14)

        return r2


func15()



def func16():
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

    for ix in range((qtd_linhaspl - 1), 9, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x10 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 10, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x11 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 11, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x12 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 12, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x13 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 13, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x14 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 14, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x15 = '{}-{}'.format(inicio0, final0)

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
        celula_m10 = xp.loc[10, 'Modelo']
        md14 = celula_m10.upper()
        celula_m11 = xp.loc[11, 'Modelo']
        md15 = celula_m11.upper()
        celula_m12 = xp.loc[12, 'Modelo']
        md16 = celula_m12.upper()
        celula_m13 = xp.loc[13, 'Modelo']
        md17 = celula_m13.upper()
        celula_m14 = xp.loc[14, 'Modelo']
        md18 = celula_m14.upper()
        celula_m15 = xp.loc[15, 'Modelo']
        md19 = celula_m15.upper()

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
        celula_v = xp.loc[10, 'Valor']
        vp11 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[11, 'Valor']
        vp12 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[12, 'Valor']
        vp13 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[13, 'Valor']
        vp14 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[14, 'Valor']
        vp15 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[15, 'Valor']
        vp16 = '{} {}'.format('R$', float(celula_v))

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

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] == '' and xp.loc[10, 'Poli'] == '' and xp.loc[10, 'Vip'] == '':

            serv10 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] == '' and xp.loc[11, 'Poli'] == '' and xp.loc[11, 'Vip'] == '':

            serv11 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] == '' and xp.loc[12, 'Poli'] == '' and xp.loc[12, 'Vip'] == '':

            serv12 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] == '' and xp.loc[13, 'Poli'] == '' and xp.loc[13, 'Vip'] == '':

            serv13 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

            # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[14, 'Lavagem simples'] == 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] == 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] == 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] != 'x' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] != 'X' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[14, 'Lavagem simples'] == 'X' and xp.loc[14, 'Poli'] != 'x' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[14, 'Lavagem simples'] == 'X' and xp.loc[14, 'Poli'] != 'X' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] != 'x' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] != 'X' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] != 'X' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] != 'x' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] != 'X' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] != 'x' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] == '' and xp.loc[14, 'Poli'] == '' and xp.loc[14, 'Vip'] == '':

            serv14 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))
            # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'X':

            serv15 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[15, 'Lavagem simples'] == 'X' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] == 'X' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] == 'X' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] != 'x' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] != 'X' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[15, 'Lavagem simples'] == 'X' and xp.loc[15, 'Poli'] != 'x' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[15, 'Lavagem simples'] == 'X' and xp.loc[15, 'Poli'] != 'X' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'X':

            serv15 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'X':

            serv15 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] != 'x' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] != 'X' and xp.loc[15, 'Vip'] == 'X':

            serv15 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] != 'X' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] != 'x' and xp.loc[15, 'Vip'] == 'X':

            serv15 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] != 'X' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] != 'x' and xp.loc[15, 'Vip'] == 'X':

            serv15 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}'.format('POLIMENTO'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}'.format('POLIMENTO'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}'.format('POLIMENTO'))

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}'.format('POLIMENTO'))

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}'.format('POLIMENTO'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}'.format('POLIMENTO'))

        elif xp.loc[15, 'Lavagem simples'] == '' and xp.loc[15, 'Poli'] == '' and xp.loc[15, 'Vip'] == '':

            serv15 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        r2 = '{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}'.format(x0, '', md02, '', vp1, '', serv0, x1, '',
    md05, '', vp2, '', serv1, x2, '', md06, '', vp3,'',serv2, x3, '', md07, '', vp4,'',serv3, x4, '', md08, '', vp5,'', serv4, x5, '',
      md09, '', vp6,'',serv5, x6, '', md10, '', vp7,'',serv6, x7, '', md11, '',
     vp8,'',serv7, x8, '', md12, '', vp9,'',serv8, x9, '', md13, '', vp10,'',serv9,
     x10, '', md14, '', vp11,'',serv10, x11, '', md15, '', vp12,'',serv11,
     x12, '', md16, '', vp13,'',serv12, x13, '', md17, '', vp14,'',serv13, x14, '',
     md18, '', vp15,'',serv14, x15, '', md19, '', vp16,'',serv15)


        return r2


func16()


def func17():
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

    for ix in range((qtd_linhaspl - 1), 9, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x10 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 10, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x11 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 11, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x12 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 12, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x13 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 13, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x14 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 14, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x15 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 15, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x16 = '{}-{}'.format(inicio0, final0)

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
        celula_m10 = xp.loc[10, 'Modelo']
        md14 = celula_m10.upper()
        celula_m11 = xp.loc[11, 'Modelo']
        md15 = celula_m11.upper()
        celula_m12 = xp.loc[12, 'Modelo']
        md16 = celula_m12.upper()
        celula_m13 = xp.loc[13, 'Modelo']
        md17 = celula_m13.upper()
        celula_m14 = xp.loc[14, 'Modelo']
        md18 = celula_m14.upper()
        celula_m15 = xp.loc[15, 'Modelo']
        md19 = celula_m15.upper()
        celula_m16 = xp.loc[16, 'Modelo']
        md20 = celula_m16.upper()

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
        celula_v = xp.loc[10, 'Valor']
        vp11 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[11, 'Valor']
        vp12 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[12, 'Valor']
        vp13 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[13, 'Valor']
        vp14 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[14, 'Valor']
        vp15 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[15, 'Valor']
        vp16 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[16, 'Valor']
        vp17 = '{} {}'.format('R$', float(celula_v))

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

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] == '' and xp.loc[10, 'Poli'] == '' and xp.loc[10, 'Vip'] == '':

            serv10 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] == '' and xp.loc[11, 'Poli'] == '' and xp.loc[11, 'Vip'] == '':

            serv11 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] == '' and xp.loc[12, 'Poli'] == '' and xp.loc[12, 'Vip'] == '':

            serv12 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] == '' and xp.loc[13, 'Poli'] == '' and xp.loc[13, 'Vip'] == '':

            serv13 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

            # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[14, 'Lavagem simples'] == 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] == 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] == 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] != 'x' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] != 'X' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[14, 'Lavagem simples'] == 'X' and xp.loc[14, 'Poli'] != 'x' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[14, 'Lavagem simples'] == 'X' and xp.loc[14, 'Poli'] != 'X' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] != 'x' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] != 'X' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] != 'X' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] != 'x' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] != 'X' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] != 'x' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] == '' and xp.loc[14, 'Poli'] == '' and xp.loc[14, 'Vip'] == '':

            serv14 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))
            # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'X':

            serv15 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[15, 'Lavagem simples'] == 'X' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] == 'X' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] == 'X' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] != 'x' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] != 'X' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[15, 'Lavagem simples'] == 'X' and xp.loc[15, 'Poli'] != 'x' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[15, 'Lavagem simples'] == 'X' and xp.loc[15, 'Poli'] != 'X' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'X':

            serv15 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'X':

            serv15 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] != 'x' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] != 'X' and xp.loc[15, 'Vip'] == 'X':

            serv15 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] != 'X' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] != 'x' and xp.loc[15, 'Vip'] == 'X':

            serv15 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] != 'X' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] != 'x' and xp.loc[15, 'Vip'] == 'X':

            serv15 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}'.format('POLIMENTO'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}'.format('POLIMENTO'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}'.format('POLIMENTO'))

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}'.format('POLIMENTO'))

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}'.format('POLIMENTO'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}'.format('POLIMENTO'))

        elif xp.loc[15, 'Lavagem simples'] == '' and xp.loc[15, 'Poli'] == '' and xp.loc[15, 'Vip'] == '':

            serv15 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

            # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] == 'X':

            serv16 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] == 'X' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[16, 'Lavagem simples'] == 'X' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] != 'x':

            serv16 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] != 'X':

            serv16 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] == 'X' and xp.loc[16, 'Vip'] != 'x':

            serv16 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] == 'X' and xp.loc[16, 'Vip'] != 'X':

            serv16 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] == 'X' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] != 'x':

            serv16 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] == 'X' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] != 'X':

            serv16 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] != 'x' and xp.loc[16, 'Vip'] != 'x':

            serv16 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] != 'X' and xp.loc[16, 'Vip'] != 'X':

            serv16 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[16, 'Lavagem simples'] == 'X' and xp.loc[16, 'Poli'] != 'x' and xp.loc[16, 'Vip'] != 'X':

            serv16 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[16, 'Lavagem simples'] == 'X' and xp.loc[16, 'Poli'] != 'X' and xp.loc[16, 'Vip'] != 'x':

            serv16 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] == 'X' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] == 'X' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] == 'X':

            serv16 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] == 'X':

            serv16 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] != 'x' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] != 'X' and xp.loc[16, 'Vip'] == 'X':

            serv16 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] != 'X' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] != 'x' and xp.loc[16, 'Vip'] == 'X':

            serv16 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] != 'X' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] != 'x' and xp.loc[16, 'Vip'] == 'X':

            serv16 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] != 'x':

            serv16 = ('{}'.format('POLIMENTO'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] == 'X' and xp.loc[16, 'Vip'] != 'X':

            serv16 = ('{}'.format('POLIMENTO'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] != 'X':

            serv16 = ('{}'.format('POLIMENTO'))

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] == 'X' and xp.loc[16, 'Vip'] != 'x':

            serv16 = ('{}'.format('POLIMENTO'))

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] != 'X':

            serv16 = ('{}'.format('POLIMENTO'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] == 'X' and xp.loc[16, 'Vip'] != 'x':

            serv16 = ('{}'.format('POLIMENTO'))

        elif xp.loc[16, 'Lavagem simples'] == '' and xp.loc[16, 'Poli'] == '' and xp.loc[16, 'Vip'] == '':

            serv16 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        r2 = '{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}'.format(x0, '', md02, '', vp1, '', serv0, x1, '',
    md05, '', vp2, '', serv1, x2, '', md06, '', vp3,'',serv2, x3, '', md07, '', vp4,'',serv3, x4, '', md08, '', vp5,'', serv4, x5, '',
      md09, '', vp6,'',serv5, x6, '', md10, '', vp7,'',serv6, x7, '', md11, '',
     vp8,'',serv7, x8, '', md12, '', vp9,'',serv8, x9, '', md13, '', vp10,'',serv9,
     x10, '', md14, '', vp11,'',serv10, x11, '', md15, '', vp12,'',serv11,
     x12, '', md16, '', vp13,'',serv12, x13, '', md17, '', vp14,'',serv13, x14, '',
     md18, '', vp15,'',serv14, x15, '', md19, '', vp16,'',serv15, x16, '', md20, '', vp17,'',serv16)


        return r2


func17()


def func18():
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

    for ix in range((qtd_linhaspl - 1), 9, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x10 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 10, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x11 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 11, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x12 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 12, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x13 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 13, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x14 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 14, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x15 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 15, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x16 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 16, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x17 = '{}-{}'.format(inicio0, final0)

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
        celula_m10 = xp.loc[10, 'Modelo']
        md14 = celula_m10.upper()
        celula_m11 = xp.loc[11, 'Modelo']
        md15 = celula_m11.upper()
        celula_m12 = xp.loc[12, 'Modelo']
        md16 = celula_m12.upper()
        celula_m13 = xp.loc[13, 'Modelo']
        md17 = celula_m13.upper()
        celula_m14 = xp.loc[14, 'Modelo']
        md18 = celula_m14.upper()
        celula_m15 = xp.loc[15, 'Modelo']
        md19 = celula_m15.upper()
        celula_m16 = xp.loc[16, 'Modelo']
        md20 = celula_m16.upper()
        celula_m17 = xp.loc[17, 'Modelo']
        md21 = celula_m17.upper()

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
        celula_v = xp.loc[10, 'Valor']
        vp11 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[11, 'Valor']
        vp12 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[12, 'Valor']
        vp13 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[13, 'Valor']
        vp14 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[14, 'Valor']
        vp15 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[15, 'Valor']
        vp16 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[16, 'Valor']
        vp17 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[17, 'Valor']
        vp18 = '{} {}'.format('R$', float(celula_v))

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

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] == '' and xp.loc[10, 'Poli'] == '' and xp.loc[10, 'Vip'] == '':

            serv10 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] == '' and xp.loc[11, 'Poli'] == '' and xp.loc[11, 'Vip'] == '':

            serv11 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] == '' and xp.loc[12, 'Poli'] == '' and xp.loc[12, 'Vip'] == '':

            serv12 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] == '' and xp.loc[13, 'Poli'] == '' and xp.loc[13, 'Vip'] == '':

            serv13 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

            # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[14, 'Lavagem simples'] == 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] == 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] == 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] != 'x' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] != 'X' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[14, 'Lavagem simples'] == 'X' and xp.loc[14, 'Poli'] != 'x' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[14, 'Lavagem simples'] == 'X' and xp.loc[14, 'Poli'] != 'X' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] != 'x' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] != 'X' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] != 'X' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] != 'x' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] != 'X' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] != 'x' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] == '' and xp.loc[14, 'Poli'] == '' and xp.loc[14, 'Vip'] == '':

            serv14 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))
            # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'X':

            serv15 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[15, 'Lavagem simples'] == 'X' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] == 'X' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] == 'X' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] != 'x' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] != 'X' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[15, 'Lavagem simples'] == 'X' and xp.loc[15, 'Poli'] != 'x' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[15, 'Lavagem simples'] == 'X' and xp.loc[15, 'Poli'] != 'X' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'X':

            serv15 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'X':

            serv15 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] != 'x' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] != 'X' and xp.loc[15, 'Vip'] == 'X':

            serv15 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] != 'X' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] != 'x' and xp.loc[15, 'Vip'] == 'X':

            serv15 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] != 'X' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] != 'x' and xp.loc[15, 'Vip'] == 'X':

            serv15 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}'.format('POLIMENTO'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}'.format('POLIMENTO'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}'.format('POLIMENTO'))

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}'.format('POLIMENTO'))

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}'.format('POLIMENTO'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}'.format('POLIMENTO'))

        elif xp.loc[15, 'Lavagem simples'] == '' and xp.loc[15, 'Poli'] == '' and xp.loc[15, 'Vip'] == '':

            serv15 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

            # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] == 'X':

            serv16 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] == 'X' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[16, 'Lavagem simples'] == 'X' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] != 'x':

            serv16 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] != 'X':

            serv16 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] == 'X' and xp.loc[16, 'Vip'] != 'x':

            serv16 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] == 'X' and xp.loc[16, 'Vip'] != 'X':

            serv16 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] == 'X' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] != 'x':

            serv16 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] == 'X' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] != 'X':

            serv16 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] != 'x' and xp.loc[16, 'Vip'] != 'x':

            serv16 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] != 'X' and xp.loc[16, 'Vip'] != 'X':

            serv16 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[16, 'Lavagem simples'] == 'X' and xp.loc[16, 'Poli'] != 'x' and xp.loc[16, 'Vip'] != 'X':

            serv16 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[16, 'Lavagem simples'] == 'X' and xp.loc[16, 'Poli'] != 'X' and xp.loc[16, 'Vip'] != 'x':

            serv16 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] == 'X' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] == 'X' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] == 'X':

            serv16 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] == 'X':

            serv16 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] != 'x' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] != 'X' and xp.loc[16, 'Vip'] == 'X':

            serv16 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] != 'X' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] != 'x' and xp.loc[16, 'Vip'] == 'X':

            serv16 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] != 'X' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] != 'x' and xp.loc[16, 'Vip'] == 'X':

            serv16 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] != 'x':

            serv16 = ('{}'.format('POLIMENTO'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] == 'X' and xp.loc[16, 'Vip'] != 'X':

            serv16 = ('{}'.format('POLIMENTO'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] != 'X':

            serv16 = ('{}'.format('POLIMENTO'))

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] == 'X' and xp.loc[16, 'Vip'] != 'x':

            serv16 = ('{}'.format('POLIMENTO'))

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] != 'X':

            serv16 = ('{}'.format('POLIMENTO'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] == 'X' and xp.loc[16, 'Vip'] != 'x':

            serv16 = ('{}'.format('POLIMENTO'))

        elif xp.loc[16, 'Lavagem simples'] == '' and xp.loc[16, 'Poli'] == '' and xp.loc[16, 'Vip'] == '':

            serv16 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

            # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[17, 'Lavagem simples'] == 'x' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] == 'x':

            serv17 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[17, 'Lavagem simples'] == 'x' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] == 'X':

            serv17 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[17, 'Lavagem simples'] == 'x' and xp.loc[17, 'Poli'] == 'X' and xp.loc[17, 'Vip'] == 'x':

            serv17 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[17, 'Lavagem simples'] == 'X' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] == 'x':

            serv17 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[17, 'Lavagem simples'] == 'x' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] != 'x':

            serv17 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[17, 'Lavagem simples'] == 'x' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] != 'X':

            serv17 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[17, 'Lavagem simples'] == 'x' and xp.loc[17, 'Poli'] == 'X' and xp.loc[17, 'Vip'] != 'x':

            serv17 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[17, 'Lavagem simples'] == 'x' and xp.loc[17, 'Poli'] == 'X' and xp.loc[17, 'Vip'] != 'X':

            serv17 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[17, 'Lavagem simples'] == 'X' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] != 'x':

            serv17 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[17, 'Lavagem simples'] == 'X' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] != 'X':

            serv17 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[17, 'Lavagem simples'] == 'x' and xp.loc[17, 'Poli'] != 'x' and xp.loc[17, 'Vip'] != 'x':

            serv17 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[17, 'Lavagem simples'] == 'x' and xp.loc[17, 'Poli'] != 'X' and xp.loc[17, 'Vip'] != 'X':

            serv17 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[17, 'Lavagem simples'] == 'X' and xp.loc[17, 'Poli'] != 'x' and xp.loc[17, 'Vip'] != 'X':

            serv17 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[17, 'Lavagem simples'] == 'X' and xp.loc[17, 'Poli'] != 'X' and xp.loc[17, 'Vip'] != 'x':

            serv17 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[17, 'Lavagem simples'] != 'x' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] == 'x':

            serv17 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[17, 'Lavagem simples'] != 'X' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] == 'x':

            serv17 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[17, 'Lavagem simples'] != 'x' and xp.loc[17, 'Poli'] == 'X' and xp.loc[17, 'Vip'] == 'x':

            serv17 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[17, 'Lavagem simples'] != 'X' and xp.loc[17, 'Poli'] == 'X' and xp.loc[17, 'Vip'] == 'x':

            serv17 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[17, 'Lavagem simples'] != 'x' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] == 'X':

            serv17 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[17, 'Lavagem simples'] != 'X' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] == 'X':

            serv17 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[17, 'Lavagem simples'] != 'x' and xp.loc[17, 'Poli'] != 'x' and xp.loc[17, 'Vip'] == 'x':

            serv17 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[17, 'Lavagem simples'] != 'X' and xp.loc[17, 'Poli'] != 'X' and xp.loc[17, 'Vip'] == 'X':

            serv17 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[17, 'Lavagem simples'] != 'X' and xp.loc[17, 'Poli'] != 'X' and xp.loc[17, 'Vip'] == 'x':

            serv17 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[17, 'Lavagem simples'] != 'x' and xp.loc[17, 'Poli'] != 'x' and xp.loc[17, 'Vip'] == 'X':

            serv17 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[17, 'Lavagem simples'] != 'x' and xp.loc[17, 'Poli'] != 'X' and xp.loc[17, 'Vip'] == 'x':

            serv17 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[17, 'Lavagem simples'] != 'X' and xp.loc[17, 'Poli'] != 'x' and xp.loc[17, 'Vip'] == 'X':

            serv17 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[17, 'Lavagem simples'] != 'x' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] != 'x':

            serv17 = ('{}'.format('POLIMENTO'))

        elif xp.loc[17, 'Lavagem simples'] != 'X' and xp.loc[17, 'Poli'] == 'X' and xp.loc[17, 'Vip'] != 'X':

            serv17 = ('{}'.format('POLIMENTO'))

        elif xp.loc[17, 'Lavagem simples'] != 'X' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] != 'X':

            serv17 = ('{}'.format('POLIMENTO'))

        elif xp.loc[17, 'Lavagem simples'] != 'x' and xp.loc[17, 'Poli'] == 'X' and xp.loc[17, 'Vip'] != 'x':

            serv17 = ('{}'.format('POLIMENTO'))

        elif xp.loc[17, 'Lavagem simples'] != 'x' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] != 'X':

            serv17 = ('{}'.format('POLIMENTO'))

        elif xp.loc[17, 'Lavagem simples'] != 'X' and xp.loc[17, 'Poli'] == 'X' and xp.loc[17, 'Vip'] != 'x':

            serv17 = ('{}'.format('POLIMENTO'))

        elif xp.loc[17, 'Lavagem simples'] == '' and xp.loc[17, 'Poli'] == '' and xp.loc[17, 'Vip'] == '':

            serv17 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        r2 = '{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}'.format(x0, '', md02, '', vp1, '', serv0, x1, '',
    md05, '', vp2, '', serv1, x2, '', md06, '', vp3,'',serv2, x3, '', md07, '', vp4,'',serv3, x4, '', md08, '', vp5,'', serv4, x5, '',
      md09, '', vp6,'',serv5, x6, '', md10, '', vp7,'',serv6, x7, '', md11, '',
     vp8,'',serv7, x8, '', md12, '', vp9,'',serv8, x9, '', md13, '', vp10,'',serv9,
     x10, '', md14, '', vp11,'',serv10, x11, '', md15, '', vp12,'',serv11,
     x12, '', md16, '', vp13,'',serv12, x13, '', md17, '', vp14,'',serv13, x14, '',
     md18, '', vp15,'',serv14, x15, '', md19, '', vp16,'',serv15, x16, '', md20, '',
     vp17,'',serv16, x17, '', md21, '', vp18,'',serv17)

        return r2


func18()


def func19():
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

    for ix in range((qtd_linhaspl - 1), 9, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x10 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 10, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x11 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 11, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x12 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 12, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x13 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 13, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x14 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 14, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x15 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 15, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x16 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 16, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x17 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 17, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x18 = '{}-{}'.format(inicio0, final0)

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
        celula_m10 = xp.loc[10, 'Modelo']
        md14 = celula_m10.upper()
        celula_m11 = xp.loc[11, 'Modelo']
        md15 = celula_m11.upper()
        celula_m12 = xp.loc[12, 'Modelo']
        md16 = celula_m12.upper()
        celula_m13 = xp.loc[13, 'Modelo']
        md17 = celula_m13.upper()
        celula_m14 = xp.loc[14, 'Modelo']
        md18 = celula_m14.upper()
        celula_m15 = xp.loc[15, 'Modelo']
        md19 = celula_m15.upper()
        celula_m16 = xp.loc[16, 'Modelo']
        md20 = celula_m16.upper()
        celula_m17 = xp.loc[17, 'Modelo']
        md21 = celula_m17.upper()
        celula_m18 = xp.loc[18, 'Modelo']
        md22 = celula_m18.upper()

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
        celula_v = xp.loc[10, 'Valor']
        vp11 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[11, 'Valor']
        vp12 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[12, 'Valor']
        vp13 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[13, 'Valor']
        vp14 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[14, 'Valor']
        vp15 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[15, 'Valor']
        vp16 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[16, 'Valor']
        vp17 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[17, 'Valor']
        vp18 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[18, 'Valor']
        vp19 = '{} {}'.format('R$', float(celula_v))

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

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] == '' and xp.loc[10, 'Poli'] == '' and xp.loc[10, 'Vip'] == '':

            serv10 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] == '' and xp.loc[11, 'Poli'] == '' and xp.loc[11, 'Vip'] == '':

            serv11 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] == '' and xp.loc[12, 'Poli'] == '' and xp.loc[12, 'Vip'] == '':

            serv12 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] == '' and xp.loc[13, 'Poli'] == '' and xp.loc[13, 'Vip'] == '':

            serv13 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

            # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[14, 'Lavagem simples'] == 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] == 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] == 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] != 'x' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] != 'X' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[14, 'Lavagem simples'] == 'X' and xp.loc[14, 'Poli'] != 'x' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[14, 'Lavagem simples'] == 'X' and xp.loc[14, 'Poli'] != 'X' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] != 'x' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] != 'X' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] != 'X' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] != 'x' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] != 'X' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] != 'x' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] == '' and xp.loc[14, 'Poli'] == '' and xp.loc[14, 'Vip'] == '':

            serv14 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))
            # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'X':

            serv15 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[15, 'Lavagem simples'] == 'X' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] == 'X' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] == 'X' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] != 'x' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] != 'X' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[15, 'Lavagem simples'] == 'X' and xp.loc[15, 'Poli'] != 'x' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[15, 'Lavagem simples'] == 'X' and xp.loc[15, 'Poli'] != 'X' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'X':

            serv15 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'X':

            serv15 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] != 'x' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] != 'X' and xp.loc[15, 'Vip'] == 'X':

            serv15 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] != 'X' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] != 'x' and xp.loc[15, 'Vip'] == 'X':

            serv15 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] != 'X' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] != 'x' and xp.loc[15, 'Vip'] == 'X':

            serv15 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}'.format('POLIMENTO'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}'.format('POLIMENTO'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}'.format('POLIMENTO'))

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}'.format('POLIMENTO'))

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}'.format('POLIMENTO'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}'.format('POLIMENTO'))

        elif xp.loc[15, 'Lavagem simples'] == '' and xp.loc[15, 'Poli'] == '' and xp.loc[15, 'Vip'] == '':

            serv15 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

            # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] == 'X':

            serv16 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] == 'X' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[16, 'Lavagem simples'] == 'X' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] != 'x':

            serv16 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] != 'X':

            serv16 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] == 'X' and xp.loc[16, 'Vip'] != 'x':

            serv16 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] == 'X' and xp.loc[16, 'Vip'] != 'X':

            serv16 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] == 'X' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] != 'x':

            serv16 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] == 'X' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] != 'X':

            serv16 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] != 'x' and xp.loc[16, 'Vip'] != 'x':

            serv16 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] != 'X' and xp.loc[16, 'Vip'] != 'X':

            serv16 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[16, 'Lavagem simples'] == 'X' and xp.loc[16, 'Poli'] != 'x' and xp.loc[16, 'Vip'] != 'X':

            serv16 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[16, 'Lavagem simples'] == 'X' and xp.loc[16, 'Poli'] != 'X' and xp.loc[16, 'Vip'] != 'x':

            serv16 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] == 'X' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] == 'X' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] == 'X':

            serv16 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] == 'X':

            serv16 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] != 'x' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] != 'X' and xp.loc[16, 'Vip'] == 'X':

            serv16 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] != 'X' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] != 'x' and xp.loc[16, 'Vip'] == 'X':

            serv16 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] != 'X' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] != 'x' and xp.loc[16, 'Vip'] == 'X':

            serv16 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] != 'x':

            serv16 = ('{}'.format('POLIMENTO'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] == 'X' and xp.loc[16, 'Vip'] != 'X':

            serv16 = ('{}'.format('POLIMENTO'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] != 'X':

            serv16 = ('{}'.format('POLIMENTO'))

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] == 'X' and xp.loc[16, 'Vip'] != 'x':

            serv16 = ('{}'.format('POLIMENTO'))

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] != 'X':

            serv16 = ('{}'.format('POLIMENTO'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] == 'X' and xp.loc[16, 'Vip'] != 'x':

            serv16 = ('{}'.format('POLIMENTO'))

        elif xp.loc[16, 'Lavagem simples'] == '' and xp.loc[16, 'Poli'] == '' and xp.loc[16, 'Vip'] == '':

            serv16 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

            # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[17, 'Lavagem simples'] == 'x' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] == 'x':

            serv17 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[17, 'Lavagem simples'] == 'x' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] == 'X':

            serv17 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[17, 'Lavagem simples'] == 'x' and xp.loc[17, 'Poli'] == 'X' and xp.loc[17, 'Vip'] == 'x':

            serv17 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[17, 'Lavagem simples'] == 'X' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] == 'x':

            serv17 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[17, 'Lavagem simples'] == 'x' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] != 'x':

            serv17 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[17, 'Lavagem simples'] == 'x' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] != 'X':

            serv17 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[17, 'Lavagem simples'] == 'x' and xp.loc[17, 'Poli'] == 'X' and xp.loc[17, 'Vip'] != 'x':

            serv17 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[17, 'Lavagem simples'] == 'x' and xp.loc[17, 'Poli'] == 'X' and xp.loc[17, 'Vip'] != 'X':

            serv17 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[17, 'Lavagem simples'] == 'X' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] != 'x':

            serv17 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[17, 'Lavagem simples'] == 'X' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] != 'X':

            serv17 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[17, 'Lavagem simples'] == 'x' and xp.loc[17, 'Poli'] != 'x' and xp.loc[17, 'Vip'] != 'x':

            serv17 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[17, 'Lavagem simples'] == 'x' and xp.loc[17, 'Poli'] != 'X' and xp.loc[17, 'Vip'] != 'X':

            serv17 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[17, 'Lavagem simples'] == 'X' and xp.loc[17, 'Poli'] != 'x' and xp.loc[17, 'Vip'] != 'X':

            serv17 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[17, 'Lavagem simples'] == 'X' and xp.loc[17, 'Poli'] != 'X' and xp.loc[17, 'Vip'] != 'x':

            serv17 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[17, 'Lavagem simples'] != 'x' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] == 'x':

            serv17 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[17, 'Lavagem simples'] != 'X' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] == 'x':

            serv17 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[17, 'Lavagem simples'] != 'x' and xp.loc[17, 'Poli'] == 'X' and xp.loc[17, 'Vip'] == 'x':

            serv17 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[17, 'Lavagem simples'] != 'X' and xp.loc[17, 'Poli'] == 'X' and xp.loc[17, 'Vip'] == 'x':

            serv17 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[17, 'Lavagem simples'] != 'x' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] == 'X':

            serv17 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[17, 'Lavagem simples'] != 'X' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] == 'X':

            serv17 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[17, 'Lavagem simples'] != 'x' and xp.loc[17, 'Poli'] != 'x' and xp.loc[17, 'Vip'] == 'x':

            serv17 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[17, 'Lavagem simples'] != 'X' and xp.loc[17, 'Poli'] != 'X' and xp.loc[17, 'Vip'] == 'X':

            serv17 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[17, 'Lavagem simples'] != 'X' and xp.loc[17, 'Poli'] != 'X' and xp.loc[17, 'Vip'] == 'x':

            serv17 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[17, 'Lavagem simples'] != 'x' and xp.loc[17, 'Poli'] != 'x' and xp.loc[17, 'Vip'] == 'X':

            serv17 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[17, 'Lavagem simples'] != 'x' and xp.loc[17, 'Poli'] != 'X' and xp.loc[17, 'Vip'] == 'x':

            serv17 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[17, 'Lavagem simples'] != 'X' and xp.loc[17, 'Poli'] != 'x' and xp.loc[17, 'Vip'] == 'X':

            serv17 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[17, 'Lavagem simples'] != 'x' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] != 'x':

            serv17 = ('{}'.format('POLIMENTO'))

        elif xp.loc[17, 'Lavagem simples'] != 'X' and xp.loc[17, 'Poli'] == 'X' and xp.loc[17, 'Vip'] != 'X':

            serv17 = ('{}'.format('POLIMENTO'))

        elif xp.loc[17, 'Lavagem simples'] != 'X' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] != 'X':

            serv17 = ('{}'.format('POLIMENTO'))

        elif xp.loc[17, 'Lavagem simples'] != 'x' and xp.loc[17, 'Poli'] == 'X' and xp.loc[17, 'Vip'] != 'x':

            serv17 = ('{}'.format('POLIMENTO'))

        elif xp.loc[17, 'Lavagem simples'] != 'x' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] != 'X':

            serv17 = ('{}'.format('POLIMENTO'))

        elif xp.loc[17, 'Lavagem simples'] != 'X' and xp.loc[17, 'Poli'] == 'X' and xp.loc[17, 'Vip'] != 'x':

            serv17 = ('{}'.format('POLIMENTO'))

        elif xp.loc[17, 'Lavagem simples'] == '' and xp.loc[17, 'Poli'] == '' and xp.loc[17, 'Vip'] == '':

            serv17 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

            # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[18, 'Lavagem simples'] == 'x' and xp.loc[18, 'Poli'] == 'x' and xp.loc[18, 'Vip'] == 'x':

            serv18 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[18, 'Lavagem simples'] == 'x' and xp.loc[18, 'Poli'] == 'x' and xp.loc[18, 'Vip'] == 'X':

            serv18 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[18, 'Lavagem simples'] == 'x' and xp.loc[18, 'Poli'] == 'X' and xp.loc[18, 'Vip'] == 'x':

            serv18 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[18, 'Lavagem simples'] == 'X' and xp.loc[18, 'Poli'] == 'x' and xp.loc[18, 'Vip'] == 'x':

            serv18 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[18, 'Lavagem simples'] == 'x' and xp.loc[18, 'Poli'] == 'x' and xp.loc[18, 'Vip'] != 'x':

            serv18 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[18, 'Lavagem simples'] == 'x' and xp.loc[18, 'Poli'] == 'x' and xp.loc[18, 'Vip'] != 'X':

            serv18 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[18, 'Lavagem simples'] == 'x' and xp.loc[18, 'Poli'] == 'X' and xp.loc[18, 'Vip'] != 'x':

            serv18 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[18, 'Lavagem simples'] == 'x' and xp.loc[18, 'Poli'] == 'X' and xp.loc[18, 'Vip'] != 'X':

            serv18 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[18, 'Lavagem simples'] == 'X' and xp.loc[18, 'Poli'] == 'x' and xp.loc[18, 'Vip'] != 'x':

            serv18 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[18, 'Lavagem simples'] == 'X' and xp.loc[18, 'Poli'] == 'x' and xp.loc[18, 'Vip'] != 'X':

            serv18 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[18, 'Lavagem simples'] == 'x' and xp.loc[18, 'Poli'] != 'x' and xp.loc[18, 'Vip'] != 'x':

            serv18 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[18, 'Lavagem simples'] == 'x' and xp.loc[18, 'Poli'] != 'X' and xp.loc[18, 'Vip'] != 'X':

            serv18 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[18, 'Lavagem simples'] == 'X' and xp.loc[18, 'Poli'] != 'x' and xp.loc[18, 'Vip'] != 'X':

            serv18 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[18, 'Lavagem simples'] == 'X' and xp.loc[18, 'Poli'] != 'X' and xp.loc[18, 'Vip'] != 'x':

            serv18 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[18, 'Lavagem simples'] != 'x' and xp.loc[18, 'Poli'] == 'x' and xp.loc[18, 'Vip'] == 'x':

            serv18 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[18, 'Lavagem simples'] != 'X' and xp.loc[18, 'Poli'] == 'x' and xp.loc[18, 'Vip'] == 'x':

            serv18 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[18, 'Lavagem simples'] != 'x' and xp.loc[18, 'Poli'] == 'X' and xp.loc[18, 'Vip'] == 'x':

            serv18 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[18, 'Lavagem simples'] != 'X' and xp.loc[18, 'Poli'] == 'X' and xp.loc[18, 'Vip'] == 'x':

            serv18 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[18, 'Lavagem simples'] != 'x' and xp.loc[18, 'Poli'] == 'x' and xp.loc[18, 'Vip'] == 'X':

            serv18 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[18, 'Lavagem simples'] != 'X' and xp.loc[18, 'Poli'] == 'x' and xp.loc[18, 'Vip'] == 'X':

            serv18 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[18, 'Lavagem simples'] != 'x' and xp.loc[18, 'Poli'] != 'x' and xp.loc[18, 'Vip'] == 'x':

            serv18 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[18, 'Lavagem simples'] != 'X' and xp.loc[18, 'Poli'] != 'X' and xp.loc[18, 'Vip'] == 'X':

            serv18 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[18, 'Lavagem simples'] != 'X' and xp.loc[18, 'Poli'] != 'X' and xp.loc[18, 'Vip'] == 'x':

            serv18 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[18, 'Lavagem simples'] != 'x' and xp.loc[18, 'Poli'] != 'x' and xp.loc[18, 'Vip'] == 'X':

            serv18 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[18, 'Lavagem simples'] != 'x' and xp.loc[18, 'Poli'] != 'X' and xp.loc[18, 'Vip'] == 'x':

            serv18 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[18, 'Lavagem simples'] != 'X' and xp.loc[18, 'Poli'] != 'x' and xp.loc[18, 'Vip'] == 'X':

            serv18 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[18, 'Lavagem simples'] != 'x' and xp.loc[18, 'Poli'] == 'x' and xp.loc[18, 'Vip'] != 'x':

            serv18 = ('{}'.format('POLIMENTO'))

        elif xp.loc[18, 'Lavagem simples'] != 'X' and xp.loc[18, 'Poli'] == 'X' and xp.loc[18, 'Vip'] != 'X':

            serv18 = ('{}'.format('POLIMENTO'))

        elif xp.loc[18, 'Lavagem simples'] != 'X' and xp.loc[18, 'Poli'] == 'x' and xp.loc[18, 'Vip'] != 'X':

            serv18 = ('{}'.format('POLIMENTO'))

        elif xp.loc[18, 'Lavagem simples'] != 'x' and xp.loc[18, 'Poli'] == 'X' and xp.loc[18, 'Vip'] != 'x':

            serv18 = ('{}'.format('POLIMENTO'))

        elif xp.loc[18, 'Lavagem simples'] != 'x' and xp.loc[18, 'Poli'] == 'x' and xp.loc[18, 'Vip'] != 'X':

            serv18 = ('{}'.format('POLIMENTO'))

        elif xp.loc[18, 'Lavagem simples'] != 'X' and xp.loc[18, 'Poli'] == 'X' and xp.loc[18, 'Vip'] != 'x':

            serv18 = ('{}'.format('POLIMENTO'))

        elif xp.loc[18, 'Lavagem simples'] == '' and xp.loc[18, 'Poli'] == '' and xp.loc[18, 'Vip'] == '':

            serv18 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        r2 = '{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}'.format(
            x0, '', md02, '', vp1, '', serv0, x1, '',
            md05, '', vp2, '', serv1, x2, '', md06, '', vp3, '', serv2, x3, '', md07, '', vp4, '', serv3, x4, '', md08,
            '', vp5, '', serv4, x5, '',
            md09, '', vp6, '', serv5, x6, '', md10, '', vp7, '', serv6, x7, '', md11, '',
            vp8, '', serv7, x8, '', md12, '', vp9, '', serv8, x9, '', md13, '', vp10, '', serv9,
            x10, '', md14, '', vp11, '', serv10, x11, '', md15, '', vp12, '', serv11,
            x12, '', md16, '', vp13, '', serv12, x13, '', md17, '', vp14, '', serv13, x14, '',
            md18, '', vp15, '', serv14, x15, '', md19, '', vp16, '', serv15, x16, '', md20, '',
            vp17, '', serv16, x17, '', md21, '', vp18, '', serv17, x18, '', md22, '', vp19, '', serv18)

        return r2


func19()


def func20():
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

    for ix in range((qtd_linhaspl - 1), 9, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x10 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 10, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x11 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 11, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x12 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 12, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x13 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 13, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x14 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 14, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x15 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 15, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x16 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 16, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x17 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 17, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x18 = '{}-{}'.format(inicio0, final0)

    for ix in range((qtd_linhaspl - 1), 18, -1):
        v0 = xp.loc[ix, 'Placa']
        tamanho0 = (len(v0))
        inicio0 = v0[0:3]
        final0 = v0[3:tamanho0]
        x19 = '{}-{}'.format(inicio0, final0)

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
        celula_m10 = xp.loc[10, 'Modelo']
        md14 = celula_m10.upper()
        celula_m11 = xp.loc[11, 'Modelo']
        md15 = celula_m11.upper()
        celula_m12 = xp.loc[12, 'Modelo']
        md16 = celula_m12.upper()
        celula_m13 = xp.loc[13, 'Modelo']
        md17 = celula_m13.upper()
        celula_m14 = xp.loc[14, 'Modelo']
        md18 = celula_m14.upper()
        celula_m15 = xp.loc[15, 'Modelo']
        md19 = celula_m15.upper()
        celula_m16 = xp.loc[16, 'Modelo']
        md20 = celula_m16.upper()
        celula_m17 = xp.loc[17, 'Modelo']
        md21 = celula_m17.upper()
        celula_m18 = xp.loc[18, 'Modelo']
        md22 = celula_m18.upper()
        celula_m19 = xp.loc[19, 'Modelo']
        md23 = celula_m19.upper()

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
        celula_v = xp.loc[10, 'Valor']
        vp11 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[11, 'Valor']
        vp12 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[12, 'Valor']
        vp13 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[13, 'Valor']
        vp14 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[14, 'Valor']
        vp15 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[15, 'Valor']
        vp16 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[16, 'Valor']
        vp17 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[17, 'Valor']
        vp18 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[18, 'Valor']
        vp19 = '{} {}'.format('R$', float(celula_v))
        celula_v = xp.loc[19, 'Valor']
        vp20 = '{} {}'.format('R$', float(celula_v))

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

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[10, 'Lavagem simples'] == 'x' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[10, 'Lavagem simples'] == 'X' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] != 'X' and xp.loc[10, 'Vip'] == 'x':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] != 'x' and xp.loc[10, 'Vip'] == 'X':

            serv10 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'x' and xp.loc[10, 'Poli'] == 'x' and xp.loc[10, 'Vip'] != 'X':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] != 'X' and xp.loc[10, 'Poli'] == 'X' and xp.loc[10, 'Vip'] != 'x':

            serv10 = ('{}'.format('POLIMENTO'))

        elif xp.loc[10, 'Lavagem simples'] == '' and xp.loc[10, 'Poli'] == '' and xp.loc[10, 'Vip'] == '':

            serv10 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[11, 'Lavagem simples'] == 'x' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[11, 'Lavagem simples'] == 'X' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] != 'X' and xp.loc[11, 'Vip'] == 'x':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] != 'x' and xp.loc[11, 'Vip'] == 'X':

            serv11 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'x' and xp.loc[11, 'Poli'] == 'x' and xp.loc[11, 'Vip'] != 'X':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] != 'X' and xp.loc[11, 'Poli'] == 'X' and xp.loc[11, 'Vip'] != 'x':

            serv11 = ('{}'.format('POLIMENTO'))

        elif xp.loc[11, 'Lavagem simples'] == '' and xp.loc[11, 'Poli'] == '' and xp.loc[11, 'Vip'] == '':

            serv11 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[12, 'Lavagem simples'] == 'x' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[12, 'Lavagem simples'] == 'X' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] != 'X' and xp.loc[12, 'Vip'] == 'x':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] != 'x' and xp.loc[12, 'Vip'] == 'X':

            serv12 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'x' and xp.loc[12, 'Poli'] == 'x' and xp.loc[12, 'Vip'] != 'X':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] != 'X' and xp.loc[12, 'Poli'] == 'X' and xp.loc[12, 'Vip'] != 'x':

            serv12 = ('{}'.format('POLIMENTO'))

        elif xp.loc[12, 'Lavagem simples'] == '' and xp.loc[12, 'Poli'] == '' and xp.loc[12, 'Vip'] == '':

            serv12 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[13, 'Lavagem simples'] == 'x' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[13, 'Lavagem simples'] == 'X' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] != 'X' and xp.loc[13, 'Vip'] == 'x':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] != 'x' and xp.loc[13, 'Vip'] == 'X':

            serv13 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'x' and xp.loc[13, 'Poli'] == 'x' and xp.loc[13, 'Vip'] != 'X':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] != 'X' and xp.loc[13, 'Poli'] == 'X' and xp.loc[13, 'Vip'] != 'x':

            serv13 = ('{}'.format('POLIMENTO'))

        elif xp.loc[13, 'Lavagem simples'] == '' and xp.loc[13, 'Poli'] == '' and xp.loc[13, 'Vip'] == '':

            serv13 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

            # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[14, 'Lavagem simples'] == 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] == 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] == 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] != 'x' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[14, 'Lavagem simples'] == 'x' and xp.loc[14, 'Poli'] != 'X' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[14, 'Lavagem simples'] == 'X' and xp.loc[14, 'Poli'] != 'x' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[14, 'Lavagem simples'] == 'X' and xp.loc[14, 'Poli'] != 'X' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] != 'x' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] != 'X' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] != 'X' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] != 'x' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] != 'X' and xp.loc[14, 'Vip'] == 'x':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] != 'x' and xp.loc[14, 'Vip'] == 'X':

            serv14 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] != 'x' and xp.loc[14, 'Poli'] == 'x' and xp.loc[14, 'Vip'] != 'X':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] != 'X' and xp.loc[14, 'Poli'] == 'X' and xp.loc[14, 'Vip'] != 'x':

            serv14 = ('{}'.format('POLIMENTO'))

        elif xp.loc[14, 'Lavagem simples'] == '' and xp.loc[14, 'Poli'] == '' and xp.loc[14, 'Vip'] == '':

            serv14 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))
            # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'X':

            serv15 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[15, 'Lavagem simples'] == 'X' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] == 'X' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] == 'X' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] != 'x' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[15, 'Lavagem simples'] == 'x' and xp.loc[15, 'Poli'] != 'X' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[15, 'Lavagem simples'] == 'X' and xp.loc[15, 'Poli'] != 'x' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[15, 'Lavagem simples'] == 'X' and xp.loc[15, 'Poli'] != 'X' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'X':

            serv15 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] == 'X':

            serv15 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] != 'x' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] != 'X' and xp.loc[15, 'Vip'] == 'X':

            serv15 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] != 'X' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] != 'x' and xp.loc[15, 'Vip'] == 'X':

            serv15 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] != 'X' and xp.loc[15, 'Vip'] == 'x':

            serv15 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] != 'x' and xp.loc[15, 'Vip'] == 'X':

            serv15 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}'.format('POLIMENTO'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}'.format('POLIMENTO'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}'.format('POLIMENTO'))

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}'.format('POLIMENTO'))

        elif xp.loc[15, 'Lavagem simples'] != 'x' and xp.loc[15, 'Poli'] == 'x' and xp.loc[15, 'Vip'] != 'X':

            serv15 = ('{}'.format('POLIMENTO'))

        elif xp.loc[15, 'Lavagem simples'] != 'X' and xp.loc[15, 'Poli'] == 'X' and xp.loc[15, 'Vip'] != 'x':

            serv15 = ('{}'.format('POLIMENTO'))

        elif xp.loc[15, 'Lavagem simples'] == '' and xp.loc[15, 'Poli'] == '' and xp.loc[15, 'Vip'] == '':

            serv15 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

            # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] == 'X':

            serv16 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] == 'X' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[16, 'Lavagem simples'] == 'X' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] != 'x':

            serv16 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] != 'X':

            serv16 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] == 'X' and xp.loc[16, 'Vip'] != 'x':

            serv16 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] == 'X' and xp.loc[16, 'Vip'] != 'X':

            serv16 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] == 'X' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] != 'x':

            serv16 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] == 'X' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] != 'X':

            serv16 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] != 'x' and xp.loc[16, 'Vip'] != 'x':

            serv16 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[16, 'Lavagem simples'] == 'x' and xp.loc[16, 'Poli'] != 'X' and xp.loc[16, 'Vip'] != 'X':

            serv16 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[16, 'Lavagem simples'] == 'X' and xp.loc[16, 'Poli'] != 'x' and xp.loc[16, 'Vip'] != 'X':

            serv16 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[16, 'Lavagem simples'] == 'X' and xp.loc[16, 'Poli'] != 'X' and xp.loc[16, 'Vip'] != 'x':

            serv16 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] == 'X' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] == 'X' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] == 'X':

            serv16 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] == 'X':

            serv16 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] != 'x' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] != 'X' and xp.loc[16, 'Vip'] == 'X':

            serv16 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] != 'X' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] != 'x' and xp.loc[16, 'Vip'] == 'X':

            serv16 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] != 'X' and xp.loc[16, 'Vip'] == 'x':

            serv16 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] != 'x' and xp.loc[16, 'Vip'] == 'X':

            serv16 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] != 'x':

            serv16 = ('{}'.format('POLIMENTO'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] == 'X' and xp.loc[16, 'Vip'] != 'X':

            serv16 = ('{}'.format('POLIMENTO'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] != 'X':

            serv16 = ('{}'.format('POLIMENTO'))

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] == 'X' and xp.loc[16, 'Vip'] != 'x':

            serv16 = ('{}'.format('POLIMENTO'))

        elif xp.loc[16, 'Lavagem simples'] != 'x' and xp.loc[16, 'Poli'] == 'x' and xp.loc[16, 'Vip'] != 'X':

            serv16 = ('{}'.format('POLIMENTO'))

        elif xp.loc[16, 'Lavagem simples'] != 'X' and xp.loc[16, 'Poli'] == 'X' and xp.loc[16, 'Vip'] != 'x':

            serv16 = ('{}'.format('POLIMENTO'))

        elif xp.loc[16, 'Lavagem simples'] == '' and xp.loc[16, 'Poli'] == '' and xp.loc[16, 'Vip'] == '':

            serv16 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

            # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[17, 'Lavagem simples'] == 'x' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] == 'x':

            serv17 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[17, 'Lavagem simples'] == 'x' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] == 'X':

            serv17 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[17, 'Lavagem simples'] == 'x' and xp.loc[17, 'Poli'] == 'X' and xp.loc[17, 'Vip'] == 'x':

            serv17 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[17, 'Lavagem simples'] == 'X' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] == 'x':

            serv17 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[17, 'Lavagem simples'] == 'x' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] != 'x':

            serv17 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[17, 'Lavagem simples'] == 'x' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] != 'X':

            serv17 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[17, 'Lavagem simples'] == 'x' and xp.loc[17, 'Poli'] == 'X' and xp.loc[17, 'Vip'] != 'x':

            serv17 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[17, 'Lavagem simples'] == 'x' and xp.loc[17, 'Poli'] == 'X' and xp.loc[17, 'Vip'] != 'X':

            serv17 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[17, 'Lavagem simples'] == 'X' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] != 'x':

            serv17 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[17, 'Lavagem simples'] == 'X' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] != 'X':

            serv17 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[17, 'Lavagem simples'] == 'x' and xp.loc[17, 'Poli'] != 'x' and xp.loc[17, 'Vip'] != 'x':

            serv17 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[17, 'Lavagem simples'] == 'x' and xp.loc[17, 'Poli'] != 'X' and xp.loc[17, 'Vip'] != 'X':

            serv17 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[17, 'Lavagem simples'] == 'X' and xp.loc[17, 'Poli'] != 'x' and xp.loc[17, 'Vip'] != 'X':

            serv17 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[17, 'Lavagem simples'] == 'X' and xp.loc[17, 'Poli'] != 'X' and xp.loc[17, 'Vip'] != 'x':

            serv17 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[17, 'Lavagem simples'] != 'x' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] == 'x':

            serv17 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[17, 'Lavagem simples'] != 'X' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] == 'x':

            serv17 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[17, 'Lavagem simples'] != 'x' and xp.loc[17, 'Poli'] == 'X' and xp.loc[17, 'Vip'] == 'x':

            serv17 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[17, 'Lavagem simples'] != 'X' and xp.loc[17, 'Poli'] == 'X' and xp.loc[17, 'Vip'] == 'x':

            serv17 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[17, 'Lavagem simples'] != 'x' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] == 'X':

            serv17 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[17, 'Lavagem simples'] != 'X' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] == 'X':

            serv17 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[17, 'Lavagem simples'] != 'x' and xp.loc[17, 'Poli'] != 'x' and xp.loc[17, 'Vip'] == 'x':

            serv17 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[17, 'Lavagem simples'] != 'X' and xp.loc[17, 'Poli'] != 'X' and xp.loc[17, 'Vip'] == 'X':

            serv17 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[17, 'Lavagem simples'] != 'X' and xp.loc[17, 'Poli'] != 'X' and xp.loc[17, 'Vip'] == 'x':

            serv17 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[17, 'Lavagem simples'] != 'x' and xp.loc[17, 'Poli'] != 'x' and xp.loc[17, 'Vip'] == 'X':

            serv17 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[17, 'Lavagem simples'] != 'x' and xp.loc[17, 'Poli'] != 'X' and xp.loc[17, 'Vip'] == 'x':

            serv17 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[17, 'Lavagem simples'] != 'X' and xp.loc[17, 'Poli'] != 'x' and xp.loc[17, 'Vip'] == 'X':

            serv17 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[17, 'Lavagem simples'] != 'x' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] != 'x':

            serv17 = ('{}'.format('POLIMENTO'))

        elif xp.loc[17, 'Lavagem simples'] != 'X' and xp.loc[17, 'Poli'] == 'X' and xp.loc[17, 'Vip'] != 'X':

            serv17 = ('{}'.format('POLIMENTO'))

        elif xp.loc[17, 'Lavagem simples'] != 'X' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] != 'X':

            serv17 = ('{}'.format('POLIMENTO'))

        elif xp.loc[17, 'Lavagem simples'] != 'x' and xp.loc[17, 'Poli'] == 'X' and xp.loc[17, 'Vip'] != 'x':

            serv17 = ('{}'.format('POLIMENTO'))

        elif xp.loc[17, 'Lavagem simples'] != 'x' and xp.loc[17, 'Poli'] == 'x' and xp.loc[17, 'Vip'] != 'X':

            serv17 = ('{}'.format('POLIMENTO'))

        elif xp.loc[17, 'Lavagem simples'] != 'X' and xp.loc[17, 'Poli'] == 'X' and xp.loc[17, 'Vip'] != 'x':

            serv17 = ('{}'.format('POLIMENTO'))

        elif xp.loc[17, 'Lavagem simples'] == '' and xp.loc[17, 'Poli'] == '' and xp.loc[17, 'Vip'] == '':

            serv17 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

            # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[18, 'Lavagem simples'] == 'x' and xp.loc[18, 'Poli'] == 'x' and xp.loc[18, 'Vip'] == 'x':

            serv18 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[18, 'Lavagem simples'] == 'x' and xp.loc[18, 'Poli'] == 'x' and xp.loc[18, 'Vip'] == 'X':

            serv18 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[18, 'Lavagem simples'] == 'x' and xp.loc[18, 'Poli'] == 'X' and xp.loc[18, 'Vip'] == 'x':

            serv18 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[18, 'Lavagem simples'] == 'X' and xp.loc[18, 'Poli'] == 'x' and xp.loc[18, 'Vip'] == 'x':

            serv18 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[18, 'Lavagem simples'] == 'x' and xp.loc[18, 'Poli'] == 'x' and xp.loc[18, 'Vip'] != 'x':

            serv18 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[18, 'Lavagem simples'] == 'x' and xp.loc[18, 'Poli'] == 'x' and xp.loc[18, 'Vip'] != 'X':

            serv18 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[18, 'Lavagem simples'] == 'x' and xp.loc[18, 'Poli'] == 'X' and xp.loc[18, 'Vip'] != 'x':

            serv18 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[18, 'Lavagem simples'] == 'x' and xp.loc[18, 'Poli'] == 'X' and xp.loc[18, 'Vip'] != 'X':

            serv18 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[18, 'Lavagem simples'] == 'X' and xp.loc[18, 'Poli'] == 'x' and xp.loc[18, 'Vip'] != 'x':

            serv18 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[18, 'Lavagem simples'] == 'X' and xp.loc[18, 'Poli'] == 'x' and xp.loc[18, 'Vip'] != 'X':

            serv18 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[18, 'Lavagem simples'] == 'x' and xp.loc[18, 'Poli'] != 'x' and xp.loc[18, 'Vip'] != 'x':

            serv18 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[18, 'Lavagem simples'] == 'x' and xp.loc[18, 'Poli'] != 'X' and xp.loc[18, 'Vip'] != 'X':

            serv18 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[18, 'Lavagem simples'] == 'X' and xp.loc[18, 'Poli'] != 'x' and xp.loc[18, 'Vip'] != 'X':

            serv18 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[18, 'Lavagem simples'] == 'X' and xp.loc[18, 'Poli'] != 'X' and xp.loc[18, 'Vip'] != 'x':

            serv18 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[18, 'Lavagem simples'] != 'x' and xp.loc[18, 'Poli'] == 'x' and xp.loc[18, 'Vip'] == 'x':

            serv18 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[18, 'Lavagem simples'] != 'X' and xp.loc[18, 'Poli'] == 'x' and xp.loc[18, 'Vip'] == 'x':

            serv18 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[18, 'Lavagem simples'] != 'x' and xp.loc[18, 'Poli'] == 'X' and xp.loc[18, 'Vip'] == 'x':

            serv18 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[18, 'Lavagem simples'] != 'X' and xp.loc[18, 'Poli'] == 'X' and xp.loc[18, 'Vip'] == 'x':

            serv18 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[18, 'Lavagem simples'] != 'x' and xp.loc[18, 'Poli'] == 'x' and xp.loc[18, 'Vip'] == 'X':

            serv18 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[18, 'Lavagem simples'] != 'X' and xp.loc[18, 'Poli'] == 'x' and xp.loc[18, 'Vip'] == 'X':

            serv18 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[18, 'Lavagem simples'] != 'x' and xp.loc[18, 'Poli'] != 'x' and xp.loc[18, 'Vip'] == 'x':

            serv18 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[18, 'Lavagem simples'] != 'X' and xp.loc[18, 'Poli'] != 'X' and xp.loc[18, 'Vip'] == 'X':

            serv18 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[18, 'Lavagem simples'] != 'X' and xp.loc[18, 'Poli'] != 'X' and xp.loc[18, 'Vip'] == 'x':

            serv18 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[18, 'Lavagem simples'] != 'x' and xp.loc[18, 'Poli'] != 'x' and xp.loc[18, 'Vip'] == 'X':

            serv18 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[18, 'Lavagem simples'] != 'x' and xp.loc[18, 'Poli'] != 'X' and xp.loc[18, 'Vip'] == 'x':

            serv18 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[18, 'Lavagem simples'] != 'X' and xp.loc[18, 'Poli'] != 'x' and xp.loc[18, 'Vip'] == 'X':

            serv18 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[18, 'Lavagem simples'] != 'x' and xp.loc[18, 'Poli'] == 'x' and xp.loc[18, 'Vip'] != 'x':

            serv18 = ('{}'.format('POLIMENTO'))

        elif xp.loc[18, 'Lavagem simples'] != 'X' and xp.loc[18, 'Poli'] == 'X' and xp.loc[18, 'Vip'] != 'X':

            serv18 = ('{}'.format('POLIMENTO'))

        elif xp.loc[18, 'Lavagem simples'] != 'X' and xp.loc[18, 'Poli'] == 'x' and xp.loc[18, 'Vip'] != 'X':

            serv18 = ('{}'.format('POLIMENTO'))

        elif xp.loc[18, 'Lavagem simples'] != 'x' and xp.loc[18, 'Poli'] == 'X' and xp.loc[18, 'Vip'] != 'x':

            serv18 = ('{}'.format('POLIMENTO'))

        elif xp.loc[18, 'Lavagem simples'] != 'x' and xp.loc[18, 'Poli'] == 'x' and xp.loc[18, 'Vip'] != 'X':

            serv18 = ('{}'.format('POLIMENTO'))

        elif xp.loc[18, 'Lavagem simples'] != 'X' and xp.loc[18, 'Poli'] == 'X' and xp.loc[18, 'Vip'] != 'x':

            serv18 = ('{}'.format('POLIMENTO'))

        elif xp.loc[18, 'Lavagem simples'] == '' and xp.loc[18, 'Poli'] == '' and xp.loc[18, 'Vip'] == '':

            serv18 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

            # SEXTA COMBINAÇÃO >> Lav Simples + Polimento + Vip
        if xp.loc[19, 'Lavagem simples'] == 'x' and xp.loc[19, 'Poli'] == 'x' and xp.loc[19, 'Vip'] == 'x':

            serv19 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[19, 'Lavagem simples'] == 'x' and xp.loc[19, 'Poli'] == 'x' and xp.loc[19, 'Vip'] == 'X':

            serv19 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[19, 'Lavagem simples'] == 'x' and xp.loc[19, 'Poli'] == 'X' and xp.loc[19, 'Vip'] == 'x':

            serv19 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        elif xp.loc[19, 'Lavagem simples'] == 'X' and xp.loc[19, 'Poli'] == 'x' and xp.loc[19, 'Vip'] == 'x':

            serv19 = ('{}{}{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.', '+', 'VIP'))

        # QUINTA COMBINAÇÃO >> Lav Simples + Polimento

        elif xp.loc[19, 'Lavagem simples'] == 'x' and xp.loc[19, 'Poli'] == 'x' and xp.loc[19, 'Vip'] != 'x':

            serv19 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[19, 'Lavagem simples'] == 'x' and xp.loc[19, 'Poli'] == 'x' and xp.loc[19, 'Vip'] != 'X':

            serv19 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[19, 'Lavagem simples'] == 'x' and xp.loc[19, 'Poli'] == 'X' and xp.loc[19, 'Vip'] != 'x':

            serv19 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[19, 'Lavagem simples'] == 'x' and xp.loc[19, 'Poli'] == 'X' and xp.loc[19, 'Vip'] != 'X':

            serv19 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[19, 'Lavagem simples'] == 'X' and xp.loc[19, 'Poli'] == 'x' and xp.loc[19, 'Vip'] != 'x':

            serv19 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        elif xp.loc[19, 'Lavagem simples'] == 'X' and xp.loc[19, 'Poli'] == 'x' and xp.loc[19, 'Vip'] != 'X':

            serv19 = ('{}{}{}'.format('LAV. SIMPLES', '+', 'POLIM.'))

        # QUARTA COMBINAÇÃO >> Lav Simples

        elif xp.loc[19, 'Lavagem simples'] == 'x' and xp.loc[19, 'Poli'] != 'x' and xp.loc[19, 'Vip'] != 'x':

            serv19 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[19, 'Lavagem simples'] == 'x' and xp.loc[19, 'Poli'] != 'X' and xp.loc[19, 'Vip'] != 'X':

            serv19 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[19, 'Lavagem simples'] == 'X' and xp.loc[19, 'Poli'] != 'x' and xp.loc[19, 'Vip'] != 'X':

            serv19 = ('{}'.format('LAV. SIMPLES'))

        elif xp.loc[19, 'Lavagem simples'] == 'X' and xp.loc[19, 'Poli'] != 'X' and xp.loc[19, 'Vip'] != 'x':

            serv19 = ('{}'.format('LAV. SIMPLES'))

        # TERCEIRA COMBINAÇÃO >> Vip + Polimento

        elif xp.loc[19, 'Lavagem simples'] != 'x' and xp.loc[19, 'Poli'] == 'x' and xp.loc[19, 'Vip'] == 'x':

            serv19 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[19, 'Lavagem simples'] != 'X' and xp.loc[19, 'Poli'] == 'x' and xp.loc[19, 'Vip'] == 'x':

            serv19 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[19, 'Lavagem simples'] != 'x' and xp.loc[19, 'Poli'] == 'X' and xp.loc[19, 'Vip'] == 'x':

            serv19 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[19, 'Lavagem simples'] != 'X' and xp.loc[19, 'Poli'] == 'X' and xp.loc[19, 'Vip'] == 'x':

            serv19 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[19, 'Lavagem simples'] != 'x' and xp.loc[19, 'Poli'] == 'x' and xp.loc[19, 'Vip'] == 'X':

            serv19 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        elif xp.loc[19, 'Lavagem simples'] != 'X' and xp.loc[19, 'Poli'] == 'x' and xp.loc[19, 'Vip'] == 'X':

            serv19 = ('{}{}{}'.format('VIP', '+', 'POLIM.'))

        # SEGUNDA COMBINAÇÃO >> Vip

        elif xp.loc[19, 'Lavagem simples'] != 'x' and xp.loc[19, 'Poli'] != 'x' and xp.loc[19, 'Vip'] == 'x':

            serv19 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[19, 'Lavagem simples'] != 'X' and xp.loc[19, 'Poli'] != 'X' and xp.loc[19, 'Vip'] == 'X':

            serv19 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[19, 'Lavagem simples'] != 'X' and xp.loc[19, 'Poli'] != 'X' and xp.loc[19, 'Vip'] == 'x':

            serv19 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[19, 'Lavagem simples'] != 'x' and xp.loc[19, 'Poli'] != 'x' and xp.loc[19, 'Vip'] == 'X':

            serv19 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[19, 'Lavagem simples'] != 'x' and xp.loc[19, 'Poli'] != 'X' and xp.loc[19, 'Vip'] == 'x':

            serv19 = ('{}'.format('TRATAMENTO VIP'))

        elif xp.loc[19, 'Lavagem simples'] != 'X' and xp.loc[19, 'Poli'] != 'x' and xp.loc[19, 'Vip'] == 'X':

            serv19 = ('{}'.format('TRATAMENTO VIP'))

        # PRIMEIRA COMBINAÇÃO >> POLIMENTO

        elif xp.loc[19, 'Lavagem simples'] != 'x' and xp.loc[19, 'Poli'] == 'x' and xp.loc[19, 'Vip'] != 'x':

            serv19 = ('{}'.format('POLIMENTO'))

        elif xp.loc[19, 'Lavagem simples'] != 'X' and xp.loc[19, 'Poli'] == 'X' and xp.loc[19, 'Vip'] != 'X':

            serv19 = ('{}'.format('POLIMENTO'))

        elif xp.loc[19, 'Lavagem simples'] != 'X' and xp.loc[19, 'Poli'] == 'x' and xp.loc[19, 'Vip'] != 'X':

            serv19 = ('{}'.format('POLIMENTO'))

        elif xp.loc[19, 'Lavagem simples'] != 'x' and xp.loc[19, 'Poli'] == 'X' and xp.loc[19, 'Vip'] != 'x':

            serv19 = ('{}'.format('POLIMENTO'))

        elif xp.loc[19, 'Lavagem simples'] != 'x' and xp.loc[19, 'Poli'] == 'x' and xp.loc[19, 'Vip'] != 'X':

            serv19 = ('{}'.format('POLIMENTO'))

        elif xp.loc[19, 'Lavagem simples'] != 'X' and xp.loc[19, 'Poli'] == 'X' and xp.loc[19, 'Vip'] != 'x':

            serv19 = ('{}'.format('POLIMENTO'))

        elif xp.loc[19, 'Lavagem simples'] == '' and xp.loc[19, 'Poli'] == '' and xp.loc[19, 'Vip'] == '':

            serv19 = ('{}'.format('Dados insuficiêntes. Informe o tipo de serviço'))

        r2 = '{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}\n{}{:^10}{}{:^10}{}{:^10}{}'.format(
            x0, '', md02, '', vp1, '', serv0, x1, '',
            md05, '', vp2, '', serv1, x2, '', md06, '', vp3, '', serv2, x3, '', md07, '', vp4, '', serv3, x4, '', md08,
            '', vp5, '', serv4, x5, '',
            md09, '', vp6, '', serv5, x6, '', md10, '', vp7, '', serv6, x7, '', md11, '',
            vp8, '', serv7, x8, '', md12, '', vp9, '', serv8, x9, '', md13, '', vp10, '', serv9,
            x10, '', md14, '', vp11, '', serv10, x11, '', md15, '', vp12, '', serv11,
            x12, '', md16, '', vp13, '', serv12, x13, '', md17, '', vp14, '', serv13, x14, '',
            md18, '', vp15, '', serv14, x15, '', md19, '', vp16, '', serv15, x16, '', md20, '',
            vp17, '', serv16, x17, '', md21, '', vp18, '', serv17, x18, '', md22, '', vp19, '', serv18, x19, '', md23, '', vp20, '', serv19)

        return r2


func20()


