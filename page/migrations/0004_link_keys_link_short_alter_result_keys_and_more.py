# Generated by Django 4.0.3 on 2022-04-05 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_remove_result_key_result_keys_alter_result_short'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='keys',
            field=models.IntegerField(default=59017),
        ),
        migrations.AddField(
            model_name='link',
            name='short',
            field=models.CharField(default='http://127.0.0.1:8000/59017/', editable=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='result',
            name='keys',
            field=models.IntegerField(default=72250),
        ),
        migrations.AlterField(
            model_name='result',
            name='short',
            field=models.CharField(default='http://127.0.0.1:8000/72250/', max_length=50),
        ),
    ]
