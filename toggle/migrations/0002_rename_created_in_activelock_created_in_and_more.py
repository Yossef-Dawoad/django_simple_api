# Generated by Django 4.0.4 on 2022-05-10 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toggle', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activelock',
            old_name='created_In',
            new_name='created_in',
        ),
        migrations.RemoveField(
            model_name='activelock',
            name='name',
        ),
        migrations.AddField(
            model_name='activelock',
            name='init_state',
            field=models.BooleanField(default=False),
        ),
    ]