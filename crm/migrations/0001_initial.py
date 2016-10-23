# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 16:31
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('second_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Телефонный номер должен быть в формате: '+999999999. До 15 цифр.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Телефон')),
                ('mobile_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Телефонный номер должен быть в формате: '+999999999. До 15 цифр.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Мобильный телефон')),
                ('avatar', models.ImageField(blank=True, upload_to='crm/', verbose_name='Фотография')),
                ('company', models.CharField(blank=True, max_length=50, verbose_name='Компания')),
                ('position', models.CharField(blank=True, max_length=50, verbose_name='Должность')),
                ('email_address', models.EmailField(blank=True, max_length=80, verbose_name='Эл.почта')),
                ('brith_data', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('status', models.CharField(choices=[('C', 'Делал покупку'), ('V', 'VIP'), ('I', 'Интересовался покупкой'), ('N', 'Негативно настроен'), ('O', 'Что-то еще')], max_length=1, verbose_name='Статус')),
                ('comment', models.TextField(blank=True, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name_plural': 'Всего клиентов',
                'verbose_name': 'Клиент',
            },
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Цена всего')),
                ('ident', models.IntegerField(verbose_name='Номер контракта')),
                ('description', models.TextField(verbose_name='Описание')),
                ('status', models.CharField(choices=[('E', 'Первый контакт'), ('D', 'Принятие решения'), ('H', 'Согласование контракта'), ('S', 'Контракт подписан'), ('P', 'Ожидание денег'), ('O', 'Контракт выполнен'), ('A', 'Мертвый контракт')], max_length=1, verbose_name='Статус')),
                ('deal_data', models.DateField(verbose_name='Дата')),
                ('deal_time', models.TimeField(blank=True, verbose_name='Время')),
                ('customer', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Customer', verbose_name='Клиент')),
            ],
            options={
                'verbose_name_plural': 'Всего сделок',
                'verbose_name': 'Сделка',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.IntegerField(verbose_name='Номер товара ( SKU )')),
                ('description', models.TextField()),
                ('price', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Всего продуктов',
                'verbose_name': 'Продукт',
            },
        ),
        migrations.CreateModel(
            name='SalesPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('second_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Телефонный номер должен быть в формате: '+999999999. До 15 цифр.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Телефон')),
                ('mobile_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Телефонный номер должен быть в формате: '+999999999. До 15 цифр.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Мобильный телефон')),
                ('avatar', models.ImageField(blank=True, upload_to='crm/', verbose_name='Фотография')),
                ('division', models.CharField(blank=True, max_length=50, verbose_name='Подразделение')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Логин')),
            ],
            options={
                'verbose_name_plural': 'Всего менеджеров по продажам',
                'verbose_name': 'Менеджер по продажам',
            },
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('E', 'Электронная почта'), ('P', 'Телефонный звонок'), ('L', 'Личная встреча'), ('S', 'Почта бумажная'), ('O', 'Что-то еще')], max_length=1, verbose_name='Действие')),
                ('action_description', models.TextField(verbose_name='Комментарий')),
                ('data_time', models.DateTimeField(verbose_name='Дата и время')),
                ('sales_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.SalesPerson', verbose_name='Менеджер')),
            ],
            options={
                'verbose_name_plural': 'Всего дел',
                'verbose_name': 'Список дел',
            },
        ),
        migrations.AddField(
            model_name='deal',
            name='products',
            field=models.ManyToManyField(to='crm.Product', verbose_name='Список продуктов'),
        ),
        migrations.AddField(
            model_name='deal',
            name='sales_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.SalesPerson', verbose_name='Менеджер'),
        ),
        migrations.AddField(
            model_name='customer',
            name='sales_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.SalesPerson', verbose_name='Менеджер'),
        ),
    ]
