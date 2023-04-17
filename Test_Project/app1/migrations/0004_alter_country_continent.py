# Generated by Django 3.2.18 on 2023-04-16 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_country_continent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='continent',
            field=models.CharField(choices=[('North America', 'north america'), ('Oceania', 'oceania'), ('South America', 'south america'), ('Africa', 'africa'), ('Europe', 'europe'), ('Asia', 'asia'), ('Antarctica', 'antarctica')], default='Asia', max_length=20),
        ),
    ]
