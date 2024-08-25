from django.contrib import admin
from .models import *


# Register your models here.

class productView(admin.ModelAdmin):
    list_display = ('name', 'category', 'desc', 'istrend', 'price', 'cover', 'img2', 'img3', 'img4', 'img5', 'timestamp')


class userView(admin.ModelAdmin):
    list_display = ('name', 'email', 'password', 'timestamp')


admin.site.register(product, productView)
admin.site.register(user, userView)
