def calcular_data(self, data):
    '''
        Funcao para calcular a distancia entre duas datas
    '''

    dataPublicacao = datetime.date(
        day = int( data[0:2] ),
        month = int( data[3:5] ),
        year = int( data[-4:] )
    )
    hoje = datetime.date.today()

    return (hoje - dataPublicacao).days

def tratar_nome_vaga (self, vaga):
    '''
        Funcao para remover caracteres especiais ("\n\t"), e fatiar o nome da vaga
    '''

    vaga = vaga.lower();
    vaga = vaga.strip()

    if '–' in vaga:
        vaga = vaga[0:vaga.index("–" )]

    elif '-' in vaga:
        vaga = vaga[0:vaga.index("-" )]

    return vaga

'''Dando bug, apagando comeco e final de algumas condicoes que nao se enquadra ao seguinte controle de fluxo
    if 'empregos' or 'vagas' or 'emprego' or 'vaga' in vaga:
        vaga = vaga.strip('empregos')
        vaga = vaga.strip('emprego')
        vaga = vaga.strip('vagas')
        vaga = vaga.strip('vaga')
'''
