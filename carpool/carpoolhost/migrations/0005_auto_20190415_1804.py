# Generated by Django 2.2 on 2019-04-15 09:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('carpoolhost', '0004_host'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='hour_of_host',
            field=models.CharField(choices=[('17', '오후 5시'), ('18', '오후 6시'), ('19', '오후 7시'), ('20', '오후 8시'), ('21', '오후 9시'), ('22', '오후 10시'), ('23', '오후 11시'), ('24', '자정'), ('01', '새벽 1시')], default='06', max_length=2),
        ),
        migrations.AddField(
            model_name='host',
            name='minutes_of_host',
            field=models.CharField(choices=[('00', '정각'), ('15', '15분'), ('30', '30분'), ('45', '45분')], default='00', max_length=2),
        ),
        migrations.AlterField(
            model_name='host',
            name='date_of_host',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
