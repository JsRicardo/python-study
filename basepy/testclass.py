class Test:
    default_dic = {
        'testkey1':'testvalue1',
        'testkey2':'testvalue2',
        'testkey3':'testvalue3',
    }
    # 时尚的写法 动态的初始化一个类 不用  name = 'xx' 这种方式
    def __init__(self, **kargs):
        self.__dict__.update(self.default_dic)
        self.__dict__.update(kargs)
    
    def show(self):
        print(self.__dict__)

    @classmethod
    def get_default(cls):
        print(cls.default_dic)