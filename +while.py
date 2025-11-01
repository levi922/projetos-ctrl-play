'''
v = input('qualquer coisa ')
print(v end = '', v*2 end = '', v*3 end = '', v*4 end = '', v*5 end = '')
'''
'''
l = int(input('linhas:'))
i = 0
while i <= l:
    j=0
    while j<=i:
        print('*', end = '')
        j+=1
    print('\n')
    i+=1
'''
l = int(input('linhas:'))
while l > 0:
    j=l
    while j> 0:
        print('*', end = '')
        j-=1
    print('')
    l-=1