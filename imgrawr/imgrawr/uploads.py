import string
import random
from django.db import models
from . import models
from uuid import uuid1
import os.path
from PIL import Image, ImageFile

def generate_id(filetype=""):
    ext = ""
    if filetype == 'image/jpeg':
        ext = ".jpg"
    if filetype == 'image/png':
        ext = ".png"
    if filetype == 'image/gif':
        ext = ".gif"
    
    return str(uuid1()).replace("-", "") + ext

def handle_uploaded_file(img, tags):
    tag_count = models.Tag.objects.filter(tag_text="imgrawr").count() #models.Tag.objects.raw("SELECT count(*) FROM imgrawr_tag where tag_text = 'imgrawr'")
    if tag_count == 0:
            new_tag = models.Tag.objects.create_tag(tag_text="imgrawr")
            new_tag.save()
    
    new_img_id = generate_id(img.content_type)
    
    if save_file(new_img_id, img):    
        new_img = models.Image.objects.create_image(original_filename=img.name, id=new_img_id)
        new_img.save()
    
        imgrawr = models.Tag.objects.filter(tag_text="imgrawr")[0]
        imgrawr_id = imgrawr.tag_text
        imagetag = models.ImagesTags.objects.create_imagetag(new_img_id, imgrawr_id, 1)
        imagetag.save()
    
        if tags != "":
            tag_list = tags.split(" ")
            for t in tag_list:
                tag_count = models.Tag.objects.filter(tag_text=t).count()
                if tag_count == 0:
                    new_tag = models.Tag.objects.create_tag(tag_text=t)
                    new_tag.save()
                imagetag = models.ImagesTags.objects.create_imagetag(new_img_id, t, 1)
                imagetag.save()
                
        return new_img_id
    else:
        return None
    
def save_file(filename, img):
    with open('../tmp/' + filename, 'wb+') as destination:
        for chunk in img.chunks():
            destination.write(chunk)
          
    tmp = Image.open('../tmp/' + filename)
    width, height = tmp.size
    
    if width >= 180:
        tmp.save('../images/' + filename)
        ratio = width / 180
        size = 180, (height / ratio)
        tmp.thumbnail(size, Image.ANTIALIAS)
        shave = height - 180
        tmp.crop((0, 0, 180, height-shave)).save('../images/thumbnails/' + filename)
        return os.path.isfile('../images/' + filename) 
    