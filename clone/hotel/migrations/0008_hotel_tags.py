# Generated by Django 4.1.4 on 2022-12-24 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='hotel.tag'),
        ),
    ]