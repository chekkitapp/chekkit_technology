# Generated by Django 2.0.7 on 2018-07-23 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('production_date', models.DateTimeField()),
                ('expiry_date', models.DateTimeField()),
                ('batch_number', models.IntegerField(blank=True, null=True, unique=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.IntegerField(unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('batch_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Batch')),
            ],
        ),
        migrations.CreateModel(
            name='ProductLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='images')),
                ('is_active', models.BooleanField(default=False)),
                ('manufacturer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Manufacturer')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_line',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.ProductLine'),
        ),
    ]
