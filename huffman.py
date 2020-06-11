import numpy as np

probc = np.chararray((26), unicode=True)
# probc[:] = ''
probc[0] = 'a'
for i in range(0,25):
    probc[i+1] = chr(ord(probc[i])+1)

probn = np.zeros((26))
probi = -1
sum = 0
outc = np.chararray((26), unicode=True)
outn = np.zeros((26))
rel = np.chararray((26,26), unicode=True)

r = np.chararray((26,10), unicode=True)


#counting letters

st = input("Enter the string : ")
for ch in st:
    sum = sum + 1
    for i in range (0,26):
        if(probc[i] == ch):
            break
    probn[i] =  probn[i] + 1

#probability calculation

for i in range(0,26):
    probn[i] = probn[i] / sum

#copied to new datastructure probn -> outn , probc -> outc

j = 0
for i in range(0,26):
    if(probn[i] != 0):
        outc[j] = probc[i]
        rel[j][0] = probc[i]
        outn[j] = probn[i]
        j = j + 1

ctr = j





for i in range (1,ctr):
    for j in range (0,ctr-i):
        if(outn[j]>outn[j+1]):
            (outc[j],outc[j+1]) = (outc[j+1],outc[j])
            (outn[j],outn[j+1]) = (outn[j+1],outn[j])
        # temp
        for i in range(0, ctr):
            print('temp ', outc[i],end=' ')
        print()



count = ctr


def result():
    print('combine ',outc[0],outc[1])
    flag = 1
    while(flag == 1):
        ch1 = outc[0]
        ch2 = outc[1]
        for i in range(0,26):
            if(rel[i][0] == ch1):
                break


        for z in range(0, 10):
            if (r[i][z] == ''):
                break
        r[i][z] = '1'

        for j in range(1,26):
            if(rel[i][j] ==''):
                break
            else:
                ch = rel[i][j]
                print('first',ch,end=' ')
                for k in range(0,26):
                    if(rel[k][0] == ch):
                        break


                for z in range(0, 10):
                    if (r[k][z] == ''):
                        break
                r[k][z] = '1'

        rel[i][j] = ch2
        ter = j + 1

        # 0 case same as above
        for h in range(0,26):
            if(rel[h][0] == ch2):
                break


        for z in range(0, 10):
            if (r[h][z] == ''):
                break
        r[h][z] = '0'

        for j in range(1,26):
            if(rel[h][j] ==''):
                break
            else:
                ch = rel[h][j]
                print('second ',ch)

                #transfer
                f = 1
                for l in range (1,26):
                    if(rel[i][l] == ch):
                        print('l',l)
                        f = 0
                print('f =',f)
                if(f == 1):
                    print('transfer',outc[0],outc[1])
                    rel[i][ter] = ch
                    ter = ter + 1

                for k in range(0,26):
                    if(rel[k][0] == ch):
                        break


                for z in range(0, 10):
                    if (r[k][z] == ''):
                        break
                r[k][z] = '0'

        flag = 0




while(count != 1):
    result()
    outn[0] = outn[0] + outn[1]
    for i in range(1,count):
        outc[i] = outc[i+1]
        outn[i] = outn[i+1]
    count = count - 1

    for i in range(1, count):
        for j in range(0, count - i):
            if (outn[j] > outn[j + 1]):
                (outc[j], outc[j + 1]) = (outc[j + 1], outc[j])
                (outn[j], outn[j + 1]) = (outn[j + 1], outn[j])





print('\n\n--------------------\nRESULT')


# for i in range (0,26):
#     print(probc[i],probn[i])

for i in range (0,ctr):
    # print(rel[i][0],int(res[i]))
    print(rel[i][0],'= ',end='')
    for j in range(9,-1,-1):
        if(r[i][j] != ''):
            print(r[i][j],end='')
    print()
