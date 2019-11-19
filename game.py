import random,math,os,sys,glob
sys.path.insert(0, os.getcwd() + "/Libs")
# custom libraries
import ui
version = "v0001"
player_body = []
parts = []
materials = []
bodies = []
enemies = []
### MOD DATA                                ###
# [0] = ID                                     
# [1] = data - split into further unsorted list
###                                         ###
def Get_Property(data,_property):
    for d in data:
        dsLite = d.split(":")
        if dsLite[0].lower() == _property:
            return dsLite[1]
    return None
def Tavern():
    raise Exception("TBA")
def Settings():
    raise Exception("TBA")
def LoadGame():
    pass
def SaveGame():
    pass
def LoadModFiles():
    files = glob.glob("Mods/*/*.txt")
    
def Setup():
    pass

def Game():
    LoadModFiles()
    Setup()
    LoadGame()
    
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


