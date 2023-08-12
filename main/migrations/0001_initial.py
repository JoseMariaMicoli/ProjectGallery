# Generated by Django 4.2.4 on 2023-08-12 22:02

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('altText', models.TextField(blank=True, null=True)),
                ('hashtag', models.CharField(blank=True, max_length=300, null=True)),
                ('squareImage', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default_square.jpg', force_format=None, keep_meta=True, quality=-1, scale=None, size=[1000, 1000], upload_to='square')),
                ('landscapeImage', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default_land.jpg', force_format=None, keep_meta=True, quality=-1, scale=None, size=[2678, 1618], upload_to='landscape')),
                ('tallImage', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default_tall.jpg', force_format=None, keep_meta=True, quality=-1, scale=None, size=[1618, 2878], upload_to='tall')),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
        ),
    ]
