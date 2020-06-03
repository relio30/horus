from config.wsgi import *
from core.erp.models import Category

q = Category.objects.all()
print(q)