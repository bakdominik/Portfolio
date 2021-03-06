# Generated by Django 3.1.1 on 2020-09-03 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200)),
                ('thumbnail', models.ImageField(blank=True, default='/images/placeholder.png', null=True, upload_to='images')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
                ('live', models.CharField(max_length=200)),
                ('github', models.CharField(max_length=200)),
                ('tags', models.ManyToManyField(blank=True, null=True, to='base.Tag')),
            ],
        ),
    ]
