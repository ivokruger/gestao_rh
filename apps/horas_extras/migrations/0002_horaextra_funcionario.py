# Generated by Django 2.0.1 on 2019-07-01 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0002_auto_20190701_2044'),
        ('horas_extras', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='horaextra',
            name='funcionario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='funcionarios.Funcionario'),
            preserve_default=False,
        ),
    ]
