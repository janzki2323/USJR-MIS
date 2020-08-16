# Generated by Django 3.0.8 on 2020-08-16 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Id_Number', models.IntegerField(primary_key=True, serialize=False)),
                ('First_Name', models.TextField(max_length=50)),
                ('Last_Name', models.TextField(max_length=50)),
                ('Email', models.TextField(max_length=100)),
                ('Contact', models.BigIntegerField()),
                ('Password', models.CharField(max_length=20)),
                ('Employee_Picture', models.ImageField(null=True, upload_to='pictures')),
            ],
            options={
                'db_table': 'Employee',
            },
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('Form_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Type', models.CharField(max_length=50)),
                ('Date_Requested', models.DateField(null=True)),
                ('Date_Approved', models.DateField(null=True)),
                ('Status', models.CharField(max_length=20)),
                ('Id_Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Employee')),
            ],
            options={
                'db_table': 'Form',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('Department_ID', models.AutoField(primary_key=True, serialize=False)),
                ('department', models.CharField(max_length=100)),
                ('College', models.CharField(max_length=100)),
                ('Status_Dept', models.TextField(max_length=100)),
                ('Id_Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Employee')),
            ],
            options={
                'db_table': 'Department',
            },
        ),
    ]
