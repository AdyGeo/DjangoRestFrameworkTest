# Generated by Django 4.0.1 on 2022-03-20 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoBeeDoBeeDoo', '0006_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('L', 'LOW'), ('M', 'MEDIUM'), ('H', 'HIGH')], default='ME', max_length=2, verbose_name='prority'),
        ),
    ]
