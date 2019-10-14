spanish = open('C:\\Users\\jeffm\\Downloads\\pythonsubspa.txt' , 'r')
english = open('C:\\Users\\jeffm\\Downloads\\pythonsubeng.txt' , 'r')
scontent = spanish.readlines()
econtent = english.readlines()
englines = []
spalines = []
engword = []
spaword = []
engtime = []
spatime = []
engsplit=[]
spasplit=[]
n = 0
a = ''
output = ''
for x in scontent:
    x=x.strip('\n')
    if x.isdigit() or x=='':
        pass
    else:
        spalines.append(x)

for x in econtent:
    x=x.strip('\n')
    if x.isdigit() or x=='':
        pass
    else:
        englines.append(x)
    
for z in englines:
    if z.startswith('0'):
        z=z.replace(':','')
        z=z.replace(',','')
        z=z.replace('-','')
        z=z.replace('>','-')
        z=z.replace(' ','')   
        engtime.append(z)
        engword.append(a)
        a=''
    else:
        a=a+' '+z
engword.append(a)
engword.pop(0)

for z in spalines:
    if z.startswith('0'):
        z=z.replace(':','')
        z=z.replace(',','')
        z=z.replace('-','')
        z=z.replace('>','-')
        
        z=z.replace(' ','')   
        spatime.append(z)
        spaword.append(a)
        a=''
    else:
        a=a+' '+z
spaword.append(a)
spaword.pop(0)

#print('\nENGLISH\n')
for x in engtime:
    e=x.split("-")
    engsplit.append(e)


#for i in engsplit:
 #   print(engsplit[n][0])
  #  print(engsplit[n][1])
   # print(engword[n])
    #n=n+1


#print('\nSPANISH\n')
for x in spatime:
    e=x.split("-")
    spasplit.append(e)
    
n=0
#for i in spasplit:
 #   print(spasplit[n][0])
  #  print(spasplit[n][1])
   # print(spaword[n])
    #n=n+1

s=0
e=0
time=[]
if len(spatime)>len(engtime):
    time=spatime
else:
    time=engtime


    
for i in range(0,len(time)+19):
    spa0=spasplit[s][0]
    eng0=engsplit[e][0]
    spa1=spasplit[s][1]
    eng1=engsplit[e][1]
    if spa0<eng0 and spa1<eng0:
        ntime0=spa0
        ntime1=spa1
        ntime0=ntime0[:2]+':'+ntime0[2:]
        ntime0=ntime0[:5]+':'+ntime0[5:]
        ntime0=ntime0[:8]+':'+ntime0[8:]
        ntime1=ntime1[:2]+':'+ntime1[2:]
        ntime1=ntime1[:5]+':'+ntime1[5:]
        ntime1=ntime1[:8]+':'+ntime1[8:]
        output=output+'\n'+ntime0+' --> '+ntime1+'\n'+spaword[s]
        s+=1
        
    elif eng0<spa0 and eng1<spa0:
        ntime0=eng0
        ntime1=eng1
        ntime0=ntime0[:2]+':'+ntime0[2:]
        ntime0=ntime0[:5]+':'+ntime0[5:]
        ntime0=ntime0[:8]+':'+ntime0[8:]
        ntime1=ntime1[:2]+':'+ntime1[2:]
        ntime1=ntime1[:5]+':'+ntime1[5:]
        ntime1=ntime1[:8]+':'+ntime1[8:]
        output=output+'\n'+ntime0+' --> '+ntime1+'\n'+engword[e]
        e+=1
        
    else:
        if eng0<spa0 and eng1==spa1 and eng0==0 is False:
            e+=1
            s+=1
            ntime0=eng0
            ntime1=eng1
            ntime0=ntime0[:2]+':'+ntime0[2:]
            ntime0=ntime0[:5]+':'+ntime0[5:]
            ntime0=ntime0[:8]+':'+ntime0[8:]
            ntime1=ntime1[:2]+':'+ntime1[2:]
            ntime1=ntime1[:5]+':'+ntime1[5:]
            ntime1=ntime1[:8]+':'+ntime1[8:]
            output=output+'\n'+ntime0+' --> '+ntime1+'\n'+engword[e]+'\n'+spaword[s]
        elif spa0<eng0 and spa1>=eng0:
            e+=1
            eng0=engsplit[e+1][0]
            eng1=engsplit[e+1][1]
            if spa0<eng0 and spa1<eng0:
                s+=1
            else:
                break
        elif eng0<spa0 and eng1>=spa0:
            ntime0=eng0
            ntime1=eng1
            ntime0=ntime0[:2]+':'+ntime0[2:]
            ntime0=ntime0[:5]+':'+ntime0[5:]
            ntime0=ntime0[:8]+':'+ntime0[8:]
            ntime1=ntime1[:2]+':'+ntime1[2:]
            ntime1=ntime1[:5]+':'+ntime1[5:]
            ntime1=ntime1[:8]+':'+ntime1[8:]    
            output=output+'\n'+ntime0+' --> '+ntime1+'\n'+engword[e]+'\n'+spaword[s]
            s+=1
            spa0=spasplit[s+1][0]
            spa1=spasplit[s+1][1]
            
            while True:
                if eng0<=spa0 and eng1<=spa0:
                    
                    e+=1
                    break
                else:
                    s+=1
                    break
                
   
            
                
        else:
            ntime0=eng0
            ntime1=eng1
            ntime0=ntime0[:2]+':'+ntime0[2:]
            ntime0=ntime0[:5]+':'+ntime0[5:]
            ntime0=ntime0[:8]+':'+ntime0[8:]
            output=output+'\n'+eng0+'\n'+eng1+'\n'+engword[e]+'\n'+spaword[s]
            if spa1<eng1:
                s+=1
            else:
                e+=1
    
                
            
f= open('C:\\Users\\jeffm\\Downloads\\pythonsubengandspa.txt' , 'w')
f.write(output)

print(output)

        
   















    
