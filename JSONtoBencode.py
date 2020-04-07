import re
import string

'''
b 1/0 e - boolean (True or False)
'''
#{"fff":123,[123,"gty",true]:"fdfd"}
class JSONtoBencode:
    def __init__(self):
        self.strin = input('your JSON string:')
        result,rem_str = self.read(self.strin)
        print(result)


    def read(self,inputstr):
        if inputstr.startswith("{"):
            rest = inputstr[1:]
            result='d'
            while not (rest.startswith("}")):
                key,rest = self.read(rest)
                result+=key
                if rest.startswith(":"):
                    rest=rest[1:]
                value,rest=self.read(rest)
                result+=value
                if rest.startswith(","):
                    rest=rest[1:]
            if(rest):
                rest=rest[1:]
            result+='e'
            return result,rest

        if inputstr.startswith("\""):
            #inputstr=inputstr[1:] #delete \"
            match=re.match('\\"(.*?)\\"',inputstr)
            result=str(match.group(1))
            lenght = len(result)
            result=str(lenght)+':'+result
            inputstr = inputstr[match.span()[1]:]
            return result, inputstr

        if inputstr.startswith("["):
            rest=inputstr[1:]
            result = 'l'
            while not (rest.startswith("]")):
                element, rest = self.read(rest)
                if(rest.startswith(",")):
                    rest=rest[1:]
                result+=element
            if (rest):
                rest=rest[1:]
            result+='e'
            return result, rest

        if inputstr[0].isdigit() or inputstr[0]=="-":
            match=re.match("(\-?\\d+\.?\d+)",inputstr)
            result=match.group(1)
            result='i'+result+'e'
            #print('result')
            #print(result)
            inputstr = inputstr[match.span()[1]:]
            #print('inp')
            #print(inputstr)
            return result,inputstr

        if inputstr[:4] =='true':
            rest=inputstr[4:]
            result = 'b1e'
            return result,rest

        if inputstr[:5]=='false':
            rest = inputstr[5:]
            result = 'b0e'
            return result, rest

        if inputstr[:4] =='null':
            return 'n0e', inputstr[4:]





if __name__ == "__main__":
    p=JSONtoBencode()
