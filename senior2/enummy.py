from enum import Enum,unique

Month=Enum('Month',('jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'))

for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)
    
@unique
class Weekday(Enum):
    Sum=0
    Mon=1
    Tue=2
    Wed=3
    Thu=4
    Fri=5
    Sat=6