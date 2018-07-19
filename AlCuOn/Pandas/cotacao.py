import pandas

site = pandas.read_json('https://cotacoes.economia.uol.com.br/ws/asset/484/intraday?size=500')
json = site['data'].to_json(orient='records')
result = pandas.read_json(json)
ap = pandas.DataFrame(columns=['Data', 'WEG4'])
