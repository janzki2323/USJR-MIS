from django.db import models
from Accounts.models import Employee


class Memo_Routing(models.Model):
    Id_Number = models.ForeignKey(Employee,on_delete=models.CASCADE)
    Type_Request = models.CharField(null = False, max_length=100)
    Date_Faculty_Submitted = models.DateField(null = True)
    Date_Chairman_Approved = models.DateField(null = True)
    Date_Dean_Approved = models.DateField(null = True)
    Date_VP_Acad_Approved = models.DateField(null = True)
    Date_President_Approved = models.DateField(null = True)
    Date_PAO_Approved = models.DateField(null = True)
    Date_Accounting_Approved = models.DateField(null = True)
    Date_HR_Approved = models.DateField(null = True)

    class Meta:
        db_table = 'Memo_Routing'