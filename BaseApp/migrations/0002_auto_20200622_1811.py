# Generated by Django 3.0.5 on 2020-06-22 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BaseApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userformmodel',
            name='skills',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
        migrations.AddField(
            model_name='userformmodel',
            name='stream',
            field=models.CharField(blank=True, choices=[('Computer Science and Engineering', 'COMPUTER SCIENCE AND ENGINEERING'), ('Electronics and Communication', 'ELECTRONICS AND COMMUNICATION'), ('Mechanical Engineering', 'MECHANICAL ENGINEERING')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userformmodel',
            name='university',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userformmodel',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userformmodel',
            name='profile_pic',
            field=models.ImageField(blank=True, default='Download.png', null=True, upload_to='profile_pics'),
        ),
    ]
