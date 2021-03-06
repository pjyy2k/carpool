# Generated by Django 2.2 on 2019-04-15 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carpoolhost', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ['membername']},
        ),
        migrations.CreateModel(
            name='RegMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memberemail', models.EmailField(max_length=254)),
                ('memberpw', models.CharField(max_length=50)),
                ('membernumber', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='carpoolhost.Member')),
            ],
            options={
                'ordering': ['membernumber'],
            },
        ),
    ]
