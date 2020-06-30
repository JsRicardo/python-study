from testclass import Test
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--addkey1', type=str, help='输入addkey1')
    parser.add_argument('-j','--addkey2', type=str, help='输入addkey2')

    args = parser.parse_args()

    print(args)

    print(vars(args)) #vars 方法 将args转成一个字典

    test = Test(**vars(args))

    test.show()

    test.get_default()