from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class NewSummary(models.Model):
    main_body = RichTextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    is_summarized = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.id) + ' - ' + self.main_body[:25] + " >==> " + str(self.is_summarized)
