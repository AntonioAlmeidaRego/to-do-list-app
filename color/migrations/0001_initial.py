# Generated by Django 4.1 on 2022-08-29 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_color', models.PositiveIntegerField(blank=True, choices=[(1, 'Yellow'), (2, 'Blue'), (3, 'gray')])),
            ],
        ),
    ]