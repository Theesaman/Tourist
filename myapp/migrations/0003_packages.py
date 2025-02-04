# Generated by Django 5.1 on 2024-08-15 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_content_contact_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Images/packages')),
                ('day', models.IntegerField()),
                ('place', models.CharField(max_length=20)),
                ('person', models.IntegerField()),
                ('money', models.IntegerField()),
                ('description', models.CharField(max_length=50)),
            ],
        ),
    ]
