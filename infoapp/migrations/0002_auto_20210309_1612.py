# Generated by Django 3.1.7 on 2021-03-09 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='pbs_code',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='pbs_name',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]