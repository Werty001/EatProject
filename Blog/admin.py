from django.contrib import admin
from Blog.models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
	readonly_fields=('created', 'uploaded')

class PostAdmin(admin.ModelAdmin):
	readonly_fields=('created', 'uploaded')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)