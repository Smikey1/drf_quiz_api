# Generated by Django 4.2.6 on 2023-10-07 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_scoremodel_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ScoreModel',
        ),
    ]
