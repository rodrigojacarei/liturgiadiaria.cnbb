#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import urllib2

url = "http://liturgiadiaria.cnbb.org.br/app/user/user/UserView.php"

page = urllib2.urlopen(url)
soap = BeautifulSoup(page)

leituras = []
 
for title_read in soap.find_all(id="titulo"):
    leituras.append(title_read.string.strip())
    print title_read.string.strip()
# REmove a reflexão e deixa apenas as leituras        
leituras.pop(len(leituras)-1)

leituras_texto = []

for title_read2 in soap.find_all(id="texto"):
    leituras_texto.append(title_read2)
    print title_read2
# REmove a reflexão e deixa apenas as leituras     
leituras_texto.pop(len(leituras_texto)-1)   


