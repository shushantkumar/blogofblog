from django.contrib import admin
from blog.models import Post					#importing model post

admin.site.register(Post)						#registering post model in admin

