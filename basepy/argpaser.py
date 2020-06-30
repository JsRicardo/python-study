# -*- coding: utf-8 -*-

import argparse

def main():
    pa = argparse.ArgumentParser()
    pa.add_argument('--teststr', '-i', type=str, help='哈哈哈哈')
    # args='+' 代表传入的是一个数组
    pa.add_argument('--testlist', '-l', nargs="+", type=int, help='哈哈哈哈')
    args = pa.parse_args()
    
    print(args.teststr)
    print(args.testlist)
    
if __name__ == '__main__':
    main()