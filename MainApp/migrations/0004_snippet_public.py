# Generated by Django 4.1.7 on 2023-08-24 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_snippet_user_alter_snippet_creation_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]