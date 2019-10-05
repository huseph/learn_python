import easygui as g
import sys

while 1:
    g.msgbox('嗨，欢迎 进入第一个界面小游戏｡･∀･ﾉﾞ')

    msg = '请问你希望在大学生活中学到什么知识呢？'
    title = '小游戏互动'
    choices = ['谈恋爱', '编程', 'UI设计']

    choice = g.choicebox(msg, title, choices)   #remember the order: msg, title and choices

    g.msgbox('你的选择是：'+ str(choice))
    msg = '你希望重新开始小游戏吗？'
    title = '请选择'

    if g.ccbox(msg,title):   #show the Continue/Cancel dialog
        pass
    else:
        sys.exit(0)    #users chose Cancle
    
