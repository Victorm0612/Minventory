# Generated by Django 3.1.2 on 2020-10-16 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20201016_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='description',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='element',
            name='element_stock',
            field=models.IntegerField(),
        ),
    ]