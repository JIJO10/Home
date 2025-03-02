# Generated by Django 4.1.5 on 2023-02-24 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Subadmin', '0002_alter_officer_officer_proof'),
        ('guest', '0003_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_title', models.CharField(max_length=50)),
                ('complaint_content', models.CharField(max_length=50)),
                ('complaint_date', models.DateField(default=0)),
                ('complaint_replay', models.TextField(null=True)),
                ('complaint_status', models.IntegerField(default=0)),
                ('officer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Subadmin.officer')),
                ('owner_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='guest.owner')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='guest.user')),
            ],
        ),
    ]
