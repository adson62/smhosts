# Generated by Django 3.2.9 on 2021-11-23 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=100)),
                ('tipoHost', models.CharField(choices=[('Access Point', 'ACCESS POINT'), ('Desktop', 'DESKTOP'), ('Impressora', 'IMPRESSORA'), ('Notebook', 'NOTEBOOK'), ('Servidor', 'SERVIDOR'), ('Outros', 'OUTROS')], max_length=20)),
                ('descricao', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Porta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portaServico', models.IntegerField(default=1)),
                ('servico', models.CharField(max_length=200)),
                ('ping', models.FloatField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Host_Porta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host', to='Hosts.host')),
                ('porta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='porta', to='Hosts.porta')),
            ],
            options={
                'ordering': ('porta',),
            },
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataHora', models.DateTimeField(auto_now=True)),
                ('status', models.TextField(blank=True, choices=[('ONLINE', 'ONLINE'), ('OFFLINE', 'OFFLINE'), ('DEMORANDO', 'DEMORANDO')], default='')),
                ('host_porta_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='host_porta_id', to='Hosts.host_porta')),
            ],
        ),
    ]
