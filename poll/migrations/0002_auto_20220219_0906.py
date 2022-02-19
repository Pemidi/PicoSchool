# Generated by Django 3.2 on 2022-02-19 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='for_user',
            field=models.CharField(choices=[('all', 'همه'), ('teacher', 'دبیران'), ('parent', 'والدین'), ('student', 'دانش آموزان')], default='all', max_length=15, verbose_name='برای کاربران'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='question',
            field=models.CharField(max_length=30, verbose_name='عنوان سوال'),
        ),
        migrations.AlterField(
            model_name='polloptions',
            name='option',
            field=models.CharField(max_length=30, verbose_name='گزینه'),
        ),
    ]
