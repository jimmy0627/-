from pickle import TRUE
from set import *
import globals as gl
rotor_setting=gl.get_value("rotor_setting")
ko=gl.get_value("ko")
kt=gl.get_value("kt")
kc=gl.get_value("kc")

def dismean(code:str,rotor_setting,ko,kt,kc):
    key_setting=[kt,kc,0,0,-kc,-kt,-ko]
    index=en.find(code.lower())+ko
    def dismean_2(index):
        for i in range(0,8):
            if index>26:index-=26
            elif index<=0:index+=26
            if i==7:break
            word=rotor_setting[i][index]
            index=en.find(word)+key_setting[i]
        return en[index]
    return dismean_2(index)
    

def dismean_3(code,rotor_setting,ko,kt,kc):
    dark=''
    for i in range(0,len(code)):
        temp=str(code[i])
        if temp.isalpha()==True:
            dark+=dismean(temp,rotor_setting,ko,kt,kc)
        else:dark+=temp
        ko+=1
        if ko>26:
            ko-=26
            kt+=1
        if kt>26:
            kt-=26
            kc+=1
        if kc>26:
            kc-=26   
    return dark
