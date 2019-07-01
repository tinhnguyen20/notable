# Generated by Django 2.2.2 on 2019-07-01 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0005_auto_20190701_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='kind',
            field=models.CharField(choices=[('0', 'New Patient'), ('1', 'Follow Up')], default=0, max_length=16),
            preserve_default=False,
        ),
    ]