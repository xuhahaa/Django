# Generated by Django 2.1.7 on 2021-02-03 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0005_auto_20210203_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget_all',
            name='budgetAmount',
            field=models.FloatField(verbose_name='预算金额'),
        ),
        migrations.AlterField(
            model_name='budget_all',
            name='budgetYear',
            field=models.PositiveSmallIntegerField(verbose_name='预算年度'),
        ),
        migrations.AlterField(
            model_name='budget_all',
            name='costCategory',
            field=models.CharField(max_length=50, verbose_name='费用类别'),
        ),
        migrations.AlterField(
            model_name='budget_all',
            name='executionAmount',
            field=models.FloatField(verbose_name='执行金额'),
        ),
        migrations.AlterField(
            model_name='budget_all',
            name='executionRate',
            field=models.FloatField(verbose_name='执行率'),
        ),
        migrations.AlterField(
            model_name='budget_all',
            name='operating',
            field=models.CharField(blank=True, default='查看明细', max_length=50, verbose_name='操作'),
        ),
        migrations.AlterField(
            model_name='budget_all',
            name='remarks',
            field=models.CharField(blank=True, max_length=50, verbose_name='备注'),
        ),
    ]