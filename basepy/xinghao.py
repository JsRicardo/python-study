# *args 代表接下来的参数放入args中 => 元组
# **args 代表将接下来的参数放入键值对中 => 字典

def test(a, b, *args, **kargs):
    print(args)
    for ar in args:
        print(ar)
    
    print(kargs)
    for kw in kargs:
        print(kw, kargs[kw])


test(1, 2, 3, 4, 5, 6, aa = 1, bb = 3)

