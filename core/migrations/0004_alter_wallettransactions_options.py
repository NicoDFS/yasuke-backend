# Generated by Django 3.2.7 on 2023-01-17 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_profile_auto_logout_timeout'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wallettransactions',
            options={'verbose_name': 'Crypto Topup', 'verbose_name_plural': 'Crypto Topups'},
        ),
    ]
