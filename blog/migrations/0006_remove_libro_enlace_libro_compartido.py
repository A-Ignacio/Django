# Generated by Django 4.0.4 on 2022-06-06 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_delete_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='enlace',
        ),
        migrations.AddField(
            model_name='libro',
            name='compartido',
            field=models.CharField(default=str, max_length=50),
            preserve_default=False,
        ),
    ]
