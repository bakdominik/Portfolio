# Generated by Django 3.1.1 on 2020-09-06 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20200906_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(blank=True, default='images/placeholder.png', null=True, upload_to='images'),
        ),
    ]