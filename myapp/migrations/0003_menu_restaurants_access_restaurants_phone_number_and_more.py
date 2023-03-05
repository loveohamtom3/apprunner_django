# Generated by Django 4.1 on 2022-12-22 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0002_restaurants_delete_myapp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_id', models.IntegerField(verbose_name='レストランid')),
                ('name', models.CharField(max_length=100, verbose_name='メニュー名')),
                ('price', models.IntegerField(verbose_name='値段')),
            ],
        ),
        migrations.AddField(
            model_name='restaurants',
            name='access',
            field=models.TextField(default='japan', verbose_name='交通アクセス'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurants',
            name='phone_number',
            field=models.CharField(default=1, max_length=15, verbose_name='電話番号'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='name',
            field=models.CharField(max_length=100, verbose_name='店名'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_id', models.CharField(max_length=10, verbose_name='レストランID')),
                ('restaurant_name', models.CharField(max_length=200, verbose_name='店名')),
                ('comment', models.TextField(verbose_name='レビューコメント')),
                ('score', models.PositiveSmallIntegerField(choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')], default='3', verbose_name='レビュースコア')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('restaurant_id', 'user')},
            },
        ),
    ]
