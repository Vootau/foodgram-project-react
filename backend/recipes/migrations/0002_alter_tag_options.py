# Generated by Django 3.2.15 on 2022-10-11 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['-id'], 'verbose_name': 'Tag', 'verbose_name_plural': 'Tags'},
        ),
    ]
