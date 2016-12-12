from django.db import models
from uuid import uuid1
from django.utils import timezone

def generate_id():
    return str(uuid1()).replace("-", "")
    
class ImageManager(models.Manager):
    def create_image(self, original_filename, id=""):
        image = self.create(original_filename=original_filename, id=id)
        return image
        
class TagManager(models.Manager):
    def create_tag(self, tag_text):
        tag = self.create(tag_text=tag_text)
        return tag
        
class ImagesTagsManager(models.Manager):
    def create_imagetag(self, image_id, tag_id, vote):
        imagetag = self.create(image_id=image_id, tag_id=tag_id, vote=vote)
        return imagetag
        
        
        

class Image(models.Model):
    id = models.CharField(primary_key=True, default=generate_id, editable=False, max_length=255)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    original_filename = models.CharField(max_length=200, default=None)
    objects = ImageManager()
    
class Tag(models.Model):
    tag_text = models.CharField(primary_key=True, max_length=200, editable=False, default=generate_id)
    objects = TagManager()
    
class ImagesTags(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ForeignKey(Image)
    tag = models.CharField(max_length=200, editable=False)
    vote = models.BigIntegerField(default=1)
    objects = ImagesTagsManager()
    