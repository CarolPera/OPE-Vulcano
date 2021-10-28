from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=120, unique=True)),
                ('estoque', models.IntegerField(verbose_name='estoque atual')),
                ('estoque_minimo', models.PositiveIntegerField(default=0, verbose_name='estoque minimo')),
            ],
        ),
    ]
