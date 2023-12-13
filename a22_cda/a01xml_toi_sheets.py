import xml.etree.ElementTree as ET
from xml.dom import minidom
path_xml = "xml\_xml.xml"
# root = ET.parse(path_xml).getroot()

# nsNFE = {'ns': "http://www.portalfiscal.inf.br/nfe"}


# numero_nfe = root.find("ns:NFe/ns:infNFe/ns:ide/ns:nNF", nsNFE)
# chave = root.find("ns:NFe/ns:infNFe", nsNFE)
# print(chave.attrib)
# print(numero_nfe.text)

with open(path_xml, "rb") as xml:
    nfe = minidom.parse(xml)

cProd = nfe.getElementsByTagName("cProd")

l_cProd = []
for e in cProd:
    l_cProd.append(e.firstChild.nodeValue)
    print(e.firstChild.nodeValue)

print("L_cPrdo\n", l_cProd)

xProd = nfe.getElementsByTagName("xProd")
l_xProd = []
for e in xProd:
    l_xProd.append(e.firstChild.nodeValue)
    print(e.firstChild.nodeValue)

print("l_xProd\n", l_xProd)
