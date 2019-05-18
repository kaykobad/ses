from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Document(models.Model):
    main_body = RichTextField(blank=True, null=True)
    com_64125 = models.TextField(blank=True, null=True)
    wr = models.TextField(blank=True, null=True)
    tr = models.TextField(blank=True, null=True)
    num_rating = models.IntegerField(default=0)
    avg_com = models.FloatField(blank=True, null=True, default=0.0)
    avg_wr = models.FloatField(blank=True, null=True, default=0.0)
    avg_tr = models.FloatField(blank=True, null=True, default=0.0)

    def __str__(self):
        return str(self.id) + ' - ' + self.main_body[:25] + " >==> " + str(self.num_rating)
    

class Rating(models.Model):
    aid = models.IntegerField()
    com_score = models.FloatField()
    wr_score = models.FloatField()
    tr_score = models.FloatField()

    def __str__(self):
        return str(self.aid)
    