# Generated by Django 4.0.1 on 2022-01-27 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0005_alter_review_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='ticket',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='publication.ticket'),
            preserve_default=False,
        ),
    ]
