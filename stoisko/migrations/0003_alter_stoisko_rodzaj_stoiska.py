# Generated by Django 4.1.1 on 2022-11-19 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stoisko', '0002_remove_stoisko_ocena'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stoisko',
            name='rodzaj_stoiska',
            field=models.PositiveSmallIntegerField(choices=[('INNE', 'Inne'), ('ŻYWNOŚĆ', 'Żywność'), ('CIUCHY', 'Ciuchy'), ('AKCESORIA', 'Akcesoria')]),
        ),
    ]