# Generated by Django 5.0.2 on 2024-07-31 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_blog1_chead0_blog1_chead1_blog1_chead2'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleBlog1',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=500)),
                ('heading', models.CharField(default='', max_length=500)),
                ('description', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
