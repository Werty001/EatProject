from django.contrib import admin
from Shop.models import Category, Item


class CategoryAdmin(admin.ModelAdmin):
	readonly_fields=('created', 'uploaded')

class ItemAdmin(admin.ModelAdmin):
	readonly_fields=('created', 'uploaded')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)