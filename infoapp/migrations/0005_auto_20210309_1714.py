# Generated by Django 3.1.7 on 2021-03-09 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infoapp', '0004_pbsinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pbsinfo',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pbsinfo',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='pbsinfo',
            name='mobile_no',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pbsinfo',
            name='pbs_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]