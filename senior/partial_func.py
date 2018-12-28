print(int('12345'))

print(int('12345',base=10))

import functools
int2=functools.partial(int,base=2)
print(int2('1000000'))