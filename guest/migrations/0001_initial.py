# Generated by Django 4.1.5 on 2023-02-16 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0006_subadmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_contact', models.CharField(max_length=50)),
                ('user_email', models.EmailField(max_length=254, unique=True)),
                ('user_gender', models.CharField(max_length=50)),
                ('user_address', models.TextField(null=True)),
                ('user_zipcode', models.CharField(max_length=50)),
                ('user_photo', models.FileField(upload_to='userdocs/')),
                ('user_proof', models.FileField(upload_to='userdocs/')),
                ('user_pwd', models.CharField(max_length=50, unique=True)),
                ('user_doj', models.DateField(auto_now=True)),
                ('user_place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.place')),
            ],
        ),
    ]
