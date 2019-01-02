import pickle
d=dict(name='bob',age=20,score=99)
print(pickle.dumps(d))

#序列化写入磁盘
f=open('res\\dump.txt','wb')
pickle.dump(d,f)
f.close()