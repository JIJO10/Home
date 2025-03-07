# Generated by Django 4.1.5 on 2023-02-04 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subadmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subadmin_name', models.CharField(max_length=50)),
                ('subadmin_contact', models.CharField(max_length=50)),
                ('subadmin_email', models.EmailField(max_length=254, unique=True)),
                ('subadmin_address', models.TextField(null=True)),
                ('subadmin_photo', models.FileField(upload_to='subadmindocs/')),
                ('subadmin_pwd', models.CharField(max_length=50, unique=True)),
                ('subadmin_doj', models.DateField(auto_now=True)),
                ('subadmin_country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.country')),
            ],
        ),
    ]
