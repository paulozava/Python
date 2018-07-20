import pandas
import datetime

tags = ['KROT3', 'QUAL3', 'CYRE3', 'BTOW3', 'HYPE3', 'LREN3', 'ESTC3', 'ELET6', 'CMIG4', 'RAIL3', 'ELET3', 'SBSP3', 'PETR4', 'TIMP3', 'WEGE3', 'MGLU3', 'ITSA4', 'ITUB4', 'MRVE3', 'BBDC4', 'KLBN11', 'EQTL3', 'PETR3', 'BRFS3', 'ABEV3', 'CCRO3', 'IGTA3', 'RADL3', 'EGIE3', 'SANB11', 'PCAR4', 'FIBR3', 'JBSS3', 'CPLE6', 'VIVT4', 'CPFE3', 'MULT3', 'CIEL3', 'BBDC3', 'MRFG3', 'B3SA3', 'BRKM5', 'BRML3', 'USIM5', 'LAME4', 'RENT3', 'SUZB3', 'FLRY3', 'UGPA3', 'BBAS3', 'TAEE11', 'BBSE3', 'SAPR11', 'NATU3', 'CVCB3', 'EMBR3', 'CSAN3', 'GOAU4', 'VVAR11', 'CSNA3', 'ENBR3', 'SMLS3', 'GGBR4', 'ECOR3', 'GOLL4', 'BRAP4', 'VALE3', 'Ativo', 'KROT3', 'QUAL3', 'CYRE3', 'BTOW3', 'HYPE3', 'LREN3', 'ESTC3', 'ELET6', 'CMIG4', 'RAIL3', 'ELET3', 'SBSP3', 'PETR4', 'TIMP3', 'WEGE3', 'MGLU3', 'ITSA4', 'ITUB4', 'MRVE3', 'BBDC4', 'KLBN11', 'EQTL3', 'PETR3', 'BRFS3', 'ABEV3', 'CCRO3', 'IGTA3', 'RADL3', 'EGIE3', 'SANB11', 'PCAR4', 'FIBR3', 'JBSS3', 'CPLE6', 'VIVT4', 'CPFE3', 'MULT3', 'CIEL3', 'BBDC3', 'MRFG3', 'B3SA3', 'BRKM5', 'BRML3', 'USIM5', 'LAME4', 'RENT3', 'SUZB3', 'FLRY3', 'UGPA3', 'BBAS3', 'TAEE11', 'BBSE3', 'SAPR11', 'NATU3', 'CVCB3', 'EMBR3', 'CSAN3', 'GOAU4', 'VVAR11', 'CSNA3', 'ENBR3', 'SMLS3', 'GGBR4', 'ECOR3', 'GOLL4', 'BRAP4', 'VALE3']


for tag in tags:
    try:
        site = pandas.read_html(f'http://cotacoes.economia.uol.com.br/acao/cotacoes-diarias.html?codigo={tag}.SA&size=500')
        util = site[1]
        util.drop(columns=['VariaÃ§Ã£o', 'VariaÃ§Ã£o (%)', 'MÃ¡ximo', 'MÃ­nimo'], inplace=True)
        util.columns = ['DataHora', 'Cotacao', 'Volume']
        try:
            date_object
        except:
            date_object = util['DataHora'][0]
            date = datetime.datetime.strptime(date_object, '%d/%m/%Y %H:%M')
        finally:
            util.to_csv(f'/home/laumzav/PycharmProjects/Python_study/AlCuOn/Pandas/acoes/Data/{tag}_{date.year}{date.month}{date.day}.csv', index=False)
    except:
        continue