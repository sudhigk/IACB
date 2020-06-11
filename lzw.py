
dict = {}
ns = int(input('enter the no of symbols :'))
print('enter the sample table symbols :')
i=0
while(i<ns):
    sy = input()
    dict[sy] = [i+1,-1]
    i = i+1

count  = ns + 1
# print(dict['b'][0])

string = input('enter the string :')
# print(len(string))

n = len(string)
# print(string[1])



def search(i,l):
    ss = string[i:l]
    for ch in dict.keys():
        if(ss == ch):
            return 1
    return 0

def pos(i,l):
    ss = string[i:l]
    for ch in dict.keys():
        if(ss == ch):
            return dict[ch][0]
    return -1



i = 0
while(i<n):
    print('-----',i,'------')
    eo = -1
    l = i + 1
    f = 0
    while(f == 0 and l<= n):
        if(search(i,l) == 1):
            l = l + 1
            print('i=',i,'l=',l)
        else:
            f = 1
            print('f=1')
    if(f==1):
        ne = string[i:l]
        eo = pos(i,l-1)
        dict[ne] = [count, eo]
        count = count + 1


    i = l - 1

print('RESULT')
print(dict)

