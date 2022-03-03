from iqoptionapi.stable_api import IQ_Option
import time, json
from datetime import datetime, tzinfo
from dateutil import tz


API = IQ_Option('jhonatta_rs@hotmail.com', 'Jhow.203098')
API.connect()
API.change_balance('PRACTICE') #PRACTICE / REAL

while True:
	if API.check_connect() == False:
		print('Erro ao se conectar')
		API.connect()
	else:
		print ('Conectado com sucesso')
		break
	
	time.sleep(1)

def perfil():
	perfil = json.loads(json.dumps(API.get_profile()))

	return perfil['result']

	'''
	name
	first_name
	last_name
	email
	city
	nickname
	currency
	currency_char
	address
	created
	postal_index
	gender
	birthdate
	balance
	'''

def timestamp_converter(x):
	hora = datetime.strptime(datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
	hora = hora.replace(tzinfo=tz.gettz('GMT'))

	return str(hora.astimezone(tz.gettz('America/Sao Paulo')))[:-6]

def payout(par, tipo, timeframe = 1):
	if tipo == 'turbo':
		a = API.get_all_profit()
		return int(100 * a [par]['turbo'])
	elif tipo == 'digital':
		API.subscribe_strike_list(par, timeframe)
		while True:
			d = API.get_digital_current_profit(par, timeframe)
			if d != False:
				d = int(d)
				break
			time.sleep(1)
		API.unsubscribe_strike_list(par, timeframe)
		return d

 

#Pegar historico de trading
status, historico = API.get_position_history_v2('turbo-option', 3, 0, 0, 0 )
'''
FINAL OPERACAO: close_time
INICIO OPERACAO: open_time
LUCRO: close_profit
ENTRADA: invest

--raw_event
PARIDADE: instrument_underlying / TURBO: active
DIRECAO: instrument_dir / TURBO: direction
VALOR: buy_amount


'''

for x in historico['positions']:
	print('PAR: ' +str(x['raw_event']['instrument_underlying'])+' / '+'DIRECAO: '+str(x['raw_event']['instrument_dir'])+' / '+'VALOR: '+str(x['raw_event']['buy_amount']))
	print('LUCRO: '+str(x['close_profit'] if x['close_profit'] == 0 else round(x['close_profit']-x['invest'], 2) )+' / '+'INICIO OP: '+str(timestamp_converter(x['open_time'] / 1000))+' / '+'FINAL OP: '+str(timestamp_converter(x['close_time'] / 1000)))
	print('\n')
	
	

#retornar pares que estão abertas no momento
'''par = API.get_all_open_time()
print(par)
for paridade in par['turbo']:
	if par['turbo'][paridade]['open'] == True:
		print('[ TURBO ]: ' + paridade+ '| Payout: '+ str(payout(paridade, 'turbo')))
	print('\n')

for paridade in par['digital']:
	if par['digital'][paridade]['open'] == True:
		print('[ DIGITAL ]: ' + paridade+ '| Payout: '+ str(payout(paridade, 'digital')))
	print('\n')
def banca():
print(API.get_balance())
'''
#par = "BTCUSD"
#Retorna o humor dos traders

'''
id = dict([(l,u) for u,l in API.get_all_ACTIVES_OPCODE().items()])

API.start_mood_stream('USDCHF')
API.start_mood_stream('GBPUSD')

while True:
	x = API.get_traders_mood()
	for i in x:
		print(id[i]+': '+str(int(100 * round(x,2)))
	print('\n')

	time.sleep(1)

API.stop_mood_stream('USDCHF')
API.stop_mood_stream('GBPUSD')
'''

#retorna infor das ultimas velas, hora inicio, 
'''vela = API.get_candles(par, 60, 10, time.time())

for velas in vela:
	print('Hora inicio: ' + str(timestamp_converter(velas['from'])) + ' Abertura: '+ str(velas['open']))
print(timestamp_converter(vela[0]['from']))'''

'''total = [] #Terá as info de todas as velas
tempo = time.time()

for i in range(2):
	X = API.get_candles(par,60, 1000, tempo)
	total = X+total
	tempo = int(X[0]['from'])-1

for velas in total:
	print(timestamp_converter(velas['from']))
print(len(total))'''

#Info de preço do gráfico de linha
'''API.start_candles_stream(par,60, 1)
time.sleep(1)

vela = API.get_realtime_candles(par, 60)

while True:
	for velas in vela:
		print(vela[velas]['close'])
	time.sleep(1)#diminui a precisão pois vai trazer os valores com 1s de atraso

API.stop_candles_stream(par,60)'''

