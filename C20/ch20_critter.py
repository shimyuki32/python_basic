from PIL import Image

stache = Image.open("O'Reilly_logo.png")
critter = Image.open('watermark.jpeg')

stache.putalpha(100)

img = Image.new('RGBA', critter.size, (255, 255, 255, 0))
img.paste(critter, (0, 0))
img.paste(stache, (45, 90), mask=stache)
img.show()