# Generated by Django 3.1.4 on 2021-03-16 05:32

from django.db import migrations, models
import mcserver.models


class Migration(migrations.Migration):

    dependencies = [
        ('mcserver', '0010_auto_20201214_0405'),
    ]

    operations = [
        migrations.AddField(
            model_name='trial',
            name='name',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='json',
            field=models.FileField(upload_to=mcserver.models.random_filename),
        ),
        migrations.AlterField(
            model_name='result',
            name='trc',
            field=models.FileField(upload_to=mcserver.models.random_filename),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=mcserver.models.random_filename),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_thumb',
            field=models.FileField(blank=True, null=True, upload_to=mcserver.models.random_filename),
        ),
    ]
