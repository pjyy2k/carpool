# Generated by Django 2.2 on 2019-04-15 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('membernumber', models.PositiveIntegerField(help_text='사번', primary_key=True, serialize=False)),
                ('membername', models.CharField(help_text='이름', max_length=10)),
                ('register_tf', models.BooleanField(help_text='등록여부')),
            ],
        ),
    ]
