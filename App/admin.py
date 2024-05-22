from django.contrib import admin
from .models import Profile,Post, Comment, FollowersCount, LikePost, Favourite_post,Announcement, Group_comment,Message


# Register your models here.

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(FollowersCount) 
admin.site.register(LikePost)
admin.site.register(Favourite_post)  
admin.site.register(Announcement)  
admin.site.register(Group_comment)
admin.site.register(Message)