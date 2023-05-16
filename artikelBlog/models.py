from django.db import models
#for rigestrestion to admin site
from django.contrib.auth.models import User
from django.urls import reverse

from datetime import datetime, date

from ckeditor.fields import RichTextField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True,on_delete=models.CASCADE)
    bio = models.TextField()
    
    profile_pic =models.ImageField(null=True,blank=True)
    instagram_url =  models.CharField(max_length=255, null=True, blank=True)
    hilokal_url =  models.CharField(max_length=255, null=True, blank=True)
    facebook_url =  models.CharField(max_length=255, null=True, blank=True)
    website_url =  models.CharField(max_length=255, null=True, blank=True)
    
    
    def __str__(self) -> str:
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('homePage')

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) :
        return self.name
    
    def get_absolute_url(self):
        return reverse('homePage')



class Post(models.Model):
    title =  models.CharField(max_length=255)
    
    #to includeing image to database
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    
    title_tag = models.CharField(max_length=255, default= 'artikelBlog')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #body = models.TextField()
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='thisDefaultOfCategory')
    snippets = models.CharField(max_length=255, default='click Link above to read Blog Post ....')
    likes = models.ManyToManyField(User,related_name='blog_posts')
    
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id))) #using url name and than using id to call the page (call id using args)
        # we need some page to know whice page do you want to go, when this post is done
        return reverse('homePage')
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s - %s' % (self.post.title , self.name)
    
    
    