import re

def get_val(lookahead,array):
    if lookahead == '{':
        lookahead = match('{')
        lookahead = get_initializers(lookahead,array)
        lookahead = match('}')
    else:
        lookahead = get_INT(lookahead)
    return lookahead

def get_initializers(lookahead,array):
    lookahead = get_initializer(lookahead,array)
    while lookahead == ',' and  array[i+1]!="}":
        lookahead = match(',')
        lookahead = get_initializer(lookahead,array)
    if lookahead == ',':
        lookahead = match(',')
    elif lookahead in [']', '}']:
        pass
    else:
        raise SyntaxError("Expecting '}' or ']' but got %s" % lookahead)
 
    return lookahead

def get_initializer(lookahead,array):
    if lookahead == '[':
        lookahead = match('[')
        lookahead = get_INT_b(lookahead)
        if lookahead == '...':
            lookahead = match('...')
            lookahead = get_INT_bb(lookahead)
        if (lookahead != ']'):
            raise SyntaxError("Expecting '}' but got %s" % lookahead)
        lookahead = match(']')
        lookahead = match('=')
        lookahead = get_val(lookahead ,array)
        
    elif lookahead in [',']:
        raise SyntaxError("Expecting '}' but got %s" % lookahead)
    else:
        lookahead = get_val(lookahead,array)
    return lookahead

def match(m):
    global i,j,count,flagf
    global barray
    if(m=="{"):
        if(i>=len(array)-1):
            return 0
        else:
            i=i+1
            lookahead=array[i]
            return lookahead
    elif(m=="}"):
        if(i>=len(array)-1):
            return 0
        else:
            i=i+1
            lookahead=array[i]
            return lookahead
    elif(m==","):
        if(i>=len(array)-1):
            return
        else:
            i=i+1
            lookahead=array[i]
            return lookahead
    elif(m=="["):
        if(i>=len(array)-1):
            return 0
        else:
            i=i+1
            lookahead=array[i]
            return lookahead
    elif(m=="]"):
        if(i>=len(array)-1):
            return 0
        else:
            i=i+1
            lookahead=array[i]
            return lookahead
    elif(m=="..."):
        if(i>=len(array)-1):
            return 0
        else:
            i=i+1
            lookahead=array[i]
            return lookahead
    elif(m=="="):
        if(array[i+1]=='{'):
            flagf=True
            count=count+1  
        else:
            count=count+1 
        i=i+1
        lookahead=array[i]
        return lookahead

def get_INT_b(lookahead):
    global l
    global i,ll,flagf,count
    if(flagf==True and count==1):
        ll=int(lookahead)
    else:

        l = int(lookahead)
    i=i+1
    lookahead=array[i]
    return lookahead

def get_INT_bb(lookahead):
    global r,rr,flagf,count
    global i
    if(flagf==True and count==1):
        rr=int(lookahead)
    else:
        r = int(lookahead)
    
    i=i+1
    lookahead=array[i]
    return lookahead
 

def array_append(new_array):
    global ll,rr
    if(ll>rr):
        if(ll<len(carray)):
            carray[ll]=new_array
        else:
            for _ in range(len(carray),ll):
                carray.append(int("0"))
            carray.insert(ll,new_array)
    else:
        if(ll<len(carray) and rr<len(carray)):
            for _ in range(ll,rr+1):
                carray[_]=new_array
        elif(ll<len(carray) and rr>len(carray)-1):
            for _ in range(ll,len(carray)):
                carray[_]=new_array
            for _ in range(len(carray),rr+1):
                carray.append(new_array)
        else:
            for _ in range(len(carray),ll):
                carray.append(int("0"))
            for _ in range(rr-ll+1):
                carray.append(new_array)
    ll=rr=0


def append_last():
    global carray,barray
    global flagf,l,r,i,count

    if(l>r):
        if(l<len(barray)):
            barray[l]=carray
        else:
            for _ in range(len(barray),l):
                barray.append(int("0"))
            barray.insert(l,carray)
    else:
        if(l<len(barray) and r<len(barray)):
            for _ in range(l,r+1):
                barray[_]=carray
        elif(l<len(barray) and r>len(barray)-1):
            for _ in range(l,len(barray)):
                barray[_]=carray
            for _ in range(len(barray),r+1):
                barray.append(carray)
        else:

            for _ in range(len(barray),l):
                barray.append(int("0"))
            for _ in range(r-l+1):
                barray.append(carray)
    flagf=False
    count=0

def newcase_int_end(lookahead):
    global carray,barray
    global flagf,l,r,i,count
    if(array[i-1]=='='):
        append(lookahead)
    else:
        carray.append(int(lookahead))

    append_last()

    i=i+1
    l=0
    r=0
    count=0
    flagf=False
    carray=[]
    lookahead=array[i]
    return lookahead

def append(lookahead):
    global carray
    global ll,rr,i,flagf
    if(ll>rr):
        if(ll<len(carray)):
            carray[ll]=int(lookahead)
        else:
            for _ in range(len(carray),ll):
                carray.append(int("0"))
            carray.insert(ll,int(lookahead))
    else:
        if(ll<len(carray) and rr<len(carray)):
            for _ in range(ll,rr+1):
                carray[_]=int(lookahead)
        elif(ll<len(carray) and rr>len(carray)-1):
            for _ in range(ll,len(carray)):
                carray[_]=int(lookahead)
            for _ in range(len(carray),rr+1):
                carray.append(int(lookahead))
        else:
            for _ in range(len(carray),ll):
                carray.append(int("0"))
            for _ in range(rr-ll+1):
                carray.append(int(lookahead))

def newcase_int(lookahead):
    global carray,new,new_array
    global ll,rr,i,flagf
    if(array[i-1]=='='):
        append(lookahead)

        i=i+1
        ll=0
        rr=0
        lookahead=array[i]
        return lookahead

    else:
        carray.append(int(lookahead))
        i=i+1
        lookahead=array[i]
        return lookahead


def get_INT(lookahead):
    global i,r,l,flag,flagf,count,ll,rr
    global barray,carray,new

    if(array[i-1]=='=' and array[i+1]!='{' and count==1):
        if(l>r):
            if(l<len(barray)):
                barray[l]=int(lookahead)
            else:
                for _ in range(len(barray),l):
                    barray.append(int("0"))
                barray.insert(l,int(lookahead))
        else:
            if(l<len(barray) and r<len(barray)):
                for _ in range(l,r+1):
                    barray[_]=int(lookahead)
            elif(l<len(barray) and r>len(barray)-1):
                for _ in range(l,len(barray)):
                    barray[_]=int(lookahead)
                for _ in range(len(barray),r+1):
                    barray.append(int(lookahead))
            else:

                for _ in range(len(barray),l):
                    barray.append(int("0"))
                for _ in range(r-l+1):
                    barray.append(int(lookahead))

        i=i+1
        l=0
        r=0
        count=0
        lookahead=array[i]
        return lookahead
    
    elif(flagf==True and array[i-1]=='{' and array[i+1]=='}' and ll>0):
        if(array[i+2]=='}'):   
            new_array.append(lookahead)
            array_append(new_array)
            append_last()
        else:
            new_array.append(lookahead)
            array_append(new_array)
        i+=1
        lookahead=array[i]
        return lookahead
    
    elif(flagf==True and array[i-1]=='{' and array[i+1]!='}' and ll>0):
        new_array.append(lookahead)
        new=True
        i+=1
        lookahead=array[i]
        return lookahead
    
    elif(new==True and array[i+1]!='}'):
        new_array.append(lookahead)
        i+=1
        lookahead=array[i]
        return lookahead
    
    elif(new==True and array[i+1]=='}' and array[i+2]=='}'):
        new_array.append(lookahead)
        new=False
        array_append(new_array)
        append_last()
        i+=1
        lookahead=array[i]
        return lookahead

    elif(new==True and array[i+1]=='}'):
        new_array.append(lookahead)
        new=False
        array_append(new_array)
        i+=1
        lookahead=array[i]
        return lookahead

    elif(flagf==True and array[i+1]!='}'):
        lookahead = newcase_int(lookahead)
        return lookahead
    
    
    elif(flagf==True and array[i+1]=='}' and array[i+2]=='}'):
        lookahead= newcase_int(lookahead)
        append_last()
        return lookahead

    elif(flagf==True and array[i+1]=='}'):
        lookahead = newcase_int_end(lookahead)
        return lookahead

    elif(array[i-1]=="{" and i-1==0):
        barray.append(int(lookahead))
        flag=False
        i=i+1
        lookahead=array[i]
        return lookahead     
    
    elif(array[i-1]=="{" and i-1!=0 and array[i+1]=='}'):
        barray.append([int(lookahead)])
        i=i+1
        flag=False
        lookahead=array[i]
        return lookahead

    elif(array[i-1]=="{" and i-1!=0):
        barray.append([int(lookahead)])
        flag=True
        i=i+1
        lookahead=array[i]
        return lookahead
        
    elif (flag==True):
        if(array[i+1]=='}'):
            flag=False
            barray[len(barray)-1].append(int(lookahead))
            i=i+1
            lookahead=array[i]
            return lookahead
        else:
            barray[len(barray)-1].append(int(lookahead))
            i=i+1
            lookahead=array[i]
            return lookahead      
    else:
        barray.append(int(lookahead))
        flag=False
        i=i+1
        lookahead=array[i]
        return lookahead


global i,lookahead
global barray,carray,new_aray,new
global r,l,count,ll,rr,flagf,temp,k
carray=[]
barray = []
new_array=[]
new=False
i=0
count=0
r=0
ll=0
l=0
rr=0
k=0
flagf = False

ip = input()
array=[]
temp=[]
input=""
m=0 
blcount=brcount=0

while(m<len(ip)):
    if(ip[m].isspace()):
        m+=1
    else:
        input+=ip[m]
        m+=1

while(k<len(input)):
    if(input[k]=='{'):
        array.append(input[k])
        blcount+=1
        k+=1
    elif(input[k]=='}'):
        array.append(input[k])
        brcount+=1
        k+=1
    elif(input[k]=='[' or input[k]==']' or input[k]=='='):
        array.append(input[k])
        k+=1
    elif(input[k]==','):
        if(input[k+1]=='}' and input[k-1]!=','):
            k+=1
        else:
            array.append(input[k])
            k+=1

    elif(input[k]=='.'):
        while(input[k]=='.'):
            temp.append(input[k])
            k+=1
        if(len(temp)>3 or len(temp)<3):
            raise SyntaxError("expecting ']' but got '.'")
        else:
            array.append('.'*len(temp))
            temp=[]
            
    elif(re.match("\d+",input[k]) ):
        while( re.match("\d+",input[k])  ):
            temp.append(int(input[k]))
            k+=1
            if(k<len(input)):
                continue
            else:
                break

        n=len(temp)
        number = 0
        for j in range(0,n):
            number = number + temp[j]*(int(10)**(n-1-j))
        array.append(number)
        temp=[]

if(blcount!=brcount):
    raise SyntaxError("expecting 'EOF' but got '}'")

if(len(array)==1 and ( array[0]!='{' or  array[0]!='}'  or array[0]!='='  or array[0]!=',' ) ):
    print(array[0])

elif(len(array)>1):
    if(array[0]=='{' and array[1]=='}'):
        print(barray)
    else:
        lookahead= array[i]
        get_val(lookahead,array)
        print(barray)

      

