#coding:utf-8
from Tkinter import *


import hashlib
#CustomPY
import Helper
import Mod
import Updater
#基础信息
global UpdaterConfig
global ServerMods
global LocalMods
global root
def InitUpdater():
    configFile = open('./Config.json','r')
    #读取Config文件
    UpdaterConfig = json.load(configFile,object_hook=Updater.ConvertUpdaterHook)
    configFile.close()
    UpdaterConfig.LoadServerInfo()
    UpdaterConfig.ServerImage()
    req = urllib2.Request(UpdaterConfig.FilesAddress)
    res_data = urllib2.urlopen(req)
    res = res_data.read()

    ServerMods = []
    LocalMods = []
    for jsonobject in json.loads(res,object_hook=Mod.ConvertModHook):
        ServerMods.append(jsonobject)
    Helper.appendModInfo(LocalMods)
    
    root.title(UpdaterConfig.Name)
    totalLab = Label(root, text= "本地Mods:" +bytes(len(LocalMods)))
    totalLab.pack()
    serverLab = Label(root, text= "服务器Mods:" +bytes(len(ServerMods)))
    serverLab.pack()
    root.iconbitmap('./resources/Server.ico')

if __name__ == "__main__":
    root = Tk()
    root.geometry('320x160')
    InitUpdater()
    root.mainloop()
    #print LocalMods
#print a