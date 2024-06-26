# Generated by Django 5.0.6 on 2024-06-06 04:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(default='Card Name', max_length=255)),
                ('scryfall_id', models.CharField(default='0', max_length=255)),
                ('tcg_id', models.IntegerField(default=0)),
                ('set', models.CharField(default='Set Name', max_length=255)),
                ('collector_number', models.CharField(default='0', max_length=10)),
                ('finish', models.CharField(choices=[('foil', 'Foil'), ('nonfoil', 'Nonfoil')], default='nonfoil', max_length=10)),
                ('print_uri', models.URLField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='cards.collection')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discord_id', models.CharField(max_length=255, unique=True)),
                ('discord_username', models.CharField(max_length=255)),
                ('collection', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_collection', to='cards.collection')),
            ],
        ),
        migrations.AddField(
            model_name='collection',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_collection', to='cards.user'),
        ),
    ]
