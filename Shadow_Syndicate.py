from random import randint
import math
import random

name="Shadow Syndicate"

def moveTo(x , y , Pirate):
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


def ActTeam(team):
    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)


def ActPirate(pirate):
    up = pirate.investigate_up()
    down = pirate.investigate_down()
    left = pirate.investigate_left()
    right = pirate.investigate_right()
    nw = pirate.investigate_nw()
    ne = pirate.investigate_ne()
    se = pirate.investigate_se()
    sw = pirate.investigate_sw()
    current = pirate.investigate_current()
    x,y=pirate.getPosition()
    signal=pirate.getTeamSignal()
    track=pirate.trackPlayers()
    d=pirate.getDimensionX()
    if (signal==''):
        pirate.setTeamSignal(',,,,,,,,')
        signal=pirate.getTeamSignal()

    if(pirate.getSignal()==''):
        s=''
        for i in range(16):
            s=s+str(randint(0,d))+','+str(randint(0,d))+','
        s=s+'0'
        pirate.setSignal(s)
    s=pirate.getSignal()
    ss=s.split(',')
    rows = 16
    columns = 2
    random_2d_array = [[0] * columns for _ in range(rows)]
    for i in range(16):
        random_2d_array[i][0]=int(ss[2*i])
        random_2d_array[i][1]=int(ss[2*i+1])
    '''if (
        (current[0] == "island1")
        or (current[0] == "island2")
        or (current[0] == "island3")
    ):
        return 0'''

    if( (se[0]=='island1' or se[0]=='island2' or se[0]=='island3') and  
       (down[0]!='island1' or down[0]!='island2' or down[0]!='island3') and 
       (sw[0]!='island1' or sw[0]!='island2' or sw[0]!='island3') and
       (ne[0]!='island1' or ne[0]!='island2' or ne[0]!='island3') and
       (right[0]!='island1' or right[0]!='island2' or right[0]!='island3')):
      ino=int(se[0][-1])
      s=signal.split(",")

      if(s[3*ino-3]==''):
          s[3*ino-3]=se[0][-1]
          s[3*ino-2]=str(x+2)
          s[3*ino-1]=str(y+2)
          signal=s[0]+","+s[1]+","+s[2]+","+s[3]+","+s[4]+","+s[5]+","+s[6]+","+s[7]+","+s[8]
          pirate.setTeamSignal(signal)
          return moveTo(x+2,y+2,pirate)
        
      elif(se[1]!='friend'):
          return moveTo(x+1,y+1,pirate)
      
      else :
          return random.randint(1,4)
    
    if( (se[0]=='island1' or se[0]=='island2' or se[0]=='island3') and  
       (down[0]=='island1' or down[0]=='island2' or down[0]=='island3') and 
       (sw[0]!='island1' or sw[0]!='island2' or sw[0]!='island3') 
       ):
      ino=int(se[0][-1])
      s=signal.split(",")

      if(s[3*ino-3]==''):
          s[3*ino-3]=se[0][-1]
          s[3*ino-2]=str(x+1)
          s[3*ino-1]=str(y+2)
          signal=s[0]+","+s[1]+","+s[2]+","+s[3]+","+s[4]+","+s[5]+","+s[6]+","+s[7]+","+s[8]
          pirate.setTeamSignal(signal)
          return moveTo(x+1,y+2,pirate)
      
      elif(down[1]!='friend'):
          return moveTo(x,y+1,pirate)
        
      elif(se[1]!='friend'):
          return moveTo(x+1,y+1,pirate)
      
      else :
          return random.choice([1,2,4])
    
    if( (se[0]=='island1' or se[0]=='island2' or se[0]=='island3') and  
       (down[0]=='island1' or down[0]=='island2' or down[0]=='island3') and 
       (sw[0]=='island1' or sw[0]=='island2' or sw[0]=='island3') 
       ):
      ino=int(se[0][-1])
      s=signal.split(",")

      if(s[3*ino-3]==''):
          s[3*ino-3]=se[0][-1]
          s[3*ino-2]=str(x)
          s[3*ino-1]=str(y+2)
          signal=s[0]+","+s[1]+","+s[2]+","+s[3]+","+s[4]+","+s[5]+","+s[6]+","+s[7]+","+s[8]
          pirate.setTeamSignal(signal)
          return moveTo(x,y+2,pirate)
      
      elif(down[1]!='friend'):
          return moveTo(x,y+1,pirate)
      
      elif(sw[1]!='friend'):
          return moveTo(x-1,y+1,pirate)
        
      elif(se[1]!='friend'):
          return moveTo(x+1,y+1,pirate)
      
      else :
          return random.choice([1,2,4])
    
    if( (se[0]!='island1' or se[0]!='island2' or se[0]!='island3') and  
       (down[0]=='island1' or down[0]=='island2' or down[0]=='island3') and 
       (sw[0]=='island1' or sw[0]=='island2' or sw[0]=='island3') 
       ):
      ino=int(sw[0][-1])
      s=signal.split(",")

      if(s[3*ino-3]==''):
          s[3*ino-3]=sw[0][-1]
          s[3*ino-2]=str(x-1)
          s[3*ino-1]=str(y+2)
          signal=s[0]+","+s[1]+","+s[2]+","+s[3]+","+s[4]+","+s[5]+","+s[6]+","+s[7]+","+s[8]
          pirate.setTeamSignal(signal)
          return moveTo(x-1,y+2,pirate)
      
      elif(down[1]!='friend'):
          return moveTo(x,y+1,pirate)
        
      elif(sw[1]!='friend'):
          return moveTo(x-1,y+1,pirate)
      
      else :
          return random.choice([1,2,4])

    if( (se[0]!='island1' or se[0]!='island2' or se[0]!='island3') and  
       (down[0]!='island1' or down[0]!='island2' or down[0]!='island3') and 
       (sw[0]=='island1' or sw[0]=='island2' or sw[0]=='island3') and
       (nw[0]!='island1' or nw[0]!='island2' or nw[0]!='island3') and
       (left[0]!='island1' or left[0]!='island2' or left[0]!='island3')):
      ino=int(sw[0][-1])
      s=signal.split(",")

      if(s[3*ino-3]==''):
          s[3*ino-3]=sw[0][-1]
          s[3*ino-2]=str(x-2)
          s[3*ino-1]=str(y+2)
          signal=s[0]+","+s[1]+","+s[2]+","+s[3]+","+s[4]+","+s[5]+","+s[6]+","+s[7]+","+s[8]
          pirate.setTeamSignal(signal)
          return moveTo(x-2,y+2,pirate)
        
      elif(sw[1]!='friend'):
          return moveTo(x-1,y+1,pirate)
      
      else :
          return random.randint(1,4)
    
    if( (sw[0]=='island1' or sw[0]=='island2' or sw[0]=='island3') and  
       (left[0]=='island1' or left[0]=='island2' or left[0]=='island3') and 
       (nw[0]!='island1' or nw[0]!='island2' or nw[0]!='island3') 
       ):
      ino=int(sw[0][-1])
      s=signal.split(",")

      if(s[3*ino-3]==''):
          s[3*ino-3]=sw[0][-1]
          s[3*ino-2]=str(x-2)
          s[3*ino-1]=str(y+1)
          signal=s[0]+","+s[1]+","+s[2]+","+s[3]+","+s[4]+","+s[5]+","+s[6]+","+s[7]+","+s[8]
          pirate.setTeamSignal(signal)
          return moveTo(x-2,y+1,pirate)
      
      elif(left[1]!='friend'):
          return moveTo(x-1,y,pirate)
        
      elif(sw[1]!='friend'):
          return moveTo(x-1,y+1,pirate)
      
      else :
          return random.choice([1,2,3])
    
    if( (sw[0]=='island1' or sw[0]=='island2' or sw[0]=='island3') and  
       (left[0]=='island1' or left[0]=='island2' or left[0]=='island3') and 
       (nw[0]=='island1' or nw[0]=='island2' or nw[0]=='island3') 
       ):
      ino=int(sw[0][-1])
      s=signal.split(",")

      if(s[3*ino-3]==''):
          s[3*ino-3]=sw[0][-1]
          s[3*ino-2]=str(x-2)
          s[3*ino-1]=str(y)
          signal=s[0]+","+s[1]+","+s[2]+","+s[3]+","+s[4]+","+s[5]+","+s[6]+","+s[7]+","+s[8]
          pirate.setTeamSignal(signal)
          return moveTo(x-2,y,pirate)
      
      elif(left[1]!='friend'):
          return moveTo(x-1,y,pirate)
        
      elif(sw[1]!='friend'):
          return moveTo(x-1,y+1,pirate)
      
      elif(nw[1]!='friend'):
          return moveTo(x-1,y-1,pirate)
      
      else :
          return random.choice([1,2,3])
      
    if( (sw[0]!='island1' or sw[0]!='island2' or sw[0]!='island3') and  
       (left[0]=='island1' or left[0]=='island2' or left[0]=='island3') and 
       (nw[0]=='island1' or nw[0]=='island2' or nw[0]=='island3') 
       ):
      ino=int(nw[0][-1])
      s=signal.split(",")

      if(s[3*ino-3]==''):
          s[3*ino-3]=nw[0][-1]
          s[3*ino-2]=str(x-2)
          s[3*ino-1]=str(y-1)
          signal=s[0]+","+s[1]+","+s[2]+","+s[3]+","+s[4]+","+s[5]+","+s[6]+","+s[7]+","+s[8]
          pirate.setTeamSignal(signal)
          return moveTo(x-2,y-1,pirate)
      
      elif(left[1]!='friend'):
          return moveTo(x-1,y,pirate)
        
      elif(nw[1]!='friend'):
          return moveTo(x-1,y-1,pirate)
      
      else :
          return random.choice([1,2,3])
      
    if( (ne[0]!='island1' or ne[0]!='island2' or ne[0]!='island3') and  
       (up[0]!='island1' or up[0]!='island2' or up[0]!='island3') and 
       (nw[0]=='island1' or nw[0]=='island2' or nw[0]=='island3') and
       (sw[0]!='island1' or sw[0]!='island2' or sw[0]!='island3') and
       (left[0]!='island1' or left[0]!='island2' or left[0]!='island3')):
      ino=int(nw[0][-1])
      s=signal.split(",")

      if(s[3*ino-3]==''):
          s[3*ino-3]=nw[0][-1]
          s[3*ino-2]=str(x-2)
          s[3*ino-1]=str(y-2)
          signal=s[0]+","+s[1]+","+s[2]+","+s[3]+","+s[4]+","+s[5]+","+s[6]+","+s[7]+","+s[8]
          pirate.setTeamSignal(signal)
          return moveTo(x-2,y-2,pirate)
        
      elif(nw[1]!='friend'):
          return moveTo(x-1,y-1,pirate)
      
      else :
          return random.randint(1,4)
      
    if( (ne[0]!='island1' or ne[0]!='island2' or ne[0]!='island3') and  
       (up[0]=='island1' or up[0]=='island2' or up[0]=='island3') and 
       (nw[0]=='island1' or nw[0]=='island2' or nw[0]=='island3') 
       ):
      ino=int(nw[0][-1])
      s=signal.split(",")

      if(s[3*ino-3]==''):
          s[3*ino-3]=nw[0][-1]
          s[3*ino-2]=str(x-1)
          s[3*ino-1]=str(y-2)
          signal=s[0]+","+s[1]+","+s[2]+","+s[3]+","+s[4]+","+s[5]+","+s[6]+","+s[7]+","+s[8]
          pirate.setTeamSignal(signal)
          return moveTo(x-1,y-2,pirate)
      
      elif(up[1]!='friend'):
          return moveTo(x,y-1,pirate)
        
      elif(nw[1]!='friend'):
          return moveTo(x-1,y-1,pirate)
      
      else :
          return random.choice([4,2,3])
      
    if( (ne[0]=='island1' or ne[0]=='island2' or ne[0]=='island3') and  
       (up[0]=='island1' or up[0]=='island2' or up[0]=='island3') and 
       (nw[0]=='island1' or nw[0]=='island2' or nw[0]=='island3') 
       ):
      ino=int(nw[0][-1])
      s=signal.split(",")

      if(s[3*ino-3]==''):
          s[3*ino-3]=nw[0][-1]
          s[3*ino-2]=str(x)
          s[3*ino-1]=str(y-2)
          signal=s[0]+","+s[1]+","+s[2]+","+s[3]+","+s[4]+","+s[5]+","+s[6]+","+s[7]+","+s[8]
          pirate.setTeamSignal(signal)
          return moveTo(x,y-2,pirate)
      
      elif(up[1]!='friend'):
          return moveTo(x,y-1,pirate)
        
      elif(nw[1]!='friend'):
          return moveTo(x-1,y-1,pirate)
      
      elif(ne[1]!='friend'):
          return moveTo(x+1,y-1,pirate)
      
      else :
          return random.choice([4,2,3])
      
    if( (ne[0]=='island1' or ne[0]=='island2' or ne[0]=='island3') and  
       (up[0]=='island1' or up[0]=='island2' or up[0]=='island3') and 
       (nw[0]!='island1' or nw[0]!='island2' or nw[0]!='island3') 
       ):
      ino=int(ne[0][-1])
      s=signal.split(",")

      if(s[3*ino-3]==''):
          s[3*ino-3]=ne[0][-1]
          s[3*ino-2]=str(x+1)
          s[3*ino-1]=str(y-2)
          signal=s[0]+","+s[1]+","+s[2]+","+s[3]+","+s[4]+","+s[5]+","+s[6]+","+s[7]+","+s[8]
          pirate.setTeamSignal(signal)
          return moveTo(x+1,y-2,pirate)
      
      elif(up[1]!='friend'):
          return moveTo(x,y-1,pirate)
      
      elif(ne[1]!='friend'):
          return moveTo(x+1,y-1,pirate)
      
      else :
          return random.choice([4,2,3])

    if( (nw[0]!='island1' or nw[0]!='island2' or nw[0]!='island3') and  
       (up[0]!='island1' or up[0]!='island2' or up[0]!='island3') and 
       (ne[0]=='island1' or ne[0]=='island2' or ne[0]=='island3') and
       (se[0]!='island1' or se[0]!='island2' or se[0]!='island3') and
       (right[0]!='island1' or right[0]!='island2' or right[0]!='island3')):
      ino=int(ne[0][-1])
      s=signal.split(",")

      if(s[3*ino-3]==''):
          s[3*ino-3]=ne[0][-1]
          s[3*ino-2]=str(x+2)
          s[3*ino-1]=str(y-2)
          signal=s[0]+","+s[1]+","+s[2]+","+s[3]+","+s[4]+","+s[5]+","+s[6]+","+s[7]+","+s[8]
          pirate.setTeamSignal(signal)
          return moveTo(x+2,y-2,pirate)
        
      elif(ne[1]!='friend'):
          return moveTo(x+1,y-1,pirate)
      
      else :
          return random.randint(1,4)
    
    if( (ne[0]=='island1' or ne[0]=='island2' or ne[0]=='island3') and  
       (right[0]=='island1' or right[0]=='island2' or right[0]=='island3') and 
       (se[0]!='island1' or se[0]!='island2' or se[0]!='island3') 
       ):
      ino=int(ne[0][-1])
      s=signal.split(",")

      if(s[3*ino-3]==''):
          s[3*ino-3]=ne[0][-1]
          s[3*ino-2]=str(x+2)
          s[3*ino-1]=str(y-1)
          signal=s[0]+","+s[1]+","+s[2]+","+s[3]+","+s[4]+","+s[5]+","+s[6]+","+s[7]+","+s[8]
          pirate.setTeamSignal(signal)
          return moveTo(x+2,y-1,pirate)
      
      elif(right[1]!='friend'):
          return moveTo(x+1,y,pirate)
      
      elif(ne[1]!='friend'):
          return moveTo(x+1,y-1,pirate)
      
      else :
          return random.choice([4,1,3])
    
    if( (ne[0]=='island1' or ne[0]=='island2' or ne[0]=='island3') and  
       (right[0]=='island1' or right[0]=='island2' or right[0]=='island3') and 
       (se[0]=='island1' or se[0]=='island2' or se[0]=='island3') 
       ):
      ino=int(ne[0][-1])
      s=signal.split(",")

      if(s[3*ino-3]==''):
          s[3*ino-3]=ne[0][-1]
          s[3*ino-2]=str(x+2)
          s[3*ino-1]=str(y)
          signal=s[0]+","+s[1]+","+s[2]+","+s[3]+","+s[4]+","+s[5]+","+s[6]+","+s[7]+","+s[8]
          pirate.setTeamSignal(signal)
          return moveTo(x+2,y,pirate)
      
      elif(right[1]!='friend'):
          return moveTo(x+1,y,pirate)
        
      elif(se[1]!='friend'):
          return moveTo(x+1,y+1,pirate)
      
      elif(ne[1]!='friend'):
          return moveTo(x+1,y-1,pirate)
      
      else :
          return random.choice([4,1,3])
      
    if( (ne[0]!='island1' or ne[0]!='island2' or ne[0]!='island3') and  
       (right[0]=='island1' or right[0]=='island2' or right[0]=='island3') and 
       (se[0]=='island1' or se[0]=='island2' or se[0]=='island3') 
       ):
      ino=int(se[0][-1])
      s=signal.split(",")

      if(s[3*ino-3]==''):
          s[3*ino-3]=se[0][-1]
          s[3*ino-2]=str(x+2)
          s[3*ino-1]=str(y+1)
          signal=s[0]+","+s[1]+","+s[2]+","+s[3]+","+s[4]+","+s[5]+","+s[6]+","+s[7]+","+s[8]
          pirate.setTeamSignal(signal)
          return moveTo(x+2,y+1,pirate)
      
      elif(right[1]!='friend'):
          return moveTo(x+1,y,pirate)
        
      elif(se[1]!='friend'):
          return moveTo(x+1,y+1,pirate)
      
      else :
          return random.choice([4,1,3])
    st=signal.split(',')

    if(int(pirate.getID())%3==0 and st[0]!='' and (track[3]=='oppCapturing' or track[3]=='oppCaptured')):
        return moveTo(int(st[1]),int(st[2]),pirate)
    
    if(int(pirate.getID())%3==1 and st[3]!='' and (track[4]=='oppCapturing' or track[4]=='oppCaptured')):
        return moveTo(int(st[4]),int(st[5]),pirate)
    
    if(int(pirate.getID())%3==2 and st[6]!='' and (track[5]=='oppCapturing' or track[5]=='oppCaptured')):
        return moveTo(int(st[7]),int(st[8]),pirate)
    
    else:
        pno=int(ss[-1])
        if(pno<15):
            if (pirate.getDeployPoint()==(0,d) or pirate.getDeployPoint==(d,0) ):
                x1=random_2d_array[pno][0]
                y1=random_2d_array[pno][1]
            else :
                x1=d-random_2d_array[pno][0]
                y1=d-random_2d_array[pno][1]
            if(pirate.getPosition()==(x1,y1) or int(pirate.getCurrentFrame()/100)%16>pno):
                if(pno<10):
                    s=s[:-1]
                else:
                    s=s[:-2]
                s=s+str(pno+1)
            pirate.setSignal(s)
            return moveTo(x1,y1,pirate)
        else:
            pirate.setSignal('')
            return randint(1,4)
        

