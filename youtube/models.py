  
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.

# # appname ="youtube"
class Channel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    subs = models.ManyToManyField(User, blank=True,related_name="subs")
    my_sub_channels = models.ManyToManyField(User, blank=True,related_name="my_sub_channels")
    def total_subs(self):
        return self.subs.count() 
class Video(models.Model):
    # user=models.ForeignKey(User,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    path=models.CharField(max_length=60,default="/")
    videofile=models.FileField(upload_to='videos/%y', null=True, verbose_name="")
    title=models.CharField(max_length=40)
    desc=models.TextField(max_length=300)
    datetime=models.DateTimeField(auto_now=True,blank=False,null=False)
    like = models.ManyToManyField(User, related_name='likes', blank=True)
    dislike = models.ManyToManyField(User, related_name='dislikes', blank=True)
    def __str__(self):
        return self.title
    def total_likes(self):
        return self.like.count()
    def total_dislikes(self):
        return self.dislike.count()
    
class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField(max_length=300,default="")
    datetime=models.DateTimeField(auto_now=True,blank=False,null=False)
    video=models.ForeignKey(Video,on_delete=models.CASCADE)
    
 


