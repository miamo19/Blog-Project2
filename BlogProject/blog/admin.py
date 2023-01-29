#from django
from django.contrib import admin
#from project
from .models import Post, Comment

# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug', 'status','created_on')
#     list_filter = ("status",)
#     search_fields = ['title', 'content']
#     prepopulated_fields = {'slug': ('title',)}

# admin.site.register(Post, PostAdmin)

# ++++++👆👆👆👆OR+++++Do👇👇👇👇

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Name: PostAdmin
    Description: This class register the model class Post from the models.py file
    """
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Name: CommentAdmin
    Description: This class register the model class Comment from the models.py file
    """
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        print(queryset)
        queryset.update(active=True)
