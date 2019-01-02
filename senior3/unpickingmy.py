import pickle
f=open('res\\dump.txt','rb')
d=pickle.load(f)
f.close()
print(d)