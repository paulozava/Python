import pandas

site = pandas.read_json('https://cotacoes.economia.uol.com.br/ws/asset/484/intraday?size=500')
json = site['data'].to_json(orient='records')
result = pandas.read_json(json)
ap = pandas.DataFrame(columns=['Data', 'WEG4'])

site = pandas.read_html('http://cotacoes.economia.uol.com.br/acao/cotacoes-diarias.html?codigo=PETR4.SA&size=500')
df = site[1]
util = pandas.DataFrame(columns=['DataHora', 'Cotacao', 'Volume'])
util['DataHora'] = df['Data / Hora']
util['Cotacao'] = df['CotaÃ§Ã£o']
util['Volume'] = df['Volume']