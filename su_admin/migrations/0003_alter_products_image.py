# Generated by Django 4.1.13 on 2024-05-29 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('su_admin', '0002_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='uploads'),
        ),
    ]
