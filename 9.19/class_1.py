class Turtle(list):  #Python 中类约定以大写字母开头, 加个括号就是继承！！！！！
    color = 'green'   
    weight = 10
    legs = 4
    mouth = 'big'

    def climb(self):
        print('{}正在很努力地向前爬'.format(self))


tt = Turtle()
a = 1
tt.climb()
tt.append(3)
print(tt, tt.color)

    
