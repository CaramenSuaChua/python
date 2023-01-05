# Generated by Django 3.2.16 on 2022-11-22 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0005_auto_20211104_0957'),
        ('orders', '0007_orderitem_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateCate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PostCate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='manage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ad_cate', to='store.category')),
                ('orders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ad_order', to='orders.order')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ad_product', to='store.product')),
            ],
        ),
    ]
