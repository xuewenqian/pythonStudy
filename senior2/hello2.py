def _private_1(name):
    return 'hello,%s' % name
def __private_2(name):
    return 'hi,%s' % name

def greeting(name):
    if len(name)>3:
        return _private_1(name)
    else:
        return __private_2(name)