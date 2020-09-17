# Generated by Django 3.1.1 on 2020-09-17 21:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Benefactor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('curp', models.CharField(max_length=100)),
                ('nss', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=50)),
                ('blood_type', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('salary', models.CharField(max_length=50)),
                ('insured_amount', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'm_insurance_benefactor',
            },
        ),
        migrations.CreateModel(
            name='MedicReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('weight', models.FloatField()),
                ('imc', models.FloatField()),
                ('blood_pressure', models.FloatField()),
                ('uric_acid', models.FloatField()),
                ('cholesterol', models.FloatField()),
                ('triglycerides', models.FloatField()),
                ('creatine', models.FloatField()),
                ('chronic_deseases', models.CharField(max_length=50)),
                ('id_insurance_benefactor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.benefactor')),
            ],
            options={
                'db_table': 'm_insurance_medic_report',
            },
        ),
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('curp', models.CharField(max_length=100)),
                ('nss', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=50)),
                ('blood_type', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('salary', models.CharField(max_length=50)),
                ('insured_amount', models.CharField(max_length=50)),
                ('id_insurance_benefactor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.benefactor')),
            ],
            options={
                'db_table': 'm_insurance_beneficiary',
            },
        ),
    ]
