# Generated by Django 4.1 on 2022-08-30 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
        ('car', '0001_initial'),
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, max_length=100)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='car.car')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='owner.owner')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.store')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
