# Generated by Django 2.2.1 on 2019-05-18 05:39

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('is_summarized', models.IntegerField(default=0)),
            ],
        ),
    ]
