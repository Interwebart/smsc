from django.contrib import admin
from SMSC.models import Account, Abonent, CellNumbers, Sends

# Register your models here.
admin.site.register(Abonent)
admin.site.register(Account)
admin.site.register(CellNumbers)
admin.site.register(Sends)

