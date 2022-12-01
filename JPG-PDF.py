from PIL import Image
import stdio 
import os 
import img2pdf

# Image Storing 
img_path = ("IMG_6201.JPG")

#PDF Path
pdf_path = ("Newpdf.pdf")

#open Image
image= Image.open(img_path)

#Chunk Conversion
pdf_bytes = img2pdf.convert(image.filename)

#open/Creating Pdf
file = open(pdf_path, "wb")

#Write PDF with chunks
file.write(pdf_bytes)

#Close image file
image.close()

#Close PDF File
file.close()

print ("Successfully made pdf file")

