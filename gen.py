"""Converts an image to CSS."""

# Uses Pillows module to process image.
from PIL import Image
import os
import sys

# Size to reduce one dimenson of image to.
max_size = 512, 512

# Get the image from file.

filename = os.path.join(sys.path[0], input("Enter filename of image: ").strip().lower())
image = Image.open(filename)

# Reduce size of image, keep aspect ratio.
image.thumbnail(max_size, Image.LANCZOS)

# Get rgb values for each pixel.
pixels = image.load()

# Get size of reduced image.
size = image.size

# Create HTML file for output.
file = open(os.path.join(sys.path[0], os.path.splitext(os.path.basename(filename))[0] + '.html'), "w")

# HTML headers and metadata.
file.write('<!DOCTYPE html>\n')
file.write('<html>\n')
file.write('<head>\n')
file.write('<meta name="viewport" content="width=device-width, initial-scale=1">\n')

file.write('<style>\n') # Styles to remove borders.
file.write('.line { display:block;\n\tborder: 0px;\n\tpadding: 0px;\n\tfont-size: 0px;\n\tborder-image-width: 0px;\n}\n')
file.write('.pixel { display: inline-block;\n\theight: 2px;\n\twidth: 2px;\n\tborder: 0px;\n\tpadding: 0px;\n\tfont-size: 0px;\n\tborder-image-width: 0px;\n}\n')
file.write('</style>\n')

file.write('</head>\n')
file.write('<body>\n')

# Create a div element for each row of pixels, and a span element of each column.
# The background-color of each span is taken from corresponding pixel in the image.
for px in range(size[1]):
    file.write('\t<div class="line">')
    for py in range(size[0]):
        pixelColor = str(pixels[py, px])
        file.write('<span class="pixel", style="background-color: rgb' + pixelColor + ';"></span>')
    file.write('</div>\n')

file.write('</body>\n')
file.write('</html> ')
file.write('')

file.close()