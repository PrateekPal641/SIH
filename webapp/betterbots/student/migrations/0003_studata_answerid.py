# Generated by Django 4.0.6 on 2022-08-16 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_remove_studata_answerid'),
    ]

    operations = [
        migrations.AddField(
            model_name='studata',
            name='answerid',
            field=models.TextField(default='', verbose_name='answerid'),
        ),
    ]