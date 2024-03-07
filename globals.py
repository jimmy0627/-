def _init():
    global glo_dic
    glo_dic={"rotor_setting":[],'ko':0,"kt":0,'kc':0}
def set_value(name, value):
    glo_dic[name] = value

def get_value(name, defValue=None):
    try:
        return glo_dic[name]
    except KeyError:
        return defValue