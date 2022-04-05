# Generated by Django 4.0.3 on 2022-04-05 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('info', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'link url',
                'verbose_name_plural': 'links',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.IntegerField(default=93903)),
                ('short', models.CharField(default='http://127.0.0.1:8000/<django.db.models.fields.IntegerField>/', max_length=50)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.link')),
            ],
            options={
                'verbose_name': 'Results',
            },
        ),
    ]
