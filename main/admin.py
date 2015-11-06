from django.contrib import admin
from main.models import CustomUser, Thread, Post
# Register your models here.


admin.site.register(CustomUser)
admin.site.register(Thread)
admin.site.register(Post)
