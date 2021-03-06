# Generated by Django 2.2.5 on 2019-09-06 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_campaign_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('pre_text', models.CharField(max_length=100)),
                ('article_url', models.URLField()),
                ('html_content', models.TextField(max_length=1000)),
                ('plain_text', models.TextField(max_length=1000)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('sent', models.BooleanField(default=False)),
            ],
        ),
    ]
