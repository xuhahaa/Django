from django.db import models


# python manage.py makemigrations
# python manage.py migrate


# Create your models here.

# class 类名称(models.Model):
#    第一列字段名称 = models.字符特征(null=False,blank=False,Max_length = 最大长度)

class budget(models.Model):
    time = models.DateTimeField(null=False, blank=False)
    name = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name


class budget_all(models.Model):
    costCategory = models.CharField(max_length=50, verbose_name='费用类别')
    budgetYear = models.PositiveSmallIntegerField(verbose_name='预算年度')
    budgetAmount = models.FloatField(verbose_name='预算金额')
    executionAmount = models.FloatField(verbose_name='执行金额')
    executionRate = models.FloatField(verbose_name='执行率')
    remarks = models.CharField(blank=True, max_length=50, verbose_name='备注')
    operating = models.CharField(blank=True, max_length=50, default='查看明细', verbose_name='操作')

    def __str__(self):
        return self.costCategory


# 应急资金
class EmergencyFund(models.Model):
    pass


# 授权采购
class AuthBuy(models.Model):
    # 数据库存储‘yes’,前端界面展示‘已完成’
    YES = 'yes'
    ING = 'ing'
    NO = 'no'
    StatusChoices = ((YES, '已完成'), (ING, '采购中'), (NO, '取消'))
    assetType = models.CharField(max_length=50, verbose_name='设备类型', default='笔记本电脑')
    status = models.CharField(max_length=50, choices=StatusChoices, default=NO, verbose_name='设备类型')

    def __str__(self):
        return self.assetType


# 总部集采
class HeadBuy(models.Model):
    pass


# 部门开支
class DepartmentExes(models.Model):
    pass


# executionRate = executionAmount + budgetAmount

# 定义一个class类，设备，属性有资产编号、序列号等等
'''class Device(models.Model):
    AssetNo = models.TextField(null=False, blank=False)  # 资产编号字段
    SN = models.TextField(null=False, blank=False)  # 序列号字段

    @property
    def __str__(self):
        return self.AssetNo'''
