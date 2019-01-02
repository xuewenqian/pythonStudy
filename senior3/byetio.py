from io import BytesIO

f=BytesIO()
print(f.write('中文'.encode('utf-8')))
print(f.getvalue())

