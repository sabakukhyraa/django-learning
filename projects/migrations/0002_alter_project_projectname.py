# Generated by Django 5.0.4 on 2024-04-18 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='projectName',
            field=models.CharField(max_length=100, null=True),
        ),
    ]