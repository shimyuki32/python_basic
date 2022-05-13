poem = ''
chunk = 10
fin = open('relativity', 'r')
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    print(fragment)
    poem += fragment
    print(poem)
fin.close()

