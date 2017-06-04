from django.contrib import admin
from mia.models import Post,Comment,Board,Category

# Register your models here.
admin.site.register(Comment)
admin.site.register(Board)
admin.site.register(Category)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
admin.site.register(Post, PostAdmin)
