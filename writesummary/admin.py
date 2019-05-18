from django.contrib import admin
from .models import NewSummary


# Register your models here.
class NewSummaryAdmin(admin.ModelAdmin):
    ordering = ('id',)


admin.site.register(NewSummary, NewSummaryAdmin)