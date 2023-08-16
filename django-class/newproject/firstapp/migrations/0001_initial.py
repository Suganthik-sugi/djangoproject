# Generated by Django 4.2.1 on 2023-07-20 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20, verbose_name='First Name')),
                ('lname', models.CharField(max_length=20, verbose_name='Last Name')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='User Name')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='Email id')),
                ('phno', models.CharField(max_length=20, unique=True, verbose_name='Phone number')),
                ('address', models.CharField(max_length=20, unique=True, verbose_name='Address')),
                ('gstin', models.CharField(max_length=20, unique=True, verbose_name='gstin')),
                ('officename', models.CharField(max_length=20, unique=True, verbose_name='Office Name')),
                ('gmname', models.CharField(max_length=20, unique=True, verbose_name='GM Name')),
                ('officeaddress', models.CharField(max_length=20, unique=True, verbose_name='Office address')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.IntegerField(null=True)),
                ('modified_by', models.IntegerField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=True)),
            ],
        ),
    ]
