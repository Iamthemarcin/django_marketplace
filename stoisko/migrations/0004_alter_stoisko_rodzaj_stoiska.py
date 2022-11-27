# Generated by Django 4.1.1 on 2022-11-19 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stoisko', '0003_alter_stoisko_rodzaj_stoiska'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stoisko',
            name='rodzaj_stoiska',
            field=models.PositiveSmallIntegerField(choices=[('INNE', 'Inne'), ('ŻYWNOŚĆ', 'Żywność'), ('CIUCHY', 'Ciuchy'), ('AKCESORIA', 'Akcesoria')], default=1),
        ),
    ]