# Generated by Django 5.0 on 2023-12-21 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0010_alter_city_count_alter_city_img_alter_city_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='jingdu',
            field=models.FloatField(verbose_name='经度'),
        ),
        migrations.AlterField(
            model_name='city',
            name='weidu',
            field=models.FloatField(verbose_name='纬度'),
        ),
    ]
