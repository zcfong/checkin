from django.db import models


class Active(models.Model):
    title = models.CharField('活动标题', max_length=30, null=False, db_index=True)

    class Meta:
        verbose_name = '活动'

    def __str__(self):
        return self.title


# Create your models here.
class ContactSeat(models.Model):
    guest = models.CharField(max_length=30, null=False, db_index=True,
                             verbose_name='嘉宾')
    # active = models.CharField('活动', max_length=64, null=False)
    seat = models.CharField('座位', max_length=64, null=False)
    is_sign = models.BooleanField('签到', default=False)
    createtime = models.DateTimeField('创建时间', editable=False,
                                      auto_now=True)
    active = models.ForeignKey(Active, related_name='active',
                               verbose_name='活动')

    class Meta:
        verbose_name = '嘉宾座位'
