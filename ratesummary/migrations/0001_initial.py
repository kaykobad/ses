# Generated by Django 2.2.1 on 2019-05-18 11:23

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('com_64125', models.TextField(blank=True, null=True)),
                ('wr', models.TextField(blank=True, null=True)),
                ('tr', models.TextField(blank=True, null=True)),
                ('num_rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aid', models.IntegerField()),
                ('com_score', models.IntegerField()),
                ('wr_score', models.IntegerField()),
                ('tr_score', models.IntegerField()),
            ],
        ),
    ]
