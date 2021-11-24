# Generated by Django 3.2.8 on 2021-11-24 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app10', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=10)),
                ('Description', models.CharField(max_length=50)),
                ('Category', models.CharField(max_length=10)),
                ('Price', models.IntegerField()),
                ('Photo', models.ImageField(blank=True, null=True, upload_to='gallery/')),
            ],
        ),
    ]