# Generated by Django 4.0 on 2022-02-07 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_category_options_remove_product_subcategory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='p_image',
            field=models.ImageField(default='products/m2.png', upload_to='products/'),
        ),
    ]
