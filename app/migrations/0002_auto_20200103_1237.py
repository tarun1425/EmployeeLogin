# Generated by Django 3.0.1 on 2020-01-03 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employemodel',
            name='userEmailId',
        ),
        migrations.RemoveField(
            model_name='employemodel',
            name='userGender',
        ),
        migrations.RemoveField(
            model_name='employemodel',
            name='userMobileNo',
        ),
        migrations.RemoveField(
            model_name='employemodel',
            name='userQualification',
        ),
        migrations.AddField(
            model_name='employemodel',
            name='userCity',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='employemodel',
            name='userState',
            field=models.CharField(choices=[('mp', 'MP'), ('up', 'UP'), ('dehli', 'DEHLI'), ('goa', 'GOA')], default='', max_length=5),
        ),
        migrations.AddField(
            model_name='employemodel',
            name='username',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='employemodel',
            name='userFirstName',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='employemodel',
            name='userLastName',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='employemodel',
            name='userPasswsord',
            field=models.CharField(default='', max_length=15),
        ),
    ]
