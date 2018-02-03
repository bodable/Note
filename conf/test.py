import ConfigParser

conf = ConfigParser.ConfigParser()
conf.read('conf.ini')
x = conf.get('test1','x')
conf.set('test1','y','123')
b = conf.get('test2','b')

conf.add_section('test3')
conf.set('test3','u','XXX')
conf.write(open('conf.ini','w'))

print x
print b
