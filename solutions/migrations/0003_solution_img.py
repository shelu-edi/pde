# Generated by Django 3.2.9 on 2022-07-21 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0002_solution_solution_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='img',
            field=models.ImageField(default=1, upload_to='solutions/img/'),
            preserve_default=False,
        ),
    ]
