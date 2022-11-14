# Generated by Django 3.2.9 on 2022-11-14 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_application_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=1000)),
                ('designation', models.CharField(max_length=1000)),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to='employees/img/')),
            ],
        ),
    ]