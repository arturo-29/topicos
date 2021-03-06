# Generated by Django 2.2.24 on 2021-12-04 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=8)),
                ('tipo', models.CharField(choices=[('ORDINARIA', 'ORDINARIA'), ('REPITE', 'REPITE'), ('ESPECIAL', 'ESPECIAL')], default='available', max_length=45)),
                ('carrera', models.CharField(max_length=25)),
                ('fk_persona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.persona')),
            ],
        ),
    ]
