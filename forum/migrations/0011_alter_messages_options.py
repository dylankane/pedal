# Generated by Django 3.2.19 on 2023-07-29 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0010_rename_contact_messages'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messages',
            options={'ordering': ['-date_sent']},
        ),
    ]