from typing import Final
import globals as gs
en="0abcdefghijklmnopqrstuvwxyz"
x="0dmtwsilruyqnkfejcazbpgxohv"
y="0hqzgpjtmoblncifdyawveusrkx"
z="0untlsqzfmrehdpxkibvygjcwoa"
refl="0qyhognecvpuztfdjaxwmkisrbl"
x2="0rtqaonvyfpmgblxukhecizdwjs"
y2="0rjmpuodanfykhliebxwgvtszqc"
z2="0zrwmkhulqvpdibynfjecasxotg"
dic={"x":x,"x2":x2,"y":y,"y2":y2,"z":z,"z2":z2}
gs._init()
rotor_setting:list=gs.get_value("rotor_setting") # type: ignore
ko=gs.get_value('ko')
kt=gs.get_value('kt')
kc=gs.get_value('kc')
def set_up(message:str):
    global ko,kt,kc,rotor_setting
    for i in range(0,len(message),2):
        if i<5:
            rotor_setting.append(message[i])
        else:
            rotor_setting.append(message[10-i]+"2")
    for i in range(0,len(rotor_setting)):
        rotor_setting[i]=dic[rotor_setting[i]]
    rotor_setting.insert(3,refl)
    ko=int(message[6])
    kt=int(message[8])
    kc=int(message[10])
    gs.set_value("rotor_setting",rotor_setting)
    gs.set_value("ko",ko)
    gs.set_value("kt",kt)
    gs.set_value("kc",kc)
    return
def reset():
    global ko,kt,kc,rotor_setting
    rotor_setting=[]
    ko=kt=kc=0
    gs.set_value("rotor_setting",rotor_setting)
    gs.set_value("ko",ko)
    gs.set_value("kt",kt)
    gs.set_value("kc",kc)
    return

