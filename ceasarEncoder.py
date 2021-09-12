'''
ceasarEncoder.py
--------------------------
same as ceasarEncoder(executable/bin)
but this takes user input directly
rather than reading from a file, like
the binary version.
'''

# Ceasar Encoder Dictionary
#BetterIdea = {'a':'0','b':'1','c':'2',.......}
AlphaDecimal = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25,}
DecimalAlpha = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}

def encodeMsg(msgIn,nKey):
    NumList = []
    encMsg = ''

    for n in msgIn:
        if n == '\n':
            break
        elif n == ' ':
            NumList.append(n)
        else:
            NumList.append(str((AlphaDecimal[n] + nKey)%26))

    for n in NumList:
        if n == ' ':
            encMsg += ' '
        else:
            encMsg += DecimalAlpha[int(n)]

    return encMsg

usrStr = input('enter msg: ')
usrKey = int(input('enter key: '))

print('\noriginal msg:\n'+usrStr+'\n\nencoded msg:\n'+encodeMsg(usrStr,usrKey))
