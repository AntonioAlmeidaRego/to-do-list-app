# Generated by Django 4.1 on 2022-08-30 14:36

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
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('type_color', models.PositiveIntegerField(blank=True, choices=[(1, 'Yellow'), (2, 'Blue'), (3, 'gray')])),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
