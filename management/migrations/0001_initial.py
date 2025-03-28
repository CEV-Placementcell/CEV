# Generated by Django 4.2.2 on 2025-01-18 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('e_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('e_name', models.CharField(max_length=50)),
                ('topic', models.CharField(blank=True, max_length=255, null=True)),
                ('dep', models.CharField(blank=True, max_length=255, null=True)),
                ('company', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField()),
                ('date_to', models.DateField(blank=True, null=True)),
                ('time', models.TimeField()),
                ('l_date', models.DateField()),
                ('venue', models.CharField(max_length=100)),
                ('fee', models.IntegerField(default='NULL')),
            ],
        ),
        migrations.CreateModel(
            name='job',
            fields=[
                ('d_no', models.IntegerField(primary_key=True, serialize=False)),
                ('j_pos', models.CharField(max_length=50)),
                ('c_name', models.CharField(max_length=50)),
                ('l_date', models.CharField(max_length=20)),
                ('j_dis', models.CharField(max_length=2500)),
                ('req_s', models.CharField(max_length=500)),
                ('qual', models.CharField(max_length=100)),
                ('sal', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=100)),
                ('poster', models.FileField(default='NULL', upload_to='poster')),
                ('program', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('notify', models.CharField(max_length=500)),
                ('last_date', models.DateField()),
            ],
        ),
    ]
