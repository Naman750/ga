# Generated by Django 4.0.6 on 2023-04-15 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_shoppingcart_shoppingcartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.IntegerField()),
                ('expiry_date', models.IntegerField()),
                ('cvv', models.IntegerField()),
            ],
        ),
    ]
