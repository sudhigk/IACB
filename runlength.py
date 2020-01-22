def rlEncode(data):
    c = 0
    r = 1
    res = ''

    for ch in data:
        #print('####char =',ch)
        if(ch == '$'):
            #
            #print('terminal')
            #print('r=',r,' sc=',sc)
            if (r < 4):
                # write
                for i in range(0, r):
                    res = res + str(sc)
                r = 1
                sc = ch
            else:
                # write compress
                res = res + '@' +str(r)+ str(sc)
                r = 1
                sc = ch
        else:
            c = c + 1
            if(c==1):
                sc = ch
            elif(sc == ch):
                r = r + 1
            elif(r < 4):
                #write
                # print()
                for i in range (0,r):
                    res = res + str(sc)
                r = 1
                sc = ch
            else:
                #write compress
                res = res + '@' + str(r) + str(sc)
                r = 1
                sc = ch
    return(res)



st = input("Enter the string : ")
st = st + '$'
encoded = rlEncode(st)
print(encoded)

def rlDecode(data):
    op = ''
    cf = 0
    n = 1
    for ch in data:
        if(cf == 0):
            if(ch == '@'):
                cf = 1
            else:
                for i in range(0,n):
                    op = op + str(ch)
                n =1
        else:
            n = int(ch)
            cf = 0
    return op


print(rlDecode(encoded))