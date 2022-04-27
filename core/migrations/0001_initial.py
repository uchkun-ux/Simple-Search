# Generated by Django 4.0 on 2022-04-26 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('age', models.IntegerField(default=18)),
                ('job', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Worker',
                'verbose_name_plural': 'Employees',
            },
        ),
    ]