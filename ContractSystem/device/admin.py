from django.contrib import admin

# Register your models here.
from device import models

admin.site.register(models.budget)
admin.site.register(models.budget_all)
admin.site.register(models.EmergencyFund)
admin.site.register(models.AuthBuy)
admin.site.register(models.HeadBuy)
admin.site.register(models.DepartmentExes)
# admin.site.register(models.Device)

# 修改后台项目名称
admin.site.site_header = "预算管理系统后台管理"
