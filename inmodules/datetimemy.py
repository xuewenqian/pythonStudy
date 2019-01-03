from datetime import datetime

#当前时间
now=datetime.now()
print(now)
print(type(now))

#获取指定日期和时间
dt=datetime(2015,4,19,12,20)
print(dt)

#datetime转换为timestamp
print(dt.timestamp())

#timestamp转换为datetime
t=1429417200.0
print(datetime.fromtimestamp(t))