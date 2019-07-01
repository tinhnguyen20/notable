# Generated by Django 2.2.2 on 2019-07-01 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0003_visit_notes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Visit',
            new_name='Appointment',
        ),
        migrations.AlterModelOptions(
            name='patient',
            options={'ordering': ('first_name',)},
        ),
        migrations.AlterModelOptions(
            name='physician',
            options={'ordering': ('last_name',)},
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='physician',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='physician',
            name='created',
        ),
        migrations.AddField(
            model_name='patient',
            name='last_name',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='physician',
            name='last_name',
            field=models.CharField(default=' ', max_length=64),
            preserve_default=False,
        ),
    ]
