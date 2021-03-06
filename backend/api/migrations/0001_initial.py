# Generated by Django 2.2.12 on 2020-04-24 16:52

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=25, verbose_name='Name')),
                ('surname', models.CharField(max_length=25, verbose_name='Surname')),
                ('password', models.CharField(max_length=300, verbose_name='Password')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name': 'Event Register',
                'verbose_name_plural': 'Event Register',
                'ordering': ['-created'],
            },
        ),
    ]
