bdata = bytes(range(256))
len(bdata)

fout = open('bfile', 'wb')
fout.write(bdata)
fout.close()
size = len(bdata)
offset = 0
