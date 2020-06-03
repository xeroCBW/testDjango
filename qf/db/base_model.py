from django.db import models
from django.utils import timezone


class BaseMode(models.Model):

    # 抽象类,所有类继承于这个类

    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now_add=True,verbose_name='更新时间')
    is_delete= models.BooleanField(default=False,verbose_name='是否删除')


    class Meta:
        # 表明是一个抽象类
        abstract = True

