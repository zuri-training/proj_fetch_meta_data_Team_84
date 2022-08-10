from PIL import Image
from PIL.ExifTags import TAGS

#open image file


imagename="Jofin badge.JPG"

#opening and reading image data

image=Image.open(imagename)
#lets open getexif() method which returns image data
exifdata=image.getexif()

#name: Jofin badege.JPG
#need tags dictionary from pil.exiftags module
#convert id's into name and store them in a variable called tag
#extract the data and store them in a variable called data
#we will decode if the data are in bytes
for tag_id in exifdata:
    #convert
    tag=TAGS.get(tag_id, tag_id)
    #extract the data
    data=exifdata.get(tag_id)
    if isinstance(data, bytes):
        #isinstance(5, int)
        data=data.decode()
        print(f"{tag:40}:{data}") #name:    Jofin badge.JPG
        
