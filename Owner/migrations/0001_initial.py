# Generated by Django 4.1.5 on 2023-02-17 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guest', '0003_owner'),
        ('Admin', '0006_subadmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_name', models.CharField(max_length=50)),
                ('rent_image', models.FileField(upload_to='rentdocs/')),
                ('rent_details', models.TextField(null=True)),
                ('rent_amount', models.CharField(max_length=50)),
                ('rent_vsts', models.IntegerField(default=0)),
                ('owner_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='guest.owner')),
                ('renttype_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.renttype')),
            ],
        ),
    ]
