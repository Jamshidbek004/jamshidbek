# Generated by Django 4.2.3 on 2024-02-02 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_coment_contact_email_reklama_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Coment',
        ),
    ]
