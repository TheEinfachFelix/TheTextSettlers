import textQuelle


import os
import keyboard
import time

from rich.console import Console

console = Console()
debug = 0

class Game:
    def __init__(self, pcharacter, pvars) -> None:
        self.mycharacter = pcharacter
        self.myVars = pvars

        self.quBuffer = ""

    def varSet(self, pname, pvar, pprint = False):
        """this function can set vars

        [   ["gold","rw",3465],
            ["name","r and or w for read / write permission",value],  
        ]

        Args:
            pname (string): the name of the var
            pvar (string): the new value
        """
        for i in self.myVars:
            if i[0] == pname: # check if it has the right name
                if "w" in i[1]: # check for perm
                     # set value
                    if pprint and i[3] != "":
                        oldval = self.varGet(pname)
                        newVal = pvar
                        change = newVal - oldval
                        #print(i[3])
                        
                        self.runText(["say","game",i[3]])
                    i[2] = pvar
                else:
                    print(f"->{i[0]}<- ->{i[1]}<- no perms") # i[0] is name  i[1] is perms
                return
        print(f"->{pname}<- coud not be found in var list")
    
    def varGet(self, pname):
        """get the value of a var

        [   ["gold","rw",3465],
            ["name","r and or w for read / write permission",value],  
        ]

        Args:
            pname (string): name of the var

        Returns:
            any: returns the value of the var
        """
        for i in self.myVars: 
            if i[0] == pname: # check if it has the right name
                if "r" in i[1]:# check for perm
                    return i[2] # return value
                else:
                    print(f"->{i[0]}<- ->{i[1]}<- no perms") # i[0] is name  i[1] is perms 
                return
        print(f"->{pname}<- coud not be found in var list")
        

    def characterSay(self, pname, pstring):
        """
        this function searches the characterlist and then prints the pstring message with the name and style infos as fond in the list

        characterlist formate exampe:
        [
            ["Tim",[[rgb(50,200,190)] Tim:[/rgb(50,200,190)]", "rgb(150,255,255)"]],
            ["name of char",["you can do every thing here maybe say the name ot the char", "style infos for the message more styte infos can be set in the message"]],
        ]

        Args:
            pname (string): name of the char
            pstring (string): what ever you want the char to say
        """
        for i in self.mycharacter:
            if i[0] == pname:
                console.print(i[1][0],pstring,style=i[1][1])
                return
        print(f"->{pname}<- coud not be found in character list")

    def poll(self, ptext, pOptions):
        console.print(ptext , style="rgb(0,100,255)")
        for index,element in enumerate(pOptions):
            console.print(f"[rgb(0,100,255)]{index+1}:[/rgb(0,100,255)]",element,style="rgb(50,200,255)")
        while 1:
            for i,v in enumerate(pOptions):
                if keyboard.is_pressed(i+2) or keyboard.is_pressed("num "+str(i+1)):
                    return i+1

    def playMission(self, pMission):
        for abschnitt in pMission:
            self.runText(abschnitt)
    1
    def runText(self, pinput):
        if self.quBuffer == "":
            self.quBuffer = pinput
        match pinput[0]:
            case "clear":
                if debug:
                    os.system('cls')
                else:
                    print("cleared")
                pass
            case "retry":
                self.runText(["wait"])
                self.runText(["clear"])
                self.runText(self.quBuffer)
            case "say":
                self.characterSay(pinput[1],pinput[2])
                # wait after say
                if len(pinput) <=3:
                    self.runText(["wait"])
                else:
                    self.runText(["wait",pinput[3]])
            case "poll":
                self.quBuffer = pinput
                x = self.poll(pinput[1][0],pinput[1][1])
                for next in pinput[1][2][x-1]:
                    self.runText(next)
            case "exit":
                exit()
            case "wait":
                if len(pinput) <= 1:
                    waitTime = 0.5
                else:
                    waitTime = pinput[1]
                if debug:
                    time.sleep(waitTime)
            case "set":
                oldval = self.varGet(pinput[1])
                change = pinput[2]
                newVal = oldval + change
                self.varSet(pinput[1],newVal,True)
            case _:
                print(f'error in "Game.runText" with ->{pinput}<-')

def testVarsandChars():
    
    myGame.characterSay("dario","ich bin Dario")
    myGame.characterSay("erek","ich bin Erek")
    myGame.characterSay("pilgrim","ich bin Pilgrim")
    myGame.characterSay("pilli","ich bin Pilgrim")
    myGame.characterSay("game","dasa ist ein test")
    myGame.varSet("gold",5)
    myGame.varSet("seed",5)
    myGame.varSet("test",5)
    print(myGame.varGet("gold"))
    print(myGame.varGet("seed"))
    print(myGame.varGet("test"))
    print(myGame.poll("das ist ein test", ["option a", "option b"]))







if __name__ == "__main__":
    myGame = Game(textQuelle.setupCharacter, textQuelle.setupVars)
    #testVarsandChars()
    myGame.playMission(textQuelle.intro)