import time as t

class MyTimer():
    def __init__(self):
        self.isStart = False
        self.lasted = []
        self.prompt = '计时未开始'
        self.default = ['年', '月', '日', '时', '分', '秒']
        self.begin = 0
        self.end = 0

        
    def __str__(self):
        return self.prompt

    #开始计时
    def start(self):
        if self.isStart:
            print('计时已经运行，请勿重复调用')
        else:
            self.isStart = True
            self.begin = t.localtime()
            print('计时开始')


    def finish(self):
        if self.isStart:
            self.end = t.localtime()
            print('计时结束')
            self._calc()
            self.begin = 0
            self.stop = 0
            self.isStart = False
            self.prompt = '计时未开始'
        else:
            print('请先开始计时')


    def _calc(self):
        self.prompt = '运行了'
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index] or index == 5:
                self.prompt += (str(self.lasted[index]) + str(self.default[index]))            
        print(self.prompt)

    def __add__(self, other):
        self.prompt = '总共运行了'
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index] or index == 5:
                self.prompt += (str(self.lasted[index]) + str(self.default[index]))            
        print(self.prompt)



t1 = MyTimer()
t1.start()
t1.finish()

t1
