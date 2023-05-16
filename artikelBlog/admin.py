from django.contrib import admin

# Register your models here.
# for register my models
from .models import Post,Category, Profile,Comment #get post from models #and then don't forget to get category too

admin.site.register(Post) #get post and register to site admin
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)