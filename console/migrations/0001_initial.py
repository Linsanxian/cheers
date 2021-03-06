# Generated by Django 3.0.7 on 2020-06-17 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=254)),
                ('customer_code', models.CharField(max_length=254)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('module_name', models.CharField(max_length=254)),
                ('description', models.CharField(default='Null', max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=254)),
                ('product_code', models.CharField(max_length=254)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('version', models.CharField(max_length=254)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.Customer')),
                ('module_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.Module')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.Product')),
            ],
        ),
    ]
