import random,math,os,sys
sys.path.insert(0, os.getcwd() + "/Libs")
# custom libraries
import ui
version = "v0001"

def MainMenu():
    ui.Menu(["Dive In","Tavern","Settings"],"Ye Olde Menu",True)

MainMenu()
