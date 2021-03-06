# Generated by Django 3.0 on 2020-12-14 13:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biblemodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=30)),
                ('good', models.IntegerField(blank=True, default=0, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('url', models.URLField(max_length=300)),
                ('category', models.CharField(max_length=10)),
                ('sex', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
