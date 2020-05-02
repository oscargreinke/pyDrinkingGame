import random
import os

def toBoolio(st):
    return st.lower() == "True"

class piccoloPrompt():
    def __init__(self, prompt, virus=None, excludeCouples=False): #virus will be end string
        self.prompt = prompt
        self.virus = virus
        if self.virus == "":
            self.virus = None
        self.exclude = excludeCouples

    def valid(self,p1,p2):
        for couple in couples:
           if p1 in couple and p2 in couple:
                return False
        return True

    def display(self):
        used = []
        adisplay = ""
        special = 0
        delay = 0
        global viruses
        for i in range(0, len(self.prompt)-0):
            if delay > 0:
                delay -= 1
            else:
                letter = self.prompt[i]
                if letter == '@':
                    special = 1
                elif letter == '%':
                    special = 2
                if special == 0:
                    adisplay += letter
                elif special == 1:
                    while True:
                        potentialName = players[random.randint(0, len(players)-1)]
                        if potentialName not in used:
                            nvalid = True
                            if len(used) != 0 and self.exclude:
                                for person in used:
                                    if not self.valid(person,potentialName):
                                        nvalid = False
                                        break
                            if nvalid:
                                adisplay += potentialName
                                used.append(potentialName)
                                break
                elif special == 2:
                    adisplay += str(random.randint(int(self.prompt[i+1]), int(self.prompt[i+2])))
                    i += 2
                    delay = 2
                special = 0
        if self.virus:
            adisplay = "VIRUS!\n"+adisplay
            virusText = ""
            for letter in self.virus:
                if letter != "@":
                    virusText += letter
                else:
                    virusText += used[0]
                    used = used[1:]
            viruses.append(virusText)
        input(adisplay)
        
def loadPrompts():
    versions = ["normal"]
    version = input("What version? (Normal): ")
    if version.lower() not in versions:
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAH")
        print(version.lower())
    else:
        prm = open(version+".txt", "r").read().split("\n")
        pram = []
        for item in prm:
            pram.append(item.split("#"))
        print("{} loaded.".format(version))
        return pram
                
        
players = ["player1", "player2"]
couples = [[],[]]
viruses = []
prompts = []
prompts = loadPrompts()
#for ele in prompts:
    #print(ele)
nprompts = []
for prompt in prompts:
    if len(prompt) == 1:
        nprompts.append(piccoloPrompt(prompt[0]))
    elif len(prompt) == 2:
        nprompts.append(piccoloPrompt(prompt[0],prompt[1]))
    else:
        nprompts.append(piccoloPrompt(prompt[0],prompt[1],toBoolio(prompt[2])))
prompts = nprompts
virusCount = 0

while len(prompts) > 0:
    aprompt = prompts[random.randint(0, len(prompts)-1)]
    prompts.remove(aprompt)
    aprompt.display()
    if len(viruses) != 0:
        if random.randint(1, 10) < virusCount:
            input("!<"+viruses[0]+">!")
            viruses = viruses[1:]
            virusCount = 0
        else:
            virusCount += 1
while len(viruses) >0:
    input("!<"+viruses[0]+">!")
    viruses = viruses[1:]












