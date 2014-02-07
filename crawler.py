#-*- coding:utf-8 -*-

'''
	necessária a instalação do pacote BeautifulSoup
'''

from bs4 import BeautifulSoup
import urllib2


url_page = "http://liturgiadiaria.cnbb.org.br/app/user/user/UserView.php"

'''
	Carrega a página da liturgia diária pela dia especificado nos parametros.
'''

def load_content_page(url,dia, mes, ano):
	try:
		page = urllib2.urlopen(url+"?ano="+str(ano)+"&mes="+str(mes)+"&dia="+str(dia))
	except Exception, e:
		print "Erro ao abrir a url"
		raise e

	soap = BeautifulSoup(page)
	#retorna um objeto do tipo BeautifulSoup
	return soap


def capture_leituras(soap):
	leituras = []

	for title_read in soap.find_all(id="titulo"):
	    leituras.append(title_read.string.strip())

	# Remove a reflexão e deixa apenas as leituras        
	leituras.pop(len(leituras)-1)

	#retorna um array de leituras.
	return leituras

'''
	capturar a cor liturgica do dia.
'''
def captura_cor(Soap):
	text = Soap.find(id="informacao_extra").ul.li.string.strip()
	cor = text[:text.find(".")]
	return cor


soap2 = load_content_page(url_page,07, 02, 2014)

print capture_leituras(soap2)

print captura_cor(soap2)

