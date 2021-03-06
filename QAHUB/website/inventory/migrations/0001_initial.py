# Generated by Django 3.2.8 on 2021-11-03 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='materialForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_of_the_Material_per_specification', models.CharField(max_length=100, null=True)),
                ('Site_Material_Code', models.CharField(max_length=100, null=True)),
                ('Lot_Number', models.CharField(max_length=100, null=True)),
                ('Purchase_Order', models.CharField(max_length=100, null=True)),
                ('Material_Identity', models.CharField(max_length=100, null=True)),
                ('Quantity', models.CharField(max_length=100, null=True)),
                ('Supplier_Name', models.CharField(max_length=100, null=True)),
                ('Supplier_Lot_Number', models.CharField(max_length=100, null=True)),
                ('Manufacturer', models.CharField(max_length=100, null=True)),
                ('Site_Lot_Number', models.CharField(max_length=100, null=True)),
                ('Receipt_Date', models.CharField(max_length=100, null=True)),
                ('Personnel', models.CharField(max_length=100, null=True)),
                ('Comments', models.CharField(max_length=400, null=True)),
                ('MSDS', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
