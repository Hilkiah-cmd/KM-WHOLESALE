# Generated by Django 4.1.3 on 2022-11-03 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('km', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_code', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('discount', models.FloatField()),
            ],
        ),
    ]
