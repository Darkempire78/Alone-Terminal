import xlrd
import ast
import json
import codecs

# Help
#http://www.python-simple.com/python-autres-modules-non-standards/xlrd.php

def excelExtractor():
    # Read excel file
    eventTable = xlrd.open_workbook('event_table.xlsx', encoding_override="utf8")

# EVENT
    # Get sheet
    sheet = eventTable.sheet_by_index(0)

    event = {}

    # Get action number
    actionNumber = 0
    line = 1

    while line <= (sheet.nrows - 2): # line number
        line += 1

        # Zone
        zone = sheet.cell(line, 0)
        type = sheet.cell(line, 1)
        if zone.value in event.keys():
            pass
        else:
            event[f'{zone.value}'] = {"script": {}, "random": {}}

        # Action 1
        description1 = sheet.cell(line, 4)
        next_message1 = sheet.cell(line, 5)
        health1 = sheet.cell(line, 6)
        oxygen1 = sheet.cell(line, 7)
        loot1 = sheet.cell(line, 8)
        add1 = sheet.cell(line, 9)
        remove1 = sheet.cell(line, 10)
        script1 = sheet.cell(line, 11)
        zone1 = sheet.cell(line, 12)
        require1 = sheet.cell(line, 13)

        # Check if second action exists
        secondDescription = sheet.cell(line, 14)

        if len(sheet.row_values(line)) > 14 and secondDescription.value != "":
            actionNumber = 2

            # Action 2
            description2 = sheet.cell(line, 14)
            next_message2 = sheet.cell(line, 15)
            health2 = sheet.cell(line, 16)
            oxygen2 = sheet.cell(line, 17)
            loot2 = sheet.cell(line, 18)
            add2 = sheet.cell(line, 19)
            remove2 = sheet.cell(line, 20)
            script2 = sheet.cell(line, 21)
            zone2 = sheet.cell(line, 22)
            require2 = sheet.cell(line, 23)
        else:
            actionNumber = 1

        # Get cells
        name = sheet.cell(line, 2)
        text = sheet.cell(line, 3)

        event[zone.value][type.value][name.value] = {} # Create event
        event[zone.value][type.value][name.value]["text"] = text.value # Add text
        event[zone.value][type.value][name.value]["actions"] = {} # Add actions dict

        # If more than or 1 action
        if actionNumber >= 1:
            event[zone.value][type.value][name.value]["actions"]["action1"] = {} # Add action1 dict
            # Description
            event[zone.value][type.value][name.value]["actions"]["action1"]["description"] = description1.value
            # Next_message
            event[zone.value][type.value][name.value]["actions"]["action1"]["next_message"] = next_message1.value
            # Health
            event[zone.value][type.value][name.value]["actions"]["action1"]["health"] = int(health1.value)
            # Oxygen
            event[zone.value][type.value][name.value]["actions"]["action1"]["oxygen"] = int(oxygen1.value)
            # Loot
            if loot1.value == "":
                event[zone.value][type.value][name.value]["actions"]["action1"]["loot"] = []
            else:
                event[zone.value][type.value][name.value]["actions"]["action1"]["loot"] = loot1.value.split(", ")
            # Add
            if add1.value == "":
                event[zone.value][type.value][name.value]["actions"]["action1"]["add"] = []
            else:
                event[zone.value][type.value][name.value]["actions"]["action1"]["add"] = ast.literal_eval(add1.value)
            # Remove
            if remove1.value == "":
                event[zone.value][type.value][name.value]["actions"]["action1"]["remove"] = []
            else:
                event[zone.value][type.value][name.value]["actions"]["action1"]["remove"] = ast.literal_eval(remove1.value)
            # Script
            if script1.value == "":
                event[zone.value][type.value][name.value]["actions"]["action1"]["script"] = []
            else:
                event[zone.value][type.value][name.value]["actions"]["action1"]["script"] = script1.value.split(", ")
            # Zone
            if zone1.value == "None" or zone1.value == "":
                event[zone.value][type.value][name.value]["actions"]["action1"]["zone"] = None
            else:
                event[zone.value][type.value][name.value]["actions"]["action1"]["zone"] = zone1.value
            # Require
            if require1.value == "":
                event[zone.value][type.value][name.value]["actions"]["action1"]["require"] = []
            else:
                event[zone.value][type.value][name.value]["actions"]["action1"]["require"] = require1.value.split(", ")

        # If more than or 2 actions
        if actionNumber >= 2:
            event[zone.value][type.value][name.value]["actions"]["action2"] = {} # Add action2 dict
            # Description
            event[zone.value][type.value][name.value]["actions"]["action2"]["description"] = description2.value
            # Next_message
            event[zone.value][type.value][name.value]["actions"]["action2"]["next_message"] = next_message2.value
            # Health
            event[zone.value][type.value][name.value]["actions"]["action2"]["health"] = int(health2.value)
            # Oxygen
            event[zone.value][type.value][name.value]["actions"]["action2"]["oxygen"] = int(oxygen2.value)
            # Loot
            if loot2.value == "":
                event[zone.value][type.value][name.value]["actions"]["action2"]["loot"] = []
            else:
                event[zone.value][type.value][name.value]["actions"]["action2"]["loot"] = loot2.value.split(", ")
            # Add
            if add2.value == "":
                event[zone.value][type.value][name.value]["actions"]["action2"]["add"] = []
            else:
                event[zone.value][type.value][name.value]["actions"]["action2"]["add"] = ast.literal_eval(add2.value)
            # Remove
            if remove2.value == "":
                event[zone.value][type.value][name.value]["actions"]["action2"]["remove"] = []
            else:
                event[zone.value][type.value][name.value]["actions"]["action2"]["remove"] = ast.literal_eval(remove2.value)
            # Script
            if script2.value == "":
                event[zone.value][type.value][name.value]["actions"]["action2"]["script"] = []
            else:
                event[zone.value][type.value][name.value]["actions"]["action2"]["script"] = script2.value.split(", ")
            # Zone
            if zone2.value == "None"  or zone2.value == "":
                event[zone.value][type.value][name.value]["actions"]["action2"]["zone"] = None
            else:
                event[zone.value][type.value][name.value]["actions"]["action2"]["zone"] = zone2.value
            # Require
            if require2.value == "":
                event[zone.value][type.value][name.value]["actions"]["action2"]["require"] = []
            else:
                event[zone.value][type.value][name.value]["actions"]["action2"]["require"] = require2.value.split(", ")

    # write python file with data
    with codecs.open("data/Event.py",'w', "utf-8") as file:
        data = json.dumps(event, indent = 4, ensure_ascii=False)
        data = data.replace("null", "None")
        file.write("event = "+ data)

# LOOT
    # Get sheet
    lootSheet = eventTable.sheet_by_index(2)

    loot = {}

    # Get action number
    line = 0

    while line <= (lootSheet.nrows - 2): # line number
        line += 1

        # codeName
        codeName = lootSheet.cell(line, 0)
        # name
        name = lootSheet.cell(line, 1)
        # health
        health = lootSheet.cell(line, 2)
        # oxygen
        oxygen = lootSheet.cell(line, 3)
        # maxHealth
        maxHealth = lootSheet.cell(line, 4)
        # maxOxygen
        maxOxygen = lootSheet.cell(line, 5)

        # Add to loot
        loot[codeName.value] = {}

        # name
        loot[codeName.value]["name"] = name.value
        # health
        loot[codeName.value]["health"] = int(health.value)
        # oxygen
        loot[codeName.value]["oxygen"] = int(oxygen.value)
        # maxHealth
        loot[codeName.value]["maxHealth"] = int(maxHealth.value)
        # maxOxygen
        loot[codeName.value]["maxOxygen"] = int(maxOxygen.value)

    # write python file with data
    with codecs.open("data/Loot.py",'w', "utf-8") as file:
        data = json.dumps(loot, indent = 4, ensure_ascii=False)
        data = data.replace("null", "None")
        file.write("loot = "+ data)


# ADD EVENT
    # Get sheet
    addEventSheet = eventTable.sheet_by_index(1)

    addEvent = {}

    # Get action number
    line = 1

    while line <= (addEventSheet.nrows - 2): # line number
        line += 1

        # Action 1
        description1 = addEventSheet.cell(line, 4)
        next_message1 = addEventSheet.cell(line, 5)
        health1 = addEventSheet.cell(line, 6)
        oxygen1 = addEventSheet.cell(line, 7)
        loot1 = addEventSheet.cell(line, 8)
        add1 = addEventSheet.cell(line, 9)
        remove1 = addEventSheet.cell(line, 10)
        script1 = addEventSheet.cell(line, 11)
        zone1 = addEventSheet.cell(line, 12)
        require1 = addEventSheet.cell(line, 13)

        # Check if second action exists
        secondDescription = addEventSheet.cell(line, 14)

        if len(addEventSheet.row_values(line)) > 14 and secondDescription.value != "":
            # Action 2
            actionNumber = 2
            description2 = addEventSheet.cell(line, 14)
            next_message2 = addEventSheet.cell(line, 15)
            health2 = addEventSheet.cell(line, 16)
            oxygen2 = addEventSheet.cell(line, 17)
            loot2 = addEventSheet.cell(line, 18)
            add2 = addEventSheet.cell(line, 19)
            remove2 = addEventSheet.cell(line, 20)
            script2 = addEventSheet.cell(line, 21)
            zone2 = addEventSheet.cell(line, 22)
            require2 = addEventSheet.cell(line, 23)
        else:
            actionNumber = 1

        # Get cells
        name = addEventSheet.cell(line, 2)
        text = addEventSheet.cell(line, 3)

        addEvent[name.value] = {} # Create event
        addEvent[name.value]["text"] = text.value # Add text
        addEvent[name.value]["actions"] = {} # Add actions dict

        # If more than or 1 action
        if actionNumber >= 1:
            addEvent[name.value]["actions"]["action1"] = {} # Add action1 dict
            # Description
            addEvent[name.value]["actions"]["action1"]["description"] = description1.value
            # Next_message
            addEvent[name.value]["actions"]["action1"]["next_message"] = next_message1.value
            # Health
            addEvent[name.value]["actions"]["action1"]["health"] = int(health1.value)
            # Oxygen
            addEvent[name.value]["actions"]["action1"]["oxygen"] = int(oxygen1.value)
            # Loot
            if loot1.value == "":
                addEvent[name.value]["actions"]["action1"]["loot"] = []
            else:
                addEvent[name.value]["actions"]["action1"]["loot"] = loot1.value.split(", ")
            # Add
            addEvent[name.value]["actions"]["action1"]["add"] = ast.literal_eval(add1.value) if add1.value else []
            # Remove
            addEvent[name.value]["actions"]["action1"]["remove"] = ast.literal_eval(remove1.value)  if remove1.value else []
            # Script
            if script1.value == "":
                addEvent[name.value]["actions"]["action1"]["script"] = []
            else:
                addEvent[name.value]["actions"]["action1"]["script"] = script1.value.split(", ")
            # Zone
            if zone1.value == "None"  or zone1.value == "":
                addEvent[name.value]["actions"]["action1"]["zone"] = None
            else:
                addEvent[name.value]["actions"]["action1"]["zone"] = zone1.value
            # Require
            if require1.value == "":
                addEvent[name.value]["actions"]["action1"]["require"] = []
            else:
                addEvent[name.value]["actions"]["action1"]["require"] = require1.value.split(", ")

        # If more than or 2 actions
        if actionNumber >= 2:
            addEvent[name.value]["actions"]["action2"] = {} # Add action2 dict
            # Description
            addEvent[name.value]["actions"]["action2"]["description"] = description2.value
            # Next_message
            addEvent[name.value]["actions"]["action2"]["next_message"] = next_message2.value
            # Health
            addEvent[name.value]["actions"]["action2"]["health"] = int(health2.value)
            # Oxygen
            addEvent[name.value]["actions"]["action2"]["oxygen"] = int(oxygen2.value)
            # Loot
            if loot2.value == "":
                addEvent[name.value]["actions"]["action2"]["loot"] = []
            else:
                addEvent[name.value]["actions"]["action2"]["loot"] = loot2.value.split(", ")
            # Add
            addEvent[name.value]["actions"]["action2"]["add"] = ast.literal_eval(add2.value) if add2.value else []
            # Remove
            addEvent[name.value]["actions"]["action2"]["remove"] = ast.literal_eval(remove2.value) if remove2.value else []
            # Script
            if script2.value == "":
                addEvent[name.value]["actions"]["action2"]["script"] = []
            else:
                addEvent[name.value]["actions"]["action2"]["script"] = script2.value.split(", ")
            # Zone
            if zone2.value == "None"  or zone2.value == "": 
                addEvent[name.value]["actions"]["action2"]["zone"] = None
            else:
                addEvent[name.value]["actions"]["action2"]["zone"] = zone2.value
            # Require
            if require2.value == "":
                addEvent[name.value]["actions"]["action2"]["require"] = []
            else:
                addEvent[name.value]["actions"]["action2"]["require"] = require2.value.split(", ")

    # write python file with data
    with codecs.open("data/AddEvent.py",'w', "utf-8") as file:
        data = json.dumps(addEvent, indent = 4, ensure_ascii=False)
        data = data.replace("null", "None")
        file.write("addEvent = "+ data)
