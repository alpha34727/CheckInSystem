# Generated by Django 3.2.15 on 2023-01-07 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MemberID', models.IntegerField()),
                ('Start', models.DateTimeField()),
                ('End', models.DateTimeField()),
                ('Info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LeaveApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ApplierID', models.IntegerField()),
                ('AttendantID', models.IntegerField()),
                ('LeaveType', models.BooleanField()),
                ('LeaveInfo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
            ],
        ),
    ]