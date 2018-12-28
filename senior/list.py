print('生成list')

print(list(range(1,11)))

print([x*x for x in range(1,11)])

print(list(x*2 for x in range(1,11)))

print([x*x for x in range(1,11) if x%2==0])

print([m+n for m in 'abc' for n in 'xyz'])

print('-----列出当前目录下文件-----')

import os
print([d for d in os.listdir('.')])

d={'x':'A','y':'B','z':'C'}
for k,v in d.items():
    print(k,'=',v)