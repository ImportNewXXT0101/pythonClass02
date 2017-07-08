#-*- encoding=UTF-8 -*-

def log(level, *args, **kvargs):
    def inner(func):
        '''
        * 表示无名字参数
        ** 表示有名字参数
        '''

        def wrapper(*args, **kvargs):
            #
            print level, 'before calling ', func.__name__
            print level, 'args', args, 'kvargs', kvargs
            func(*args, **kvargs)
            print level, 'end calling ', func.__name__

        return wrapper
    return inner

    #@log
    #装饰器

@log(level='Start')
def helloXXT(name, age):
    print 'hello:', name, age

@log(level="No.1")
def welcome(num,name):
    print 'welcome:',num,name

if __name__ == '__main__':
    # helloXXT(name='xuxiaotong', age=26)
    # #相当于调用 log(hello())
    welcome(01,name='xxt')
    #01为无名字参数  ，'xxt'为有名字参数