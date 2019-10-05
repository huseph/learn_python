def isnumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def inp():
    i = input()
    while not isnumber(i):
        print('what the hell are you thinking???')
        i = input('come on guy, type a number\n')
    return i
    
import random
ans = random.randint(1,100)
print('guess which number I am thinking now?\n')
guess = float(inp())
while guess != ans:
    if guess > ans:
        print('please have a smaller one')
    else:
        print('please have a bigger one')
    print('try again please:\n')
    guess = float(inp())
print('you are right!')
input()
