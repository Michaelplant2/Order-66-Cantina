from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consumable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('description', models.TextField()),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('cuisine_type', models.CharField(choices=[('FD', 'Food'), ('DR', 'Drink')], max_length=2)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
