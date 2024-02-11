# Generated by Django 3.2.23 on 2024-02-11 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientManager', '0004_contract_contractdate'),
        ('hr', '0001_initial'),
        ('track', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectRequest',
            fields=[
                ('timestampmixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='track.timestampmixin')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='تحصيل شهر ')),
                ('daftr_serial', models.CharField(blank=True, max_length=14, null=True, verbose_name='سريال دفتر التحصيل')),
                ('clientt', models.ManyToManyField(to='clientManager.Client')),
                ('collector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.employee', verbose_name='المحصل')),
            ],
            bases=('track.timestampmixin', models.Model),
        ),
    ]