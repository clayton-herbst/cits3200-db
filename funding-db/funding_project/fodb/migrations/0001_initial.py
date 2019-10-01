# Generated by Django 2.2.4 on 2019-09-16 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='funding_opportunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=2500)),
                ('herdc', models.CharField(blank=True, choices=[('1', 'category1'), ('2', 'category2'), ('3', 'category3'), ('4', 'category4')], max_length=15)),
                ('closing_date', models.DateTimeField()),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('last_updated', models.DateField(auto_now=True)),
                ('link', models.URLField(max_length=260)),
                ('limit_per_uni', models.BooleanField(default=False)),
                ('max_amount', models.PositiveIntegerField(blank=True)),
                ('max_duration', models.PositiveIntegerField(blank=True)),
                ('duration_type', models.CharField(choices=[('Y', 'Year'), ('M', 'Month')], max_length=6)),
                ('amount_estimated', models.BooleanField(default=False)),
                ('duration_estimated', models.BooleanField(default=False)),
                ('ecr', models.BooleanField(default=False, verbose_name='ECR')),
                ('travel', models.BooleanField(default=False, verbose_name='Travel')),
                ('visiting', models.BooleanField(default=False, verbose_name='Visiting')),
                ('wir', models.BooleanField(default=False, verbose_name='Women in Research')),
                ('phd', models.BooleanField(default=False, verbose_name='PHD')),
                ('international', models.BooleanField(default=False, verbose_name='International')),
                ('hms', models.BooleanField(default=False, verbose_name='HMS')),
                ('ems', models.BooleanField(default=False, verbose_name='EMS')),
                ('science', models.BooleanField(default=False, verbose_name='Science')),
                ('is_hidden', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Funding Opportunity',
                'verbose_name_plural': 'Funding Opportunities',
                'ordering': ['-name'],
            },
        ),
    ]
