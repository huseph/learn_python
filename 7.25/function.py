def test(*params):
    print('参数的长度是：', len(params))
    print('第二个参数是：', params[1])
test('aaa', 'bbb', 'ccc', 'hello')
