# Generated by Django 3.0.6 on 2020-05-18 21:37

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('golfprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('course_description', models.TextField(blank=True, null=True)),
                ('holes', models.IntegerField(blank=True, null=True)),
                ('green_fee', models.IntegerField(blank=True, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('facility_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('img_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('facility_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('facility_email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('friendly_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TeeTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tee_time', models.DateTimeField()),
                ('price', models.IntegerField(blank=True, null=True)),
                ('booked', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='golfprofile.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.District'),
        ),
    ]
