##Imports Exports##
import os
import sys
import time
import string
##Imports Exports##

##PRESET VARIABLES##
systemwait = 0.2
loadingwait = 0.1
filewait = 0.05
bar = "============================"
value = 1
path_apps = "C:\\apps"
path_hddgames = "E:\Games"
path_ssdgames = "F:\\"
path_externalhdd = "G:\\"
dirs = os.listdir(path_apps)
games = ['DyingLight', '~BNet~', 'Civilization',
         'Fallout4', 'GTA5', 'Mafia', 'MirrorsEdge',
         'ShadowWarrior', '~Steam~', 'BDO', 'BlackOps3'
         , 'FIFA17', 'TheForest', 'CSGO', 'Overwatch']
system = ['Afterburner', 'Chrome', 'Discord', 'Malwarebytes', 'Razer',
          'Terminal', 'Settings', 'CCleaner']
correctresponse1 = "games"
correctresponse2 = "system"
def displaygames():
    time.sleep(systemwait)
    print(bar)
    for i in games:
        print(">", i)
        time.sleep(filewait)

def displayos():
    time.sleep(systemwait)
    print(bar)
    for i in system:
        print(">", i)
        time.sleep(filewait)
##PRESET VARIABLES##

print(bar)
time.sleep(loadingwait)
print("Here are the available commands:")
time.sleep(loadingwait)
for file in dirs:
    filename = file
    time.sleep(filewait)
    print(value, ">", os.path.splitext(os.path.basename(filename))[0])
    value = value + 1
print(bar)
time.sleep(loadingwait)
print("Type < games > to highlight available videogames.")
time.sleep(loadingwait)
print("Type < system > to highlight all OS applications.")
time.sleep(loadingwait)
print("Folders: < apps > < hdd > < ssd >")
time.sleep(systemwait)
print(bar)

while True:
    response = input(str("Command: "))
    
    while response not in ['games', 'system', 'apps', 'hdd', 'ssd', 'storage']:
        print("Valid commands are < games> < system > ")
        response = input(str("Command: "))
        
    if response == correctresponse1:
        displaygames()
        
    if response == correctresponse2:
        displayos()

    if response == 'apps':
        os.startfile(path_apps)
    if response == 'hdd':
        os.startfile(path_hddgames)
    if response == 'ssd':
        os.startfile(path_ssdgames)
    if response == 'storage':
        os.startfile(path_externalhdd)
    
