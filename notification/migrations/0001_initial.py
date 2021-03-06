# Generated by Django 2.1.7 on 2019-03-10 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('homedetail', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(help_text='Enter data type', max_length=200)),
                ('detail', models.TextField(help_text='Enter a brief description of the notification', max_length=1000)),
                ('notification_type', models.CharField(blank=True, choices=[('u', 'Utility'), ('o', 'other'), ('a', 'announcement')], default='a', help_text='Room Status', max_length=1)),
                ('RoomID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='homedetail.Room')),
            ],
        ),
    ]
