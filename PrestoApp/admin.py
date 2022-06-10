from django.contrib import admin

# Register your models here.
from PrestoApp.models import ItemMenu, CategoryMenu, Post
admin.site.register(CategoryMenu)
admin.site.register(ItemMenu)
admin.site.register(Post)
