#!/usr/bin/python3

from bs4 import BeautifulSoup

file = open('characters.facx', 'r')

soup =  BeautifulSoup(file, 'xml')

characters = soup.find_all("character")

file.close()

title = "Bienvenido a Fary Adventures"

print(title)
print("="*len(title))

print("\nQue quieres hacer?\n?")
print("\n1- Seleccionar\n")
print("\n2- Eliminar\n")

eleccion = input("\nEscribe 1 o 2: ")

if eleccion == 1:

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

	print("Id\t" "Name\t\t" "Age\t" "Level")


	print(f"{character['id']}\t {character.find('name').text}\t {character.find('age').text}\t{character.find('level')['value']}")

	
elif eleccion == 2:

	print("\nSelecciona un personaje para eliminarr\n")

	for character in characters:
		print(f"{character['id']}\t {character.find('name').text}")

	encontrado = False
	while not encontrado:
		id = input("\nInserta el id del personaje: ")

		file = open('characters.facx', 'r')

		soup =  BeautifulSoup(file, 'xml')

		file.close()

		character = soup.find('character', {'id': id})
	
		if not character:
			print("Error: id no encontrado")
		else:
			encontrado = True

	print("Id\t" "Name\t\t" "Age\t" "Level")


	print(f"{character['id']}\t {character.find('name').text}\t {character.find('age').text}\t{character.find('level')['value']}")





