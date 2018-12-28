from collections import Iterator
from collections import Iterable
print(isinstance((x for x in range(10)),Iterator))

print(isinstance([1,2,3],Iterator))
print(isinstance([1,2,3],Iterable))
print(isinstance(iter([1,2,3]),Iterator))

