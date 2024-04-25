#!/usr/bin/python3

from bs4 import BeautifulSoup

file = open('characters.facx', 'r')

soup =  BeautifulSoup(file, 'xml')

characters = soup.find_all("character")

file.close()

title = "Bienvenido a Fary Adventures"

print(title)
print("="*len(title))
print("\nSelecciona un personaje para mostrar los items\n")

for character in characters:
	print(f"{character['id']}\t {character.find('name').text}")

encontrado = False
while not encontrado:
	id = input("\nInserta el id del personaje elegido: ")

	file = open('characters.facx', 'r')
	soup =  BeautifulSoup(file, 'xml')

	file.close()

	character = soup.find('character', {'id': id})
	if not character:
		print("Error: id no encontrado")
	else:
		encontrado = True

print("Id\t" "Name\t\t" "Age\t" "Level")
print(f"{character['id']}\t {character.find('name').text}\t {character.find('age').text}\t{character.find('level')    ['value']}")



file = open('char_items.facix', 'r')

soup =  BeautifulSoup(file, 'xml')

characters_items = soup.find_all("character_item")

items_ids = []

for character_item in characters_items:
	id_character = character_item.find("character")["id"]

	if id_character == id:
		
		id_item = character_item.find("item")["id"]

		items_ids.append(id_item)
if len(items_ids) <= 0:
	print("El personaje no tiene items")
	exit()

file = open('item.faix', 'r')
soup =  BeautifulSoup(file, 'xml')
file.close()
items = soup.find_all('item', {'id': True})

print("\tItems:")

for item in items:
	if item['id'] in items_ids:
		print("\t\t"+item.find("item").text)

	print("="*len(title))





