# Generated by Django 2.2 on 2019-09-08 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190908_1239'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-publish_date', 'updated', '-timestamp']},
        ),
    ]
