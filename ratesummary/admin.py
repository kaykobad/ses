from django.contrib import admin
from . models import Document, Rating


# Register your models here.
class RatingAdmin(admin.ModelAdmin):
    list_display = ('aid', 'com_score', 'wr_score', 'tr_score')
    ordering = ('aid',)


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'num_rating', 'avg_com', 'avg_wr', 'avg_tr')
    ordering = ('id',)


admin.site.register(Rating, RatingAdmin)
admin.site.register(Document, DocumentAdmin)
