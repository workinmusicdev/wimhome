# Generated by Django 4.1 on 2024-02-27 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0003_review_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazine',
            name='img',
            field=models.ImageField(default=1, upload_to='magazine_img/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partenaire',
            name='img',
            field=models.ImageField(default=2, upload_to='partenaire_img/'),
            preserve_default=False,
        ),
    ]
