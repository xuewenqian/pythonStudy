try:
    print('try...')
    #r=10/0
    r=6
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally...')
print('END')

