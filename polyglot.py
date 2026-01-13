import time
import random

vowels = ""
consonants = ""
rules = []
languages=["Wookie","Klingon","Vulcan","Mando'a","Romulan/Rihannsu"]
def setWookie():
    print("Wookie")
    global vowels
    global consonants
    global rules

    vowels = "OUA"
    consonants = "WWRRRHHHWWWRR"
    rules = ["CvvvvC", "CVC", "VVCV", "VCVVVVC","VCVVC"]




def mkword():
    rule = rules[random.randrange(len(rules))]
    word = ""
    for i in range(len(rule)):
        r=rule[i]
        if r == "V":
            word = word + pickChar(vowels)
        if r == "v":
            if (random.randrange(100)>49):
                word = word + pickChar(vowels)
        if r == "C":
            con = pickChar(consonants)
            if (con == "g" and lang == 2):
                con = "gh"
            word = word + con
        if r == "c":
            if (random.randrange(100)>49):
                con = pickChar(consonants)
                if (con == "g" and lang == 2):
                    con = "gh"
                word = word + con

    return word

def printForm(instring):
    out = ""
    for x in instring.split():
        out = out + " " + x
        if len(out) >= 65:
            print(out)
            out = ""
    if out != "":
        print(out)
    print()

def setKlin():
    global vowels
    global consonants
    global rules
    print("Klingon")
    vowels = "aeIouy"
    consonants = "bcDgHjlmnpqQStvwy'"
    rules = ["CVVC", "CVC", "CCVVC", "CVVC","CV"]

def setVul():
    print("Vulcan")
    global vowels
    global consonants
    global rules

    vowels = "'iaei'uaiyaoia"
    consonants = "whltrkltkt'khthtrvttsnzh"
    rules = ["CVcvcv", "Cvcv", "Ccv", "Cvvcv","CvVccvcv"]


def setMando():
    print("Mando'a")
    global vowels
    global consonants
    global rules

    vowels = "ouaaoaaaaeaeeeauiueaaeaeeaeoaeeaoaeooeaeaaeaeeeaeueeaieaaaoeeieiioaiaiaiae"
    consonants = "slstryshlntryshlntddthnhntcrcrtryshshtryshlnsh'''''''rslrl't'tdtd'tsh'hnshhn'tsh'cshk'tlsr'chkrvrrsrmsrmrdsnrrnrnrmjycrmjyc"

    rules = ["Cvvc", "CvCvC", "vCCvc", "cvVvCv","cvCCvc"]

def setRom():
    print("Romulan")
    global vowels
    global consonants
    global rules

    vowels = "'eiueeeiia''"
    consonants = "skfhvhlnvhdhmnhl'rh"

    rules = ["cvCCv", "cvVCv", "cVvCC", "cvVvCv","cVvCCv"]
def pickChar(inp):
    return (inp[random.randrange(len(inp))])


def file_len(filename):
    with open(filename) as f:
        for i, _ in enumerate(f):
            pass
    return i + 1

def wisdom(num,filename):
    global REPL
    qs = open(filename)
    for i in range(num+1):
        quote = qs.readline()
    printForm(quote)
    qs.close()
    return quote

lines = file_len("sagan")
setWookie()
lang=1
while True:

    for i in range(7): print()

    dict = {}
    num = random.randrange(lines)
    print("\n\nEnglish\n-----------")
    quote = wisdom(num,"sagan")
    quote = quote.lower()
    q = ""
    for c in quote:
        if c >= "a" and c<="z":
            q = q+c
        else:
            q = q+ " "
    for w in q.split():
        dict[w] = mkword()
    t = ""
    for w in q.split():
        t = t + " " + dict[w]

    print(languages[lang-1]+"\n--------------------------")
    printForm(t)
    print ("\n\n\n\n\n\n\n\n\n")
    time.sleep(20)

    lang = random.randrange(5)+1


    if lang == 1:
        setWookie()

    if lang == 2:
        setKlin()

    if lang == 3:
        setVul()

    if lang == 4:
        setMando()

    if lang == 5:
        setRom()

    time.sleep(.25)
