# Generated by Django 2.1 on 2018-08-03 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0003_auto_20180803_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumertask',
            name='category',
            field=models.CharField(blank=True, choices=[('clean AC', 'clean AC'), ('clean car', 'clean car'), ('clean fridge', 'clean fridge'), ('clean room', 'clean room')], default=None, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='consumertask',
            name='status',
            field=models.CharField(blank=True, choices=[('created', 'created'), ('in_progress', 'in_progress'), ('completed', 'completed')], default='created', max_length=300, null=True),
        ),
    ]
