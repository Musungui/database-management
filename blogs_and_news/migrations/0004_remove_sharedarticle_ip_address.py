# Generated by Django 4.2.6 on 2023-11-28 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_and_news', '0003_alter_article_writer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sharedarticle',
            name='ip_address',
        ),
    ]