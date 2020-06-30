# -*- coding: utf-8 -*-

class Animal:
      
    size = 'small'
    
    def voice(self):
        print(self.name)
        
    def eat(self, val):
        print(self.name + ' eat ' + val)
    
    @classmethod
    def handle(cls): # cls代表这个类
        print('这是一个类方法，这是类上的属性{}'.format(cls.size))
    
    @staticmethod
    def staticm():
        print('这是一个类的静态方法')

    @property
    def getsize(self): # 获取类的私有属性  相当于get方法
        print('这是一个类的属性')
        return self.size
    
    @getsize.setter
    def getsize(self, size): # deleter 删除属性的方法  相当于delete
        print('这是设置类属性的方法 相当于set方法')
        self.size = size
        
    @getsize.deleter
    def getsize(self, size): # deleter 删除属性的方法  相当于delete
        print('这是类属性的方法 相当于delete方法')
        self.size = None # 直接将属性赋值为none的话 这个属性还是存在，只能通过deleter完全删除

class Miao(Animal): # 继承
    
    def __init__(self, name): #__init__ 构造方法
        self.name = name



class BosiMiao (Miao):
    
    def __init__(self, name, age):
        super(BosiMiao, self).__init__(name) # super使用父类的构造方法
        self.age = age
        print('{} is {} y old'.format(self.name,  self.age))
        
    def eat(self, val): # 重写父类的方法
        print('{} eat so many {}'.format(self.name, val))
        
        

print(__name__)
if __name__ == '__main__':
# 当文件被引入其他文件，其他文件执行时会执行一遍这个文件，通过这个判断，不执行下面的私有代码
    a = Miao('miaomiao')
        
    a.eat('fish')
            
    b = BosiMiao('bosimiao', 3)
    
    b.eat('small fish')
    
    isinstance(a, Animal) # 实例查找原型
    issubclass(Miao, Animal) # 判定继承关系



