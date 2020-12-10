# Generated by Django 3.1 on 2020-12-10 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pigeon', '0010_auto_20201210_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pigeon',
            name='father',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pigeonFather', to='pigeon.pigeon', unique=True),
        ),
        migrations.AlterField(
            model_name='pigeon',
            name='mother',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pigeonMother', to='pigeon.pigeon', unique=True),
        ),
    ]
