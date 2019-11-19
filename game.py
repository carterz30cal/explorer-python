import random,math,os,sys,glob
sys.path.insert(0, os.getcwd() + "/Libs")
# custom libraries
import ui
version = "v0001"
player_body = []
player_choices = []
parts = []
bodies = []
enemies = []
### MOD DATA                                ###
# [0] = ID                                     
# [1] = data - split into further unsorted list
###                                         ###
def TBA(thing):
    raise Exception("TBA - " + thing)
def Get_Property(data,_property):
    for d in data:
        dsLite = d.split("=")
        if dsLite[0].lower() == _property:
            return dsLite[1]
    return None
def Tavern():
    TBA("Tavern")
def Settings():
    TBA("Settings Menu")
def LoadGame():
    TBA("Load game")
def SaveGame():
    TBA("Save game")
def LoadModFiles():
    files = glob.glob("Mods/*/*.txt")
    for f in files:
        fr = open(f,"r")
        frr = fr.read().split(";")
        fr.close()
        for item in frr:
            if item == "":
                continue
            id_data = item.split("{")
            id_data[1] = id_data[1].split(",")
            idtype = id_data[0].split(",")
            if idtype[0] == "part":
                id_data[0] = idtype[1]
                parts.append(id_data)
            elif idtype[0] == "body":
                id_data[0] = idtype[1]
                bodies.append(id_data)
            elif idtype[0] == "enemy":
                id_data[0] = idtype[1]
                enemies.append(id_data)
            elif idtype[0] == "playertype":
                id_data[0] = idtype[1]
                player_choices.append(id_data)
def NewCharacter():
    ch = []
    for item in player_choices:
        ch.append(item[0])
    ui.Menu(ch,"Pick an option",True)
    NewCharacter_Select()
def NewCharacter_Select():
    try:
        select_int = int(input())
        Setup(player_choices[select_int-1][1])
    except ValueError:
        NewCharacter_Select()
def Setup(data):
    TBA("Setup stuff")
def GameMenu():
    ui.Menu(["New Character","Load Game"],"Start afresh or return to old character?",True)
    GameMenu_Select()
def GameMenu_Select():
    try:
        select_int = int(input())
        if select_int == 1:
            NewCharacter()
        elif select_int == 2:
            LoadGame()
        else:
            GameMenu_Select()
    except ValueError:
        GameMenu_Select()
def Game():
    LoadModFiles()
    GameMenu()
def MainMenu():
    ui.Menu(["Dive In","Tavern","Settings"],"Ye Olde Menu",True)
    MainMenu_Select()
def MainMenu_Select():
    try:
        selection_int = int(input())
        if selection_int == 1:
            Game()
        elif selection_int == 2:
            Tavern()
        elif selection_int == 3:
            Settings()
        else:
            MainMenu_Select()
    except ValueError:
        MainMenu_Select()
MainMenu()


