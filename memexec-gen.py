import base64
import sys 

if len(sys.argv) != 2:
    print 'Usage: python memexec-gen.py ./ur-bin-file'

x = open('memexec.tpl', 'rb').read()
y = open(sys.argv[1], 'rb').read()
xkey = 28
z = ''

for i in y:
    z+=chr(ord(i)^xkey)
zz = base64.b64encode(z)


f2 = open('gen.py', 'wb')
lp = x.replace('cicak', zz).replace('kadal', str(xkey))
f2.write(lp)

f2.close()
