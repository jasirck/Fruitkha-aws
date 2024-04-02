# Generated by Django 3.2.12 on 2024-03-07 06:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wallet", "0003_wallet_list_msg"),
    ]

    operations = [
        migrations.RenameField(
            model_name="wallet_list",
            old_name="ammount",
            new_name="amount",
        ),
        migrations.RemoveField(
            model_name="wallet",
            name="ammount",
        ),
        migrations.AddField(
            model_name="wallet",
            name="amount",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
