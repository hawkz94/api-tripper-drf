# Generated by Django 2.2.3 on 2019-07-04 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_attraction', '0001_initial'),
        ('attractions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attractions',
            name='tourist_attractions',
            field=models.ManyToManyField(to='tourist_attraction.TouristAttraction'),
        ),
    ]