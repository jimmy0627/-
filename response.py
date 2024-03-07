from set import *
from trial import dismean_3

def give(message,rotor_setting,ko,kc,kt):
    print(rotor_setting,ko,kt,kc)
    dark=dismean_3(message,rotor_setting,ko,kt,kc)
    return dark
