from django.shortcuts import render, redirect
import json
from .models import *
import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from time import time


# Create your views here.


def home(request):
    records = Contact.objects.all()
    r = 'Please enter some data :)'
    if request.POST:
        r = 'Results: '
        data = request.POST['textarea']
        print(data)
        if is_json(data):
            data = json.loads(data)
            t1 = time()
            amount = insert_data(data)
            t2 = time()
            elapsed = t2 - t1
            r += "Records Saved: " + str(amount) + ". Time: " + str(round(elapsed, 2)) + " seconds."
        else:
            r += 'Not Correct json data'

    elif request.GET:
        phone = request.GET['search']
        records = Contact.objects.filter(phone=phone)
    context = {'report': r,
               'records': records}
    return render(request, 'home.html', context)


def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True


def phone_not_in_db(phone, source_id):
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    try:
        Contact.objects.get(phone=phone, timestamp=today, source_id=source_id)
        return False
    except ObjectDoesNotExist:
        return True

@transaction.atomic
def insert_data(data):
    amount = 0
    phones_values = []
    for i in data['items']:
        phone = str(i['phone'])
        if "+7" in phone:
            phone = phone[2:]
        source_id = data['source_id']
        if phone not in phones_values and phone_not_in_db(phone, source_id):
            c = Contact()
            c.source_id = source_id
            c.name = i['name']
            c.email = i['email']
            c.phone = phone
            c.timestamp = datetime.datetime.today().strftime('%Y-%m-%d')
            phones_values.append(phone)
            c.save()
            amount += 1
    return amount
