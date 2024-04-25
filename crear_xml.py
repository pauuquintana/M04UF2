#!/usr/bin/python3


from bs4 import BeautifulSoup

soup = BeautifulSoup(features='xml')

etiqueta = soup.new_tag('cosa', id=1)

print(etiqueta)

print("-------------")


otra_cosa = soup.new_tag('otra_cosa', value="papafrita")

otra_cosa.string = "esto es el texto de otra cosa"

etiqueta.append(otra_cosa)

print(etiqueta)

print("-------------")

soup.append(etiqueta)

(soup.prettify())

file = open("cosa.xml", "w")

file.write(soup.prettify())

file.close()



