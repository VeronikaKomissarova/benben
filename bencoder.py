import re
import string
import json

# 1-res 2-ост строка
#di45eli45e4:aaaaee

class bencoder:
    def __init__(self):
        self.strin= input('your bencode string:')
        result,rem_str = self.read(self.strin)
        result_list = []

        while rem_str:
            result_list.append(result)
            result,rem_str = self.read(rem_str)
        if(result_list):
            result_list.append(result)
            print(self.encode(result_list))
        else:
            if (type(result).__name__.replace("'","") =='str'):
                result= "'"+str(result)+"'"
            print(self.encode(result))
    def read(self,str):
        if str.startswith("i"):
            match = re.match("i(-?\\d+)e", str)
            res = int(match.group(1))
            str = str[match.span()[1]:]
            return res,str

        elif str.startswith ("l"):
            list=[]
            rest = str[1:]
            while not rest.startswith("e"):
                element, rest = self.read(rest)
                list.append(element)
            rest=rest[1:] # delete last e from list
            return list,rest

        elif str.startswith("d"):
            dict={}
            rest=str[1:]
            while not rest.startswith("e"):
                key, rest = self.read(rest)
                value, rest = self.read(rest)
                dict[key]=value
            rest=rest[1:]
            return dict,rest

        elif str[0].isdigit():
            match = re.match("(\\d+)", str)
            lenght = int(match.group(1))
            str = str[match.span()[1]+1:]
            string=  str[:lenght]
            str=str[lenght:]
            return string, str
        else:
            raise IOError("Неверный ввод")
    def encode(self,string):
        print('Your JSON string:')
        res = str(string).replace("\'","\"")
        #res = res.replace("[","[\n").replace("]","\n]").replace("{","{\n").replace("}","\n}")
        return res

if __name__ == "__main__":
    p=bencoder()