import random
ans = random.randint(1,100)
temp = input('guess which number am I thinking now?\n')
while !temp.isnumeric():
    print('what the hell are you tinking???')
    temp = input('come on guy, type a number')
guess = int(temp)
while guess != ans:
    if guess > ans:
        print('please have a smaller one')
    else:
        print('please have a bigger one')
    temp = input('try again please:\n')
#    while isinstance(temp, str):
#        print('what the hell are you tinking???')
#        temp = input('come on guy, type a number')
    guess = int(temp)
print('you are right!')
input()

    
