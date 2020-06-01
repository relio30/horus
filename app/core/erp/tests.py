from config.wsgi import *
from core.erp.models import Type

query = Type.objects.all()
print(query)

t = Type()
t.name = 'President'
t.save()
