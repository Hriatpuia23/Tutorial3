from django.contrib import admin
from .models import Post, Profile, Images, Comment, Files


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status')
    list_filter = ('status', 'created', 'updated')
    search_fields = ('author__username', 'title')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('status',)
    date_hierarchy = ('created')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'dob', 'photo')


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('post', 'image')


class FilesAdmin(admin.ModelAdmin):
    list_display = ('post', 'file', 'cover')


admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Comment)
admin.site.register(Files, FilesAdmin)
# Register your models here.
