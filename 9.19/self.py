class Ball:
    def setName(self, name):
        self.name = name   ###个人理解：self.name相当于声明self（也就是这个Ball)里面的一个属性的值为传递进来的name
    def kick(self):
        print('我叫{}，该死的，谁踢我'.format(self.name))


a = Ball()
a.setName('ball')
a.kick()
