# Generated by Django 5.0 on 2023-12-05 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_anuncio_descricao_alter_anuncio_expira_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='expira',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='tempo',
            field=models.IntegerField(blank=True, default=5),
        ),
    ]