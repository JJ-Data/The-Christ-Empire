# Generated by Django 4.0.4 on 2023-02-08 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empirer', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
