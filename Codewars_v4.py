

import random
import math
import numpy as np
from pygame.sprite import Group
name = "ShadowSyndicate"
print(name)


def replaceChar(string,posn,char):
    return (string[:posn]+char+string[posn+1:])
def islandGetInfo(island, sig):
    a = island*2 - 2
    x = ord(sig[a])
    y = ord(sig[a+1])
    return (x, y)


def updateIslandInfo(island, x, y, sig):
    a = island*2 - 2
    sig = sig[:a]+chr(x)+chr(y) + sig[a+2:]
    return sig
def enemyPresent(pirate):
    posn = pirate.getPosition()
    
    teamSig = str(pirate.getTeamSignal())
    if (abs(posn[0] - ord(teamSig[0])) <= 1 and abs(posn[1] - ord(teamSig[1])) <= 1) or (abs(posn[0] - ord(teamSig[2])) <= 1 and abs(posn[1] - ord(teamSig[3])) <= 1) or (abs(posn[0] - ord(teamSig[4])) <= 1 and abs(posn[1] - ord(teamSig[5])) <= 1):
        data = np.array([[pirate.investigate_nw()[1], pirate.investigate_up()[1], pirate.investigate_ne()[1]], [pirate.investigate_left()[
                        1], pirate.investigate_current()[1], pirate.investigate_right()[1]], [pirate.investigate_sw()[1], pirate.investigate_down()[1], pirate.investigate_se()[1]]])
        data = (data == "enemy")
        # print(data)
        for who in data:
            if who.any() == True:
                return True
    return False



def moveTo(x, y, Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] < y) * 2 + 1
    if position[1] == y:
        return (position[0] > x) * 2 + 2
    if random.randint(1, 2) == 1:
        return (position[0] > x) * 2 + 2
    else:
        return (position[1] < y) * 2 + 1
def moveToChid(x, y, Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] < y) * 2 + 1
    if position[1] == y:
        return (position[0] > x) * 2 + 2
   
    else:
        return (position[1] < y) * 2 + 1

def moveToSexy(x , y , Pirate , type):
    
    position = Pirate.getPosition()
    if type == "xFirst" :
        if position[0] != x:
            return (position[0] > x) * 2 + 2
        else:
            return (position[1] < y) * 2 + 1
    elif type == "yFirst":
        if position[1] != y:
            return (position[1] < y) * 2 + 1
        else:
            return (position[0] > x) * 2 + 2
    elif type == "random":
        if random.randint(1, 2) == 1:
            return (position[0] > x) * 2 + 2
        else:
            return (position[1] < y) * 2 + 1        
    
def inspectForIsland(pirate):
    data = np.array([[pirate.investigate_nw()[0], pirate.investigate_up()[0], pirate.investigate_ne()[0]], [pirate.investigate_left()[
                    0], pirate.investigate_current()[0], pirate.investigate_right()[0]], [pirate.investigate_sw()[0], pirate.investigate_down()[0], pirate.investigate_se()[0]]])
    x, y = pirate.getPosition()
    
    teamsig = pirate.trackPlayers()
    sig = pirate.getTeamSignal()
    for island in range(1, 4):
        if (sig[2*island-2] == chr(255)):
            a = (data == ("island"+str(island)))
            if (a[2][2] and not a[2][1] and not a[1][2]):
                sig = updateIslandInfo(island, x+2, y+2, sig)
            elif (a[2][2] and a[2][1] and not a[2][0]):
                sig = updateIslandInfo(island, x+1, y+2, sig)
            elif (a[2][2] and a[2][1] and a[2][0]):
                sig = updateIslandInfo(island, x, y+2, sig)
            elif (not a[2][2] and a[2][1] and a[2][0]):
                sig = updateIslandInfo(island, x-1, y+2, sig)
            elif (a[2][0] and not a[2][1] and not a[1][0]):
                sig = updateIslandInfo(island, x-2, y+2, sig)
            elif (a[2][0] and a[1][0] and not a[0][0]):
                sig = updateIslandInfo(island, x-2, y+1, sig)
            elif (a[2][0] and a[1][0] and a[0][0]):
                sig = updateIslandInfo(island, x-2, y, sig)
            elif (not a[2][0] and a[1][0] and a[0][0]):
                sig = updateIslandInfo(island, x-2, y-1, sig)
            elif (a[0][0] and not a[0][1] and not a[1][0]):
                sig = updateIslandInfo(island, x-2, y-2, sig)
            elif (a[0][0] and a[0][1] and not a[0][2]):
                sig = updateIslandInfo(island, x-1, y-2, sig)
            elif (a[0][0] and a[0][1] and a[0][2]):
                sig = updateIslandInfo(island, x, y-2, sig)
            elif (not a[0][0] and a[0][1] and a[0][2]):
                sig = updateIslandInfo(island, x+1, y-2, sig)
            elif (a[0][2] and not a[1][2] and not a[0][1]):
                sig = updateIslandInfo(island, x+2, y-2, sig)
            elif (a[0][2] and a[1][2] and not a[2][2]):
                sig = updateIslandInfo(island, x+2, y-1, sig)
            elif (a[0][2] and a[1][2] and a[2][2]):
                sig = updateIslandInfo(island, x+2, y, sig)
            elif (not a[0][2] and a[1][2] and a[2][2]):
                sig = updateIslandInfo(island, x+2, y+1, sig)
    pirate.setTeamSignal(sig)

def CaptureIslands(pirate):
    status = pirate.trackPlayers()
   
    sig = pirate.getTeamSignal()
   
    r = random.randint(1,4)
    
    if (ord(sig[0])!='127'and (status[0]!='myCaptured')):
        x=ord(sig[0]) 
        y=ord(sig[1])
        if r==1:
            x+=1
            y+=1
        if r==2:
            x+=1
            y-=1
        if r==3:
            x-=1
            y-=1
        if r==4:
            x-=1
            y+=1
        return(moveTo(x,y,pirate))
    if (ord(sig[2])!='127'and (status[1]!='myCaptured')):
        x=ord(sig[2]) 
        y=ord(sig[3])
        if r==1:
            x+=1
            y+=1
        if r==2:
            x+=1
            y-=1
        if r==3:
            x-=1
            y-=1
        if r==4:
            x-=1
            y+=1
        return(moveTo(x,y,pirate))
    if (ord(sig[4])!='127'and (status[2]!='myCaptured')):
        x=ord(sig[4]) 
        y=ord(sig[5])
        if r==1:
            x+=1
            y+=1
        if r==2:
            x+=1
            y-=1
        if r==3:
            x-=1
            y-=1
        if r==4:
            x-=1
            y+=1
        return(moveTo(x,y,pirate))
def isSpawned(pirate):
    
    position = pirate.getPosition()
    base = pirate.getDeployPoint()
    if position[0] == base[0] and position[1] == base[1]:
        return True

def spawned(pirate):
    position = pirate.getPosition()
    base = pirate.getDeployPoint()
    if position[0] == base[0] and position[1] == base[1]:
        return (moveTo(pirate.getID()%40 , 0 , pirate))
def ActPirate(pirate):
    
    

    rum=pirate.getTotalRum()
    wood=pirate.getTotalWood()
    gunpowder=pirate.getTotalGunpowder()
    l = pirate.trackPlayers()
    status=pirate.trackPlayers()
    width = pirate.getDimensionX()    
    height = pirate.getDimensionY()
    frame = pirate.getCurrentFrame()
    teamsig = pirate.getTeamSignal()
    deploy = pirate.getDeployPoint()
    selfsig = pirate.getSignal()
    posn = pirate.getPosition()
    id = int(pirate.getID()) % width
    
    


    
    


    if selfsig == "":
        for i in range(20):
            selfsig+=chr(255)
        selfsig = replaceChar(selfsig,0,'e')
    selfsig = replaceChar(selfsig,7,chr(posn[0]))
    selfsig = replaceChar(selfsig,8,chr(posn[1]))
    
    
    
    
     
    selfsig = replaceChar(selfsig,1,chr(0)) 
    if teamsig[17] == 'X' :
        selfsig = replaceChar(selfsig, 3, 'X')
        inspectForIsland(pirate)

        if (selfsig[3] == 'Y'):
            if (posn[1] == (height-1 if not (deploy[1] == 0) else 0)):
                r = random.randint(1, 3)
                if (r == 1 and status[0] != 'myCaptured'):
                    selfsig = replaceChar(selfsig, 3, 'A')
                elif (r == 2 and status[1] != 'myCaptured'):
                    selfsig = replaceChar(selfsig, 3, 'B')
                elif (r == 3 and status[2] != 'myCaptured'):
                    selfsig = replaceChar(selfsig, 3, 'C')
            if (posn[0] == (width-id if deploy[0] == 0 else id-1)):
                finalReturn = moveTo(
                    posn[0], height-1 if not (deploy[1] == 0) else 0, pirate)
            else:
                finalReturn = moveToSexy(
                    (width-id if deploy[0] == 0 else id), (id - 1 if deploy[1] == 0 else deploy[1]+1-id), pirate, "yFirst")
        if (selfsig[3] == 'X'):
            # pirate signal change to C if the pirate has landed where it was intended to
            if (posn[1] == (height-1 if deploy[1] == 0 else 0)):
                selfsig = replaceChar(selfsig, 3, 'Y')
            if (posn[0] == (width-id if deploy[0] == 0 else id-1)):
                finalReturn = moveTo(
                    posn[0], height-1 if deploy[1] == 0 else 0, pirate)
            else:
                finalReturn = moveToSexy((width-id if deploy[0] == 0 else (id-1) % width), ((
                    deploy[1]+id - 1) % width if deploy[1] == 0 else deploy[1]+1-id), pirate, "yFirst")
            # if (finalReturn == 1):
            #     selfsig = replaceChar(selfsig, 2, chr(max(0, posn[1]-1)))
            # elif (finalReturn == 3):
            #     selfsig = replaceChar(selfsig, 2, chr(min(height, (posn[1]+1))))
            # elif (finalReturn == 2):
            #     selfsig = replaceChar(selfsig, 1, chr((min(width, posn[0]+1))))
            # elif (finalReturn == 4):
            #     selfsig = replaceChar(selfsig, 1, chr(max(0, posn[0]-1)))
            pirate.setSignal(selfsig)
            
            
            
            return finalReturn




    
    
    if(teamsig[17]=='C'):
        #print(" ccboy ")
        
        # if(ord(selfsig[1])!=0 and selfsig[0]!='g' and selfsig[0]!='G' and selfsig!='e'):
            
        #     if(teamsig[5+ord(selfsig[1])]=='n'):
        #         selfsig=replaceChar(selfsig,0,'p') # p for protect
        #     if(teamsig[5+ord(selfsig[1])]=='r'):
        #         selfsig=replaceChar(selfsig,0,'r')
        #     if(teamsig[5+ord(selfsig[1])]=='m'):
        #         selfsig=replaceChar(selfsig,0,'p')
        for iii in range(3):
            xisland = ord(teamsig[iii*2])
            yisland = ord(teamsig[iii*2+1])
            #print(xisland,yisland," islandd ")
            if(abs(posn[0]-xisland)<=1 and abs(posn[1]-yisland)<=1 ):
                selfsig = replaceChar(selfsig,1,chr(iii+1))
        
        if(selfsig[0]=='D' or selfsig[0]=='E'):
            if(teamsig[4+2*ord(selfsig[2])]=='c'):
                selfsig=replaceChar(selfsig,0,'G')
            if(teamsig[4+2*ord(selfsig[2])]=='x'):
                selfsig=replaceChar(selfsig,0,'e')
            
        if(ord(selfsig[1])!=0 and((selfsig[0]!='g' and selfsig[0]!='G' ) or ((selfsig[0]=='g' or selfsig[0]=='G') and ord(selfsig[2])==ord(selfsig[1]))) and selfsig[0]!='e' and selfsig[0]!='E' and selfsig[0]!='D'):
            if(teamsig[4+2*ord(selfsig[1])]=='h' or teamsig[4+2*ord(selfsig[1])]=='c'):
                selfsig=replaceChar(selfsig,0,'r')
            if(teamsig[4+2*ord(selfsig[1])]=='m'):
                selfsig=replaceChar(selfsig,0,'p')
            if(teamsig[4+2*ord(selfsig[1])]=='n'):
                selfsig=replaceChar(selfsig,0,'p') # p for protect
        elif(ord(selfsig[1])!=0 and selfsig[0]=='D' and ord(selfsig[2])==ord(selfsig[1])):
            if(teamsig[4+2*ord(selfsig[1])]=='d'):
                selfsig=replaceChar(selfsig,0,'E')
            if(teamsig[4+2*ord(selfsig[1])]=='n' or teamsig[4+2*ord(selfsig[1])]=='m'):
                selfsig=replaceChar(selfsig,0,'p')
            elif(teamsig[4+2*ord(selfsig[1])]=='c'):
                selfsig=replaceChar(selfsig,0,'r')
        
        if(ord(selfsig[1])!=0 and selfsig[0]=='e'):
            if(teamsig[4+2*ord(selfsig[1])]=='h' or teamsig[4+2*ord(selfsig[1])]=='c'):
                selfsig=replaceChar(selfsig,0,'r')
            if(teamsig[4+2*ord(selfsig[1])]=='m'):
                selfsig=replaceChar(selfsig,0,'p')
            
        if(selfsig[0]=='E'):
            
            tempp = ord(selfsig[2])
            yii=ord(teamsig[tempp*2-2+1])
            xii= ord(teamsig[tempp*2-2])
            if(xii<20):
                    xj=xii+5
            else:
                    xj=xii-5
            if(posn[0]==xj and posn[1]==yii):
                selfsig=replaceChar(selfsig,0,'D')


        # id = int(pirate.getID())
        #id = int(pirate.getID())%width

        
        
        if(selfsig[0]=='G'):
            tempp = ord(selfsig[2])
            pirate.setSignal(selfsig)
            return moveToChid(ord(teamsig[tempp*2-2]),ord(teamsig[tempp*2-2+1]),pirate)
        elif(selfsig[0]=='D'):
            tempp = ord(selfsig[2])
            pirate.setSignal(selfsig)
            return moveToChid(ord(teamsig[tempp*2-2]),ord(teamsig[tempp*2-2+1]),pirate)
        elif(selfsig[0]=='E'):
            tempp = ord(selfsig[2])
            xii= ord(teamsig[tempp*2-2])
            if(xii<20):
                    xj=xii+5
            else:
                    xj=xii-5
            pirate.setSignal(selfsig)
            return moveToChid(xj,ord(teamsig[tempp*2-2+1]),pirate)
        elif(selfsig[0]=='p' or selfsig[0]=='r'):
            if(pirate.investigate_current()[1]=='enemy' or pirate.investigate_current()[1]=='both'):
                return moveTo(posn[0],posn[1],pirate)
            elif(pirate.investigate_up()[1]=='enemy' or pirate.investigate_up()[1]=='both'):
                return moveTo(posn[0],posn[1]-1,pirate)
            elif(pirate.investigate_right()[1]=='enemy' or pirate.investigate_right()[1]=='both'):
                return moveTo(posn[0]+1,posn[1],pirate)
            elif(pirate.investigate_down()[1]=='enemy' or pirate.investigate_down()[1]=='both'):
                return moveTo(posn[0],posn[1]+1,pirate)
            elif(pirate.investigate_left()[1]=='enemy' or pirate.investigate_left()[1]=='both'):
                return moveTo(posn[0]-1,posn[1],pirate)
            elif(pirate.investigate_ne()[1]=='enemy' or pirate.investigate_ne()[1]=='both'):
                return moveTo(posn[0]+1,posn[1]-1,pirate)
            elif(pirate.investigate_se()[1]=='enemy' or pirate.investigate_se()[1]=='both'):
                return moveTo(posn[0]+1,posn[1]+1,pirate)
            elif(pirate.investigate_nw()[1]=='enemy' or pirate.investigate_nw()[1]=='both'):
                return moveTo(posn[0]-1,posn[1]-1,pirate)
            elif(pirate.investigate_sw()[1]=='enemy' or pirate.investigate_sw()[1]=='both'):
                return moveTo(posn[0]-1,posn[1]+1,pirate)
            else:
                tempp=ord(selfsig[1])
                tempxi = ord(teamsig[tempp*2-2])
                tempyi =ord(teamsig[tempp*2-2+1])
                if((posn[0]-tempxi)==0):
                    xwhere=random.choice([0,1,-1])
                else:
                    xwhere=random.choice([0,tempxi-posn[0]])
                if((posn[1]-tempyi)==0):
                    ywhere=random.choice([0,1,-1])
                else:
                    ywhere=random.choice([0,tempyi-posn[1]])
                pirate.setSignal(selfsig)
                return moveTo(posn[0]+xwhere,posn[1]+ywhere,pirate)
        # elif(selfsig[0]=='r'):
        #     tempp = ord(selfsig[1])
        #     pirate.setSignal(selfsig)
        #     return moveTo(ord(teamsig[tempp*2-2]),ord(teamsig[tempp*2-2+1]),pirate)

        for jj in range(1,4):
            if(teamsig[4+2*jj]=='h' or teamsig[4+2*jj]=='m' or  teamsig[4+2*jj]=='c'): # 6,7 ,8,9,  10,11 are info about islands, such as ex: h for help, n for normal, m for more
                                        #6,8,10 are letters, 7,9,11 are numbers(nearest wala)  
                xr = ord(teamsig[2*jj-2])
                yr = ord(teamsig[2*jj-2+1])
                if(xr<20):
                    xj=xr+5
                else:
                    xj=xr-5
                if(yr<20):
                    yj=yr+5
                else:
                    yj=yr-5
                distancefromrescuepoint = abs(posn[0]-xj)+abs(posn[1]-yj)
                if( ord(teamsig[5+2*jj])>= distancefromrescuepoint  and (selfsig[0]=='e' or (selfsig[0]=='g' and ord(selfsig[2])==jj)) ):   #r for rescue
                    
                    if(teamsig[12+jj-1]=='y' and selfsig[0]=='g') :  #y for yes , means go
                        

                        if(xj==posn[0] and yj==posn[1]):
                            selfsig=replaceChar(selfsig,0,'G') #g for on way to stacking point, G is reached and now going to island, my logic is first it iterates through all pirates before re entering any pirate, so when it re enters then all 8 pirates have g at end of self sig
                            selfsig=replaceChar(selfsig,2,chr(jj))
                            tempp = ord(selfsig[2])
                            pirate.setSignal(selfsig)
                            return moveToChid(ord(teamsig[tempp*2-2]),ord(teamsig[tempp*2-2+1]),pirate)
                            
                        else:
                            
                            selfsig=replaceChar(selfsig,0,'e') #e for explore
                            selsig=replaceChar(selfsig,2,chr(255))
                    

                            
                    else:
                        
                        selfsig=replaceChar(selfsig,0,'g')
                        selfsig=replaceChar(selfsig,2,chr(jj))
                        pirate.setSignal(selfsig)
                        return moveTo(xj,yj,pirate)  #you can include xi, yi, xj,yj in self signal using ASCII
                elif(ord(teamsig[5+2*jj])< distancefromrescuepoint  and ( selfsig[0]=='g' and ord(selfsig[2])==jj)):
                    selfsig=replaceChar(selfsig,0,'e') #e for explore
                    selsig=replaceChar(selfsig,2,chr(255))
            elif(teamsig[4+2*jj]=='d'):
                xr = ord(teamsig[2*jj-2])
                yr = ord(teamsig[2*jj-2+1])
                if(xr<20):
                    xj=xr+5
                else:
                    xj=xr-5
                yj=yr
                # if(yr<20):  change these later
                #     yj=yr+5
                # else:
                #     yj=yr-5
                distancefromrescuepoint = abs(posn[0]-xj)+abs(posn[1]-yj)
                if( ord(teamsig[5+2*jj])>= distancefromrescuepoint  and (selfsig[0]=='e' or (selfsig[0]=='g' and ord(selfsig[2])==jj)) ):
                    if(teamsig[12+jj-1]=='y' and selfsig[0]=='g') :
                        if(xj==posn[0] and yj==posn[1]):
                                selfsig=replaceChar(selfsig,0,'D') #g for on way to stacking point, D is reached and now going to Disturb and goes to (x,y), E is it returns back to this site (x+5,y)
                                selfsig=replaceChar(selfsig,2,chr(jj))
                                tempp = ord(selfsig[2])
                                pirate.setSignal(selfsig)
                                return moveToChid(ord(teamsig[tempp*2-2]),ord(teamsig[tempp*2-2+1]),pirate)
                        else:
                                
                            selfsig=replaceChar(selfsig,0,'e') #e for explore
                            selsig=replaceChar(selfsig,2,chr(255))
                    else:
                        
                        selfsig=replaceChar(selfsig,0,'g')
                        selfsig=replaceChar(selfsig,2,chr(jj))
                        pirate.setSignal(selfsig)
                        return moveTo(xj,yj,pirate)  #you can include xi, yi, xj,yj in self signal using ASCII
                elif(ord(teamsig[5+2*jj])< distancefromrescuepoint  and ( selfsig[0]=='g' and ord(selfsig[2])==jj)):
                    selfsig=replaceChar(selfsig,0,'e') #e for explore
                    selsig=replaceChar(selfsig,2,chr(255))
            pirate.setSignal(selfsig)
        
        if(selfsig[0]=='e'):
            numberr= random.randint(1,4)
            pirate.setSignal(selfsig)
            return numberr

            
    

def ActTeam(team):
    global n
    n=0
    pirateNumber = team.getTotalPirates()
    rum = team.getTotalRum()
    wood = team.getTotalWood()
    gunpowder = team.getTotalGunpowder()
    signals = team.getListOfSignals()
    l = team.trackPlayers()
    teamsig = team.getTeamSignal()
    width = team.getDimensionX()
    height = team.getDimensionY()
    frame = team.getCurrentFrame()
    status = team.trackPlayers()
    PirateList = team.getListOfSignals()
    
    
    if teamsig == "":
        for i in range(20):
            teamsig += chr(255)
        teamsig = replaceChar(teamsig, 17, 'X')
    if frame >= 130: #change it later
        teamsig = replaceChar(teamsig, 17, 'C')
    
    print(l[3],l[4],l[5]," kallo ")
   # print(ord(teamsig[0]),ord(teamsig[1]),ord(teamsig[2]),ord(teamsig[3]),"teamy")

   
    
    
    
    

    if(teamsig[17]=='C'):
        #print("ccgirl")
        for ii in range(3):
            
            teamsig = checkIslandStatus(PirateList,ii+1,l,teamsig)
        for mm in range(3):
            
            freeguys= 0
            for pirate in PirateList:
              
              if(pirate!="" and pirate[0]=='e'):
                    freeguys+=1
            
            if((l[mm]=="" or l[mm]=="myCapturing") and teamsig[2*mm]!=chr(255) and l[mm+3]==""): #probably change this later
                if(teamsig[6+2*mm]!='c'):
                    
                    teamsig=replaceChar(teamsig,6+2*mm,'c')
                    teamsig = callforhelp(mm+1,6,teamsig,PirateList) #change the callformore function, and change it later: Fine tune the numerical values of how many to call for what
            elif(l[mm+3]=="oppCapturing" and l[mm]=="myCaptured"):
                if(teamsig[6+2*mm]!='d'): # d for disturb , 
                   
                    teamsig=replaceChar(teamsig,6+2*mm,'d')
                    teamsig = callforhelp(mm+1,6,teamsig,PirateList)
            elif(l[mm+3]=="oppCapturing"):
                if(teamsig[6+2*mm]!='d'): # d for disturb , 
                   
                    teamsig=replaceChar(teamsig,6+2*mm,'d')
                    teamsig = callforhelp(mm+1,6,teamsig,PirateList)
            elif(l[mm+3]=="oppCaptured" and teamsig[2*mm]!=chr(127)):
                
                if(freeguys>=18):
                    if(teamsig[6+2*mm]!='c'):
                        teamsig=replaceChar(teamsig,6+2*mm,'c')
                        teamsig = callforhelp(mm+1,8,teamsig,PirateList)
                        break #should I change it later ?


        
        
            
        
        # if(len(PirateList)>=7) and kk==2 :
        #     teamsig = replaceChar(teamsig,9,'r')
        #     teamsig= callforhelp(20,20,6,teamsig,PirateList)
        #     kkk=0 
        for kk in range(3):
            
            if(teamsig[6+2*kk]=='h' or teamsig[6+2*kk]=='m' or teamsig[6+2*kk]=='c' ): #change this later, keep values specific to each thing
                xr = ord(teamsig[2*kk])
                yr = ord(teamsig[2*kk+1])
                if(xr<20):
                    xj=xr+5
                else:
                    xj=xr-5
                if(yr<20):
                    yj=yr+5
                else:
                    yj=yr-5
                if(HowManyHere(xj,yj,PirateList,kk+1)>=6):
                    teamsig=replaceChar(teamsig,12+kk,'y')
            elif(teamsig[6+2*kk]=='d'): #change this later, keep values specific to each thing
                xr = ord(teamsig[2*kk])
                yr = ord(teamsig[2*kk+1])
                if(xr<20):
                    xj=xr+5
                else:
                    xj=xr-5
                yj=yr
                if(HowManyHere(xj,yj,PirateList,kk+1)>=4):
                    teamsig=replaceChar(teamsig,12+kk,'y')
        # kk+=1

    team.setTeamSignal(teamsig)
            
    
        

    

def getnearest(xj,yj,listofsignals,howmany): # rescueteam is a Group() of rescue pirates 



    for r in range(len(listofsignals)):

        if(listofsignals[r]!="" and listofsignals[r][0]=='e' ):  # r for rescue, change its index (10) later
            m+=1
    nearestGroup = [] #list of nearest pirates
    if m>=howmany:
        maxofhowmany = 0 #max distance of 'how many' members from island
        check=0 #just a random name
        for piratenumber in range(len(listofsignals)):
            if(listofsignals[piratenumber]!="" and listofsignals[piratenumber][0]=='e'):
                #print("aa")
                #print(listofsignals[piratenumber])
                x = ord(listofsignals[piratenumber][7])  #change these indexes later
                y = ord(listofsignals[piratenumber][8])  #change these indexes later
                #print(x," ko ",y)
                distanceFromIsland = abs(x-xj)+abs(y-yj)
                if(check>=1):
                    maxofhowmany = nearestGroup[check-1]
                if check<howmany:
                    if(check==0):
                        nearestGroup.append(distanceFromIsland)
                    elif(check==1):
                        if(nearestGroup[0]<=distanceFromIsland):
                            nearestGroup.append(distanceFromIsland)
                        else:
                            nearestGroup.insert(0,distanceFromIsland)
                    else:
                        if(nearestGroup[check-1]<=distanceFromIsland):
                            nearestGroup.append(distanceFromIsland)
                        elif(nearestGroup[0]>=distanceFromIsland):
                            nearestGroup.insert(0,distanceFromIsland)
                        else:
                            for j in range(check-1):
                                
                                if(nearestGroup[j]<=distanceFromIsland and distanceFromIsland<=nearestGroup[j+1]):
                                    nearestGroup.insert(j+1,distanceFromIsland)
                    
                                                    
                    check+=1 
                    
                
                else:      
                    if distanceFromIsland<maxofhowmany:
                        nearestGroup.pop(howmany-1)
                        if(nearestGroup[howmany-2]<=distanceFromIsland):
                            nearestGroup.insert(howmany-1,distanceFromIsland)
                        elif(nearestGroup[0]>=distanceFromIsland):
                            nearestGroup.insert(0,distanceFromIsland)
                        else:
                            for j in range(howmany-2):
                                if(nearestGroup[j]<=distanceFromIsland and distanceFromIsland<=nearestGroup[j+1]):
                                    nearestGroup.insert(j+1,distanceFromIsland)
                               
        return nearestGroup
    else:
       
        nearestGroup.append(18)  #change this later
        return nearestGroup   
def callforhelp(islandnumber,howmany,teamsig,listofsignals):   #remove xi and yi and change it to islandnumber
    xi = ord(teamsig[2*islandnumber-2]) # i for island
    yi = ord(teamsig[2*islandnumber-2+1])
    if(xi<20):
        xj=xi+4
    else:
        xj=xi-4
    if(yi<20):
        yj=yi+4
    else:
        yj=yi-4
    nearestGroup = getnearest(xj,yj,listofsignals,howmany)
    if(len(nearestGroup)!=0):
        maxdistance = nearestGroup[-1]
    else:
        maxdistance=20

    
    
    teamsig=replaceChar(teamsig,5+2*islandnumber,chr(maxdistance))
    return teamsig






def HowManyHereTotal(x,y,listofsignals):  
    n=0
    for piratenumber in range(len(listofsignals)):
        if(listofsignals[piratenumber]!=""):
            xp = ord(listofsignals[piratenumber][7])
            yp = ord(listofsignals[piratenumber][8])
            if xp==x and yp==y:
                n+=1
    return n
def HowManyHere(x,y,listofsignals,islandnumber):  
    n=0
    for piratenumber in range(len(listofsignals)):
        if(listofsignals[piratenumber]!="" and listofsignals[piratenumber][0]=='g' and ord(listofsignals[piratenumber][2])==islandnumber ):
            xp = ord(listofsignals[piratenumber][7])
            yp = ord(listofsignals[piratenumber][8])
            if xp==x and yp==y:
                n+=1
    return n
def checkIslandStatus(listofsignals,islandnumber,islandtrack,teamsig):   
    
        
    xi = ord(teamsig[2*islandnumber-2])
    yi= ord(teamsig[2*islandnumber-2+1])
    if(islandtrack[islandnumber-1]=='myCaptured' and islandtrack[islandnumber+2]=='oppCapturing' ):
        teamsig=replaceChar(teamsig,4+2*islandnumber,'d') 
    elif(islandtrack[islandnumber-1]=='myCaptured'):
        teamsig=replaceChar(teamsig,4+2*islandnumber,'n')
        howMany=0
        for pirate in listofsignals:
            if( pirate!="" and (pirate[0]=='r' or pirate[0]=='p') and pirate[1]==chr(islandnumber)):
                howMany+=1
        if howMany>=2:
            teamsig=replaceChar(teamsig,4+2*islandnumber,'n') #n for normal
        else:
            callforhelp(islandnumber,3,teamsig,listofsignals)
          
            teamsig=replaceChar(teamsig,4+2*islandnumber,'m')  #m for more
    if(teamsig[4+2*islandnumber]=='h'): 
        howManyy=0
        for pirate in listofsignals:
            if (pirate!="" and( (pirate[0]=='g' and ord(pirate[2])==islandnumber) or (pirate[0]=='r' and pirate[1]==str(islandnumber)))): #r for rescue
                howManyy+=1
        if howManyy <= 4 :
            callforhelp(islandnumber,8,teamsig,listofsignals)
            teamsig=replaceChar(teamsig,11+islandnumber,'n')

    if(teamsig[4+2*islandnumber]=='d'):
        if(islandtrack[islandnumber+2]=='oppCaptured'):
            teamsig[4+2*islandnumber]=='x' 
        elif(islandtrack[islandnumber+2]==""):
            teamsig[4+2*islandnumber]=='c'
   

    if(teamsig[4+2*islandnumber]=='c'):
        howmanY=0
        for pirate in listofsignals:
            if(pirate!="" and(((pirate[0]=='g' or pirate[0]=='G')and ord(pirate[2])==islandnumber) or (pirate[0]=='r' and ord(pirate[1])==islandnumber))):
                howmanY+=1
        if(howmanY<=4): #change this later
            callforhelp(islandnumber,3,teamsig,listofsignals)
    return teamsig


       

                


        







