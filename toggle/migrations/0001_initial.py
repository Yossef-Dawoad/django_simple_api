# Generated by Django 4.0.4 on 2022-05-10 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveLock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='activelock(1)', max_length=200)),
                ('state', models.BooleanField()),
                ('created_In', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
