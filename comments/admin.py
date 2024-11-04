from django.contrib import admin

from comments.models import Comment

@admin.register(Comment)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ["content", "created_at", "car", "author"]
    search_fields = ["content", "created_at", "car", "author"]
    list_filter = ["content", "created_at", "car", "author"]
    readonly_fields = ['created_at']
    fields = [
        "content",
        "created_at",
        "car",
        "author",
    ]