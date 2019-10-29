from django.contrib import admin
from posts_app.models import postsModel, replyModel
from django.db import models
from django.forms import TextInput, Textarea

# Register your models here.
admin.site.register(postsModel)
admin.site.register(replyModel)