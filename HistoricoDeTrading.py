# Retorna o histórico, para pegar o histórico do digital, deve ser colocado 'digital-option' e para pegar binario, 
#	deve ser colocado 'turbo-option'
status,historico = API.get_position_history_v2('turbo-option', 7, 0, 0, 0)

'''

:::::::::::::::: [ MODO DIGITAL ] ::::::::::::::::
FINAL OPERACAO : historico['positions']['close_time']
INICIO OPERACAO: historico['positions']['open_time']
LUCRO          : historico['positions']['close_profit']
ENTRADA        : historico['positions']['invest']
PARIDADE       : historico['positions']['raw_event']['instrument_underlying']
DIRECAO        : historico['positions']['raw_event']['instrument_dir']
VALOR          : historico['positions']['raw_event']['buy_amount']

:::::::::::::::: [ MODO BINARIO ] ::::::::::::::::
MODO TURBO tem as chaves do dict diferentes para a direção da operação(put ou call) 
	e para exibir a paridade, deve ser utilizado:
DIRECAO : historico['positions']['raw_event']['direction']
PARIDADE: historico['positions']['raw_event']['active']
'''

for x in historico['positions']:
	print('PAR: '+str(x['raw_event']['active'])+' /  DIRECAO: '+str(x['raw_event']['direction'])+' / VALOR: '+str(x['invest']))
	print('LUCRO: '+str(x['close_profit'] if x['close_profit'] == 0 else round(x['close_profit']-x['invest'], 2) ) + ' | INICIO OP: '+str(timestamp_converter(x['open_time'] / 1000))+' / FIM OP: '+str(timestamp_converter(x['close_time'] / 1000)))
	print('\n')