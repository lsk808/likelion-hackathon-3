# Generated by Django 4.2 on 2023-08-10 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_myuser_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Files/%Y/%m/%d/'),
        ),
    ]
