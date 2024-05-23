#!/usr/bin/python3

from bs4 import BeautifulSoup

file = open('characters.facx', 'r')

soup =  BeautifulSoup(file, 'xml')

characters = soup.find_all("character")

file.close()

title = "Bienvenido a Fary Adventures"

print(title)
print("="*len(title))

print("\nQue quieres hacer?\n")
print("1- Seleccionar\n")
print("2- Eliminar\n")

eleccion = input("\nEscribe 1 o 2: ")

if eleccion == '1':

	print("\nSelecciona un personaje para empezar a jugar\n")

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



	file = open('char_weapons.facwx', 'r')

	soup =  BeautifulSoup(file, 'xml')

	file.close()

	characters_weapons = soup.find_all('character_weapon')

	id_char_weap = []

	for character_weapon in characters_weapons:
		id_character = character_weapon.find("character")["id"]
		if id_character == id:
			id_weapon = character_weapon.find("weapon")["id"]
			id_char_weap.append(id_weapon)


	if len(id_char_weap) <= 0:
		print("El personaje no tiene armas")
		exit()

	file = open('weapons.fawx', 'r')

	soup = BeautifulSoup(file, 'xml')

	file.close()

	weapons = soup.find_all('weapon', {'id':True})
	damage = 0

	for weapon in weapons:
		if weapon['id'] in id_char_weap:
			damage = damage + int(weapon.find('damage')['value'])
	

	print("Id\t" "Name\t\t" "Age\t" "Level\t" "Damage")


	print(f"{character['id']}\t {character.find('name').text}\t {character.find('age').text}\t{character.find('level')['value']}\t {damage}")

elif eleccion == '2':

	print("\nSelecciona un personaje para eliminar\n")

	for character in characters:
		print(f"{character['id']}\t {character.find('name').text}")

	encontrado = False
	while not encontrado:
		id = input("\nInserta el id del personaje: ")

		dead_character = soup.find('character', {'id': id})
		

		if not dead_character:
			print("Error: id no encontrado")
		else:
			dead_character.decompose()
			encontrado = True

	with open('characters.facx', 'w') as file:
		file.write(str(soup))
	

	characters = soup.find_all("character")

	for character in characters:
		print(f"{character['id']}\t {character.find('name').text}")



