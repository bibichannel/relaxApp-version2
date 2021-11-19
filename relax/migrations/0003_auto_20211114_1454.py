# Generated by Django 3.1.2 on 2021-11-14 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relax', '0002_auto_20211114_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to='music/'),
        ),
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(default='https://cdn.pixabay.com/photo/2014/04/02/10/57/vinyl-305025_640.png', upload_to='music-background/'),
        ),
        migrations.AlterField(
            model_name='song',
            name='stt',
            field=models.TextField(default=''),
        ),
    ]