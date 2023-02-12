from django.contrib import admin
from api_v1.models import Quote
# Register your models here.


class QuoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'rating']


admin.site.register(Quote, QuoteAdmin)

