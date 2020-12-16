from django.contrib.auth.models import User
from django.db import models

# Create your models here.



def image_upload (instance , filename):
    imagename , extension = filename.split(".")
    return "claims/%s/%s.%s"%(instance.id,instance.id,extension)

STATUS = (
    ('جديد','1'),
    ('تحت الاصدار','2'),
    ('مرفوضه','3'),
    ('مطلوب معلومات اضافيه','4'),
)

class Claim(models.Model):
    empno = models.CharField( max_length=12 ,verbose_name='الرقم الوظيفي')
    eiqama = models.CharField( max_length=10,verbose_name='هوية الموظف')
    piqama = models.CharField( max_length=16 ,verbose_name='رقم بطاقةالمريض')
    name = models.CharField( max_length=150 ,verbose_name='اسم المريض')
    requester = models.ForeignKey( User ,on_delete=models.CASCADE ,verbose_name='مقدمة عن طريق') # should be username here.....
    clinicname = models.CharField( max_length=150 ,verbose_name='العياده')
    ramount = models.IntegerField(verbose_name='مبلغ المطالبة')
    currency = models.CharField (max_length=25 ,verbose_name='العملة') # should be choices......
    rdate = models.DateTimeField( auto_now=False, auto_now_add=True ,verbose_name='تاريخ الطلب')
    note = models.CharField( max_length=500 ,verbose_name='ملاحظات')
    status = models.CharField( max_length=50 ,verbose_name='الحالة' , choices=STATUS ,default='جديد')
    image = models.ImageField( upload_to=image_upload, height_field=None, width_field=None, max_length=None, null = True , blank = True)

    def __str__(self):
        return str(self.id) +' - '+ self.piqama