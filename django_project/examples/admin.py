from django.contrib import admin
from examples.models import MyModel


@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('data', 'created_at')
    search_fields = ('data',)
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)
