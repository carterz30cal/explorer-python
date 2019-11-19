import random,math,os,sys
sys.path.insert(0, os.getcwd() + "/Libs")
# custom libraries
import ui
version = "v0001"
player_body = []


def Tavern():
    raise Exception("TBA")
def Settings():
    raise Exception("TBA")
def Game():
    pass
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


