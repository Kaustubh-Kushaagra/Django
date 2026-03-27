from django.contrib import admin
from blog.models import Post,Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']
    
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish','created','updated','status']
    list_filter = ['status', 'created', 'publish', 'author']
    prepopulated_fields = {'slug': ('title',)}
    search_fields=['title','body']
    ordering = ['status', '-publish']
    date_hierarchy = 'publish'
    raw_id_fields = ['author']
    show_facets = admin.ShowFacets.ALWAYS