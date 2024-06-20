# Generated by Django 4.1.13 on 2024-06-20 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('su_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_code', models.CharField(default=None, max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.CharField(default=None, max_length=255)),
                ('delivery_address', models.CharField(default=None, max_length=255)),
                ('order_total', models.CharField(default=None, max_length=255)),
                ('status', models.CharField(default=None, max_length=255)),
                ('contact_number', models.CharField(default=None, max_length=255)),
                ('delivery_mode', models.CharField(default=None, max_length=255)),
                ('pincode', models.CharField(default=None, max_length=255)),
                ('state', models.CharField(default=None, max_length=255)),
                ('country', models.CharField(default=None, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='uploads')),
                ('category', models.CharField(max_length=100)),
                ('selling_price', models.CharField(max_length=100)),
                ('mrp', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(default=None, max_length=255)),
                ('message', models.CharField(default=None, max_length=255)),
                ('status', models.CharField(default=None, max_length=255)),
                ('rating', models.CharField(default=None, max_length=255)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='su_admin.products')),
            ],
        ),
        migrations.CreateModel(
            name='Order_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_code', models.CharField(default=None, max_length=255)),
                ('user_id', models.CharField(max_length=255)),
                ('qty', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('total', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('discount', models.CharField(default=None, max_length=255)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='su_admin.products')),
            ],
        ),
    ]
