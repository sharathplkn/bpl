# Generated by Django 5.0.6 on 2025-01-08 06:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0002_alter_players_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('card_image', models.ImageField(upload_to='player_cards/')),
                ('base_price', models.DecimalField(decimal_places=2, default=20, max_digits=10)),
                ('year', models.IntegerField()),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='players', to='auction.team')),
            ],
        ),
        migrations.DeleteModel(
            name='players',
        ),
    ]
