# Generated by Django 2.2.6 on 2019-10-29 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inlineForm', '0003_auto_20191030_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursescore',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='coursescore',
            name='studentName',
            field=models.CharField(max_length=50),
        ),
    ]