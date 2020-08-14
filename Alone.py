# ALONE V2

import os
import sys
from termcolor import colored
import random
from random import choice
import subprocess
import pyfiglet
from pyfiglet import Figlet

import Event
from Event import event
import AddEvent
from AddEvent import addEvent
import Loot
from Loot import loot
import ExcelExtractor
from ExcelExtractor import excelExtractor

# Variables

actionNumber = 0
zone = "intro"
nextEvent = "intro1"

# Player
live = True
backpack = {}
health = 10
maxHealth = 10
oxygen = 20
maxOxygen = 20

# Run excelExtraxtor
excelExtractor()

# Synopsis
custom_fig=Figlet(font="graffiti")
print(custom_fig.renderText("Alone"))
print("_____________________________________\n\n")
print("Vous vous réveillez, au milieu de débris épars, dans ce qui semblait être une salle de conférence. De gros morceaux du plafond sont tombés à quelques mettre de vous, mais l'événement semble déjà ancien. N'étiez vous pas en train de travailler au laboratoire quelques secondes auparavant ? Que s'est-il passé ? Tout semble différent ici jusqu'à l'air qui, étonnamment, à une saveur étrange...")
input("\nEntrez pour commencer.")
os.system('cls' if os.name == 'nt' else 'clear') # Clear the terminal

while live == True:
	os.system('cls' if os.name == 'nt' else 'clear') # Clear the terminal
	# Variables
	actionNumber += 1

	# Diary and backpack
	printBackpack = ""
	for x in backpack:
		printBackpack = printBackpack + ", " + backpack[x]["name"]
	printBackpack = printBackpack[2:]
	if printBackpack == "":
		printBackpack = "vide"

	if zone == "intro":
		print("Vie : " + colored(f'{health}', 'green') + f"/{maxHealth}")
		print("Sac à dos : " + colored(printBackpack, "yellow"))
	else:
		print("Vie : " + colored(f'{health}', 'green') + f"/{maxHealth}, Oxygène : " + colored(f"{oxygen}", "cyan") + f"/{maxOxygen}")
		print("Sac à dos : " + colored(printBackpack, "yellow"))

	print("\033[1m" + "\nJournal de bord - Action n°" + str(actionNumber) + "\n" + "\033[0m")

# Event
	# eventType
	if nextEvent == None:
		eventType = "random"
	else:
		eventType = "script"
	# eventNumber
	if nextEvent == None:
		eventNumber = random.choice(list(event[f"{zone}"][f"{eventType}"].keys()))
	else:
		eventNumber = nextEvent
	# Print event text
	print(event[f"{zone}"][f"{eventType}"][f"{eventNumber}"]["text"]+"\n")

	# Print event actions
	numberOfActions = 0
	for x in event[f"{zone}"][f"{eventType}"][f"{eventNumber}"]["actions"]:
		numberOfActions += 1
		if len(event[f"{zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][x]["require"]) != 0:
			nbOfGoodItem = 0
			nbOfItemRequire = len(event[f"{zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][x]["require"])
			for requireElement in event[f"{zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][x]["require"]:
				if requireElement in list(backpack):
					nbOfGoodItem += 1
			if nbOfGoodItem == nbOfItemRequire:
				objectRequire = ""
				for y in event[f"{zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["require"]:
					objectRequire = objectRequire + ", " + backpack[y]["name"]
				objectRequire = objectRequire[2:]
				print(str(numberOfActions) + ") " + colored(f"[Nécessite l'utilisatin de : {objectRequire}] ", "red")+ event[f"{zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][x]["description"])
			else:
				print(str(numberOfActions) + ") " + colored("[Nécessite un objet non possédé]", "red"))
		else:
			print(str(numberOfActions) + ") " + event[f"{zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][x]["description"])

	# Choose the action
	x = True
	while x == True:
		choice = input("\nQue faire ? ")
		try:
			choice = int(choice)
			if (choice > 0) and (choice <= len(event[f"{zone}"][f"{eventType}"][f"{eventNumber}"]["actions"])):
				if len(event[f"{zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["require"]) != 0:
					nbOfGoodItem = 0
					nbOfItemRequire = len(event[f"{zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["require"])
					for requireElement in event[f"{zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["require"]:
						if requireElement in list(backpack):
							nbOfGoodItem += 1
					if nbOfGoodItem == nbOfItemRequire:
						for listOfRequireElement in event[f"{zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["require"]:
							del backpack[listOfRequireElement]
							x = False
					else:
						print("Vous ne possèdez pas tous les objets nécessaires pour effectuer cette action.")
				else:
					x = False
			else:
				print("Choix inexistant")
		except:
			print("Choix inexistant")

	# Print next_message
	print("\n" + event[f"{zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["next_message"])

# Consequences
	# Health
	if event[f"{zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["health"] != 0:
		lastHealth = health
		health = health + event[f"{zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["health"]
		if health > lastHealth:
			print(colored("\n+" + str(event[f"{zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["health"]) + " point(s) de santé", "green"))
			if health > maxHealth:
				health = maxHealth
		else:
			print(colored("\n"+ str(event[f"{zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["health"]) + " point(s) de santé", "red"))
			if health <= 0:
				itemIndex = -1
				for x in backpack:
					itemIndex += 1
					if backpack[x]["health"] > 0:
						health = health + backpack[x]["health"]
						print(colored("\nUtilisation de votre objet " + x["name"], "green"))
						print(colored("+" + str(x["health"]) + " point(s) de santé", "green"))
						if health > maxHealth:
							health = maxHealth
						del backpack[itemIndex]
						break
				if health <= 0:
					print(colored("\n\nVOUS ETES MORT !\n", "red"))
					print("Appuyez sur entrée pour quitter")
					input()
					sys.exit()

	# Oxygen
	if event[f"{zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["oxygen"] != 0:
		lastOxygen = oxygen
		oxygen = oxygen + event[f"{zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["oxygen"]
		if oxygen > lastOxygen:
			print(colored("\n+" + str(event[f"{zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["oxygen"]) + " point(s) d'oxygène", "green"))
			if oxygen > maxOxygen:
				oxygen = maxOxygen
		else:
			print(colored("\n"+ str(event[f"{zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["oxygen"]) + " point(s) d'oxygène", "red"))
			if oxygen <= 0:
				itemIndex = -1
				for x in backpack:
					itemIndex += 1
					if backpack[x]["oxygen"] > 0:
						oxygen = oxygen + backpack[x]["oxygen"]
						print(colored("\nUtilisation de votre objet " + x["name"], "cyan"))
						print(colored("+" + str(x["oxygen"]) + " point(s) de santé", "cyan"))
						if oxygen > maxOxygen:
							oxygen = maxOxygen
						del backpack[itemIndex]
						break
				if oxygen <= 0:
					print(colored("\n\nVOUS ETES MORT !\n", "red"))
					print("Appuyez sur entrée pour quitter")
					input()
					sys.exit()

	# Script
	if len(event[f"{zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["script"]) > 0:
		nextEvent = random.choice(event[f"{zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["script"])
	else:
		nextEvent = None

	# Loot
	if len(event[f"{zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["loot"]) > 0:
		for x in event[f"{zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["loot"]:
			if x in backpack:
				print(colored("\nVous avez trouvé : " + loot[f"{x}"]["name"]+".\nVous possédez déjà cet objet.", "yellow"))
			else:
				backpack[f"{x}"] = loot[f"{x}"]
				print(colored("\nVous avez trouvé : " + loot[f"{x}"]["name"] +".", "yellow"))
				if loot[f"{x}"]["maxHealth"] != 0:
					maxHealth = maxHealth + loot[f"{x}"]["maxHealth"]
					lastHealth = health
					health = health + loot[f"{x}"]["maxHealth"]
					if health > lastHealth:
						if health > maxHealth:
							health = maxHealth
					print(colored("\n+" + str(loot[f"{x}"]["maxHealth"]) + " point(s) de santé maximum", "green"))
				if loot[f"{x}"]["maxOxygen"] != 0:
					maxOxygen = maxOxygen + loot[f"{x}"]["maxOxygen"]
					lastOxygen = oxygen
					oxygen = oxygen + loot[f"{x}"]["maxOxygen"]
					if oxygen > lastHealth:
						if oxygen > maxOxygen:
							health = maxOxygen
					print(colored("\n+" + str(loot[f"{x}"]["maxOxygen"]) + " point(s) d'oxygène maximum", "green"))

	# Add
	if len(event[f"{zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["add"]) != 0:
		for x in event[f"{zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["add"]:
			event[f"{x[0]}"][f"{x[1]}"][f"{x[2]}"] = addEvent[f"{x[2]}"]

	# Zone
	if event[f"{zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["zone"] != None:
		tempZone = event[f"{zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["zone"]
	else:
		tempZone = zone

	# Remove
	if len(event[f"{zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["remove"]) != 0:
		for x in event[f"{zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["remove"]:
			try:
				del event[f"{x[0]}"][f"{x[1]}"][f"{x[2]}"]
			except:
				pass # The element has already been deleted

	# Change zone
	zone = tempZone

# Click to pass the event
	input("\nAppuyez sur entrée pour continuer.")