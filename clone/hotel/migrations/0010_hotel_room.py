# Generated by Django 4.1.4 on 2022-12-25 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
        ('hotel', '0009_rename_title_tag_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rooms.room'),
        ),
    ]
