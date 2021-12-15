from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_movimentodeestoque'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descricao', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Vendas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('forma_de_pagamento', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=120)),
            ],
        ),
    ]
