# Generated by Django 4.1.5 on 2023-03-09 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Subadmin', '0002_alter_officer_officer_proof'),
        ('guest', '0003_owner'),
        ('User', '0002_alter_complaint_complaint_content_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_content', models.TextField(null=True)),
                ('officer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Subadmin.officer')),
                ('owner_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='guest.owner')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='guest.user')),
            ],
        ),
    ]
