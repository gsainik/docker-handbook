import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','cbvproject.settings')
import django
django.setup()

from faker import Faker
from testapp.models import Employee
from random import *


fake=Faker()
def numbergenerator():
    d= randint(6,9)
    number = str(d)
    for i in range(9):
        number = number + str(randint(0,9))
    return int(number)

def populate(n):
    for i in range(n):
        feno=randint(100,999)
        fename=fake.name()
        fesal = randint(1000,9999)
        femobile = numbergenerator()
        feadd= fake.address()
        employee_record =  Employee.objects.get_or_create(
        eno=feno,
        ename= fename,
        esal = fesal,
        emobile= femobile,
        eadd= feadd
        )


n= int(input('enter number of records to be inserted in to Database :'))
populate(n)
print(f'{n} records instered Successfully in to Database')
