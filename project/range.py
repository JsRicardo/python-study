# range(n, m, k) 从n -> m 以 k步长跳动，直到m ，结果取头不取尾 k不传默认取1

r = range(1, 3, 1)  # 1 2 3 取头不取尾 -> 2

print(list(r))


s = 'python'

for i in range(0, len(s)):
    print(s[i])
