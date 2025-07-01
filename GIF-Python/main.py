import imageio.v3 as iio

file_names = ['img1.png', 'img2.png', 'img3.png']
images = [ ]

for file_name in file_names:
    images.append(iio.imread(file_name))

iio.imwrite('charmander.gif', images, duration = 200, loop = 0) 