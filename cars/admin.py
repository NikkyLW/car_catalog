from django.contrib import admin

from cars.models import Car

@admin.register(Car)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ["make", "model", "year", "created_at", "updated_at"]
    search_fields = ["make", "model"]
    list_filter = ["make", "model", "year", "created_at", "updated_at"]
    readonly_fields = ['created_at', 'updated_at']
    fields = [
        "make",
        "model",
        "year",
        "description",
        "created_at",
        "updated_at",
        "owner",
    ]
    
    #Автоматическое добавление Admin User как создателя записи
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'owner', None) is None:
            obj.owner = request.user
        obj.save()