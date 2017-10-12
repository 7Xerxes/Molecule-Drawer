import turtle as t;t.width(2);t.speed(0);t.ht();res=(1000,1000)#Importing turtle, setting the settings up correctly - defining resolution so screen will scale. Ignore the comprehensions... they work, trust me.

#Defining functions to draw bonds, double bonds or atoms
def dot(c,symbol):t.penup();t.goto(c[0],c[1]);t.pendown();t.write(symbol.upper(),align="center",font=("Arial",int(((res[0]+res[1])/2)/1000)*10,"normal"))
def line(c,c2):t.penup();t.width(2);t.goto(c[0],c[1]);t.pendown();t.goto(c2[0],c2[1])
def doublelineX(c,c2):
    for x in [((x*2)-1)*3 for x in range(2)]:t.penup();t.width(2);t.goto(c[0],c[1]+x);t.pendown();t.goto(c2[0],c2[1]+x)
def doublelineY(c,c2):
    for x in [((x*2)-1)*3 for x in range(2)]:t.penup();t.width(2);t.goto(c[0]+x,c[1]);t.pendown();t.goto(c2[0]+x,c2[1])
    
#Input A: Recieving and formatting input
prefixes = tuple("meth,eth,prop,but,pent,hex,hept,oct,non,dec".split(","))
a = input("Input molecule name:\n>>> ").lower().replace(" ","")
info = 'I got nothing, man.'

#Input B: Detecting type of molecule and numeric values (amount of carbons)
for x in ("a","e"):
    if a.replace(x+"ne","") in prefixes:info = ("alk"+x+"ne",prefixes.index(a.replace(x+"ne",""))+1)
if info[0] == "alkene" and info[1] == 1:info = 'I got nothing, man.'
if a.replace("anol","") in prefixes:info = ("alcohol",prefixes.index(a.replace("anol",""))+1)
if a.replace("anoicacid","") in prefixes:info = ("carboxylic acid",prefixes.index(a.replace("anoicacid","")))
if [x in prefixes for x in a.replace("yl",",").replace("anoate","").split(",")] == [True, True]:
    info = ("ester",[prefixes.index(x) + 1 for x in a.replace("yl",",").replace("anoate","").split(",")])

#Defining the structure of the molecule based upon the input. 'N' denotes a space - a fix for an early bug where 2 atoms in a column followed by 3 would cause a diagonal line connecting their middles.
if info[0] == "alkane":runtime = ["h"]+[["h","c","h"] for x in range(info[1])]+["h"]
elif info[0] == "alkene":runtime = ["hch","Nch"]+[["h","c","h"] for x in range(info[1]-2)]+["h"]
elif info[0] == "alcohol":runtime = ["h"]+[["h","c","h"] for x in range(info[1])]+["o","h"]
elif info[0] == "ester":runtime = ["h"]+[["h","c","h"] for x in range(info[1][1]-1)]+[["N","c","o"],"o"]+[["h","c","h"] for x in range(info[1][0])]+["h"]

#Caculating coordinates of every atom based upon the structure
coords=[]
for x in range(len(runtime)):
    ygap = res[1]/(len(runtime[x]));xgap=res[1]/(len(runtime));xgap=ygap=sorted((xgap,ygap))[0];log=[]
    for y in range(len(runtime[x])):log.append((((xgap*x)-((len(runtime)-1)*xgap)/2,(ygap*y)-((len(runtime[x])-1)*ygap)/2)))
    coords.append(log)

#Printing out the information figured by the code, 'cause it looks really cool   
print(info)
for x in coords:print(x,len(x))

#Drawing the molecule by iterating through coords[the coordinate list] and runtime[the atom name list] (with appropriate exceptions for double bonds and spacing in runtime)
for x in range(len(runtime)):
    for y in range(len(runtime[x])):
        if runtime[x][y] != "N":dot(coords[x][y],runtime[x][y])
        if runtime[x] == ["N","c","o"] and runtime[x][y] == "c":
            doublelineY([z+[-0.6,25][q] for q,z in enumerate(coords[x][y])],[z+[-0.6,-10][q] for q,z in enumerate(coords[x][y+1])])
        elif y < len(runtime[x])-1 and runtime[x][y] != "N":
            line([z+[-0.6,25][q] for q,z in enumerate(coords[x][y])],[z+[-0.6,-10][q] for q,z in enumerate(coords[x][y+1])])
    if x == 0 and info[0] == "alkene": #The first horizontal bond for an alkene is replaced with a double bond
        doublelineX([z+[20,7][q] for q,z in enumerate(coords[x][int((len(coords[x])+1)/2)-1])],[z+[-20,7][q] for q,z in enumerate(coords[x+1][int((len(coords[x+1])+1)/2)-1])])
    elif x < len(coords)-1:#It must fall short of the final atom horizontally, as otherwise the code would attempt to draw a line from the final atom to the one 'after' it (thus causing an index error)
        line([z+[20,7][q] for q,z in enumerate(coords[x][int((len(coords[x])+1)/2)-1])],[z+[-20,7][q] for q,z in enumerate(coords[x+1][int((len(coords[x+1])+1)/2)-1])])

#Consider this v1.0 of the code. Carboxylic acids will require something of an overhaul, likely an added section of code to cater for its quirks. As such, they are left out of the first iteration of this
#code. That said, I have finalised Alkanes and Alkanes (you will notice cheeky time saving in their detection on line 15); Alcohols (simple mutations on Alkanes), and Esters (rather a combination of required
#exceptions in other molecule types). As you can see, this code is commented - if lightly - to help you understand, if not the finer points, the general structure of the code. Carobxylic acids are on their way.

## -J

