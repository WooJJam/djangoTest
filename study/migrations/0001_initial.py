# Generated by Django 4.1.1 on 2022-09-17 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(db_column='userid', max_length=50, verbose_name='userid')),
                ('passwd', models.CharField(db_column='passwd', max_length=50, verbose_name='passwd')),
                ('email', models.CharField(blank=True, db_column='email', max_length=30, verbose_name='email')),
            ],
        ),
    ]
