# Generated by Django 3.0.7 on 2020-06-23 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITSP', '0003_auto_20200623_2035'),
    ]

    operations = [
        migrations.CreateModel(
            name='itsp_team_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Team_name', models.CharField(max_length=100)),
            ],
        ),
    ]
