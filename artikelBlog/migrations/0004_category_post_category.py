# Generated by Django 4.2 on 2023-04-29 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artikelBlog', '0003_post_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='thisDefaultOfCategory', max_length=255),
        ),
    ]
