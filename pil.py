from PIL import Image

output_size = (600, 250)

i = Image.open('img/logo.jpg')

i.thumbnail(output_size)

i.save('./img/logo.jpg')
