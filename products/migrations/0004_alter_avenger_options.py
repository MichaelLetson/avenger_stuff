# Generated by Django 3.2 on 2022-10-25 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='avenger',
            options={'verbose_name_plural': 'Avengers'},
        ),
    ]