# ALONE - PYTHON VERSION

import os
import sys
import subprocess
import random

from random import choice
from termcolor import colored
from pyfiglet import Figlet

from Event import event
from AddEvent import addEvent
from Loot import loot
from ExcelExtractor import excelExtractor

class Alone:
    def __init__(self):
        self.actionNumber = 0
        self.zone = "intro"
        self.nextEvent = "intro1"
        # Player
        self.live = True
        self.backpack = {}
        self.health = 10
        self.maxHealth = 10
        self.oxygen = 20
        self.maxOxygen = 20
    
    def synopsis(self):
        """Display the game's synopsis"""

        custom_fig = Figlet(font="graffiti")
        print(custom_fig.renderText("Alone"))
        print("_____________________________________\n\n")
        print("Vous vous réveillez, au milieu de débris épars, dans ce qui semblait être une salle de conférence. De gros morceaux du plafond sont tombés à quelques mettre de vous, mais l'événement semble déjà ancien. N'étiez vous pas en train de travailler au laboratoire quelques secondes auparavant ? Que s'est-il passé ? Tout semble différent ici jusqu'à l'air qui, étonnamment, à une saveur étrange...")
        input("\nEntrez pour commencer.")
        os.system('cls' if os.name == 'nt' else 'clear') # Clear the terminal

    def alone(self):
        """Start the game"""

        while self.live == True:
            os.system('cls' if os.name == 'nt' else 'clear') # Clear the terminal
            
            # Update data
            self.actionNumber += 1

            # Disoplay the diary and the backpack
            printBackpack = ""
            for x in self.backpack:
                printBackpack = printBackpack + ", " + self.backpack[x]["name"]
            printBackpack = printBackpack[2:]
            if printBackpack == "":
                printBackpack = "vide"

            if self.zone == "intro":
                print("Vie : " + colored(f'{self.health}', 'green') + f"/{self.maxHealth}")
                print("Sac à dos : " + colored(printBackpack, "yellow"))
            else:
                print("Vie : " + colored(f'{self.health}', 'green') + f"/{self.maxHealth}, Oxygène : " + colored(f"{self.oxygen}", "cyan") + f"/{self.maxOxygen}")
                print("Sac à dos : " + colored(printBackpack, "yellow"))

            print("\033[1m" + "\nJournal de bord - Action n°" + str(self.actionNumber) + "\n" + "\033[0m")

        # Event
            # eventType
            if self.nextEvent == None:
                eventType = "random"
            else:
                eventType = "script"
            # eventNumber
            if self.nextEvent == None:
                eventNumber = random.choice(list(event[f"{self.zone}"][f"{eventType}"].keys()))
            else:
                eventNumber = self.nextEvent
            # Print event text
            print(event[f"{self.zone}"][f"{eventType}"][f"{eventNumber}"]["text"]+"\n")

            # Print event actions
            numberOfActions = 0
            for x in event[f"{self.zone}"][f"{eventType}"][f"{eventNumber}"]["actions"]:
                numberOfActions += 1
                if len(event[f"{self.zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][x]["require"]) != 0:
                    nbOfGoodItem = 0
                    nbOfItemRequire = len(event[f"{self.zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][x]["require"])
                    for requireElement in event[f"{self.zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][x]["require"]:
                        if requireElement in list(self.backpack):
                            nbOfGoodItem += 1
                    if nbOfGoodItem == nbOfItemRequire:
                        objectRequire = ""
                        for y in event[f"{self.zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action"]["require"]:
                            objectRequire = objectRequire + ", " + self.backpack[y]["name"]
                        objectRequire = objectRequire[2:]
                        print(str(numberOfActions) + ") " + colored(f"[Nécessite l'utilisatin de : {objectRequire}] ", "red")+ event[f"{self.zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][x]["description"])
                    else:
                        print(str(numberOfActions) + ") " + colored("[Nécessite un objet non possédé]", "red"))
                else:
                    print(str(numberOfActions) + ") " + event[f"{self.zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][x]["description"])

            # Choose the action
            x = True
            while x == True:
                choice = input("\nQue faire ? ")
                try:
                    choice = int(choice)
                    if (choice > 0) and (choice <= len(event[f"{self.zone}"][f"{eventType}"][f"{eventNumber}"]["actions"])):
                        if len(event[f"{self.zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["require"]) != 0:
                            nbOfGoodItem = 0
                            nbOfItemRequire = len(event[f"{self.zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["require"])
                            for requireElement in event[f"{self.zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["require"]:
                                if requireElement in list(backpack):
                                    nbOfGoodItem += 1
                            if nbOfGoodItem == nbOfItemRequire:
                                for listOfRequireElement in event[f"{self.zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["require"]:
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
            print("\n" + event[f"{self.zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["next_message"])

        # Consequences
            # Health
            if event[f"{self.zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["health"] != 0:
                lastHealth = self.health
                self.health = self.health + event[f"{self.zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["health"]
                if self.health > lastHealth:
                    print(colored("\n+" + str(event[f"{self.zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["health"]) + " point(s) de santé", "green"))
                    if self.health > self.maxHealth:
                        self.health = self.maxHealth
                else:
                    print(colored("\n"+ str(event[f"{self.zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["health"]) + " point(s) de santé", "red"))
                    if self.health <= 0:
                        itemIndex = -1
                        for x in self.backpack:
                            itemIndex += 1
                            if self.backpack[x]["health"] > 0:
                                self.health = self.health + self.backpack[x]["health"]
                                print(colored("\nUtilisation de votre objet " + x["name"], "green"))
                                print(colored("+" + str(x["health"]) + " point(s) de santé", "green"))
                                if self.health > self.maxHealth:
                                    self.health = self.maxHealth
                                del self.backpack[itemIndex]
                                break
                        if self.health <= 0:
                            print(colored("\n\nVOUS ETES MORT !\n", "red"))
                            print("Appuyez sur entrée pour quitter")
                            input()
                            sys.exit()

            # Oxygen
            if event[f"{self.zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["oxygen"] != 0:
                lastOxygen = self.oxygen
                self.oxygen = self.oxygen + event[f"{self.zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["oxygen"]
                if self.oxygen > lastOxygen:
                    print(colored("\n+" + str(event[f"{self.zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["oxygen"]) + " point(s) d'oxygène", "green"))
                    if self.oxygen > self.maxOxygen:
                        self.oxygen = self.maxOxygen
                else:
                    print(colored("\n"+ str(event[f"{self.zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["oxygen"]) + " point(s) d'oxygène", "red"))
                    if self.oxygen <= 0:
                        itemIndex = -1
                        for x in self.backpack:
                            itemIndex += 1
                            if self.backpack[x]["oxygen"] > 0:
                                self.oxygen = self.oxygen + self.backpack[x]["oxygen"]
                                print(colored("\nUtilisation de votre objet " + x["name"], "cyan"))
                                print(colored("+" + str(x["oxygen"]) + " point(s) de santé", "cyan"))
                                if self.oxygen > self.maxOxygen:
                                    self.oxygen = self.maxOxygen
                                del self.backpack[itemIndex]
                                break
                        if self.oxygen <= 0:
                            print(colored("\n\nVOUS ETES MORT !\n", "red"))
                            print("Appuyez sur entrée pour quitter")
                            input()
                            sys.exit()

            # Script
            if len(event[f"{self.zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["script"]) > 0:
                self.nextEvent = random.choice(event[f"{self.zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["script"])
            else:
                self.nextEvent = None

            # Loot
            if len(event[f"{self.zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["loot"]) > 0:
                for x in event[f"{self.zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["loot"]:
                    if x in self.backpack:
                        print(colored("\nVous avez trouvé : " + loot[f"{x}"]["name"]+".\nVous possédez déjà cet objet.", "yellow"))
                    else:
                        self.backpack[f"{x}"] = loot[f"{x}"]
                        print(colored("\nVous avez trouvé : " + loot[f"{x}"]["name"] +".", "yellow"))
                        if loot[f"{x}"]["maxHealth"] != 0:
                            self.maxHealth = self.maxHealth + loot[f"{x}"]["maxHealth"]
                            lastHealth = self.health
                            self.health = self.health + loot[f"{x}"]["maxHealth"]
                            if self.health > lastHealth:
                                if self.health > self.maxHealth:
                                    self.health = self.maxHealth
                            print(colored("\n+" + str(loot[f"{x}"]["maxHealth"]) + " point(s) de santé maximum", "green"))
                        if loot[f"{x}"]["maxOxygen"] != 0:
                            self.maxOxygen = self.maxOxygen + loot[f"{x}"]["maxOxygen"]
                            lastOxygen = self.oxygen
                            self.oxygen = self.oxygen + loot[f"{x}"]["maxOxygen"]
                            if self.oxygen > lastHealth:
                                if self.oxygen > self.maxOxygen:
                                    self.health = self.maxOxygen
                            print(colored("\n+" + str(loot[f"{x}"]["maxOxygen"]) + " point(s) d'oxygène maximum", "green"))

            # Add
            if len(event[f"{self.zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["add"]) != 0:
                for x in event[f"{self.zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["add"]:
                    event[f"{x[0]}"][f"{x[1]}"][f"{x[2]}"] = addEvent[f"{x[2]}"]

            # Zone
            if event[f"{self.zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["zone"] != None:
                tempZone = event[f"{self.zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["zone"]
            else:
                tempZone = self.zone

            # Remove
            if len(event[f"{self.zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["remove"]) != 0:
                for x in event[f"{self.zone}"][f"{eventType}"][f"{eventNumber}"]["actions"][f"action{choice}"]["remove"]:
                    try:
                        del event[f"{x[0]}"][f"{x[1]}"][f"{x[2]}"]
                    except:
                        pass # The element has already been deleted

            # Change zone
            self.zone = tempZone

        # Click to pass the event
            input("\nAppuyez sur entrée pour continuer.")


if __name__ == '__main__':
    excelExtractor()
    main = Alone()
    main.synopsis()
    main.alone()