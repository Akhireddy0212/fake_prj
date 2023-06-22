from django.http import HttpResponse
from django.shortcuts import render
from faker import Faker
from.models import Student
# Create your views here.
fake=Faker()
def fake_data(request):
    for i in range(10):
        name=fake.name()
        address=fake.address()
        roll=fake.random.randint(1,10)
        marks=fake.random.randint(80,100)
        avg=fake.random.uniform(80,100)
        z=Student (name=name,address=address,roll=roll,marks=marks,avg=avg)
        z.save()
    return HttpResponse("data added")
