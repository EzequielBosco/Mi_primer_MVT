# Generated by Django 4.0.3 on 2022-10-26 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion',
            name='construido_por',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
