# Generated by Django 4.2 on 2023-04-18 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0002_alter_mails_sno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mails',
            name='sno',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
