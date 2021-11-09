# Generated by Django 3.2.9 on 2021-11-08 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataHora', models.DateTimeField(auto_now=True)),
                ('status', models.TextField(choices=[('ONLINE', 'ONLINE'), ('OFFLINE', 'OFFLINE'), ('DEMORANDO', 'DEMORANDO')])),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=100)),
                ('servico', models.CharField(default='', max_length=100)),
                ('tipoHost', models.CharField(choices=[('Access Point', 'ACCESS POINT'), ('Desktop', 'DESKTOP'), ('Impressora', 'IMPRESSORA'), ('Notebook', 'NOTEBOOK'), ('Servidor', 'SERVIDOR'), ('Outros', 'OUTROS')], default='ONLINE', max_length=20)),
                ('descricao', models.CharField(blank=True, max_length=200)),
                ('status', models.CharField(blank=True, default='', max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portas', to='Hosts.host')),
            ],
        ),
    ]
