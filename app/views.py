from django.shortcuts import render
from django.http import HttpResponse
from app.models import BusinessEmployeMentData
import csv
from csvproject.settings import CSV_DIR

def data_insert(request):
    with open(CSV_DIR, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            bo = BusinessEmployeMentData(
                Series_reference=row[0],
                Period=row[1],
                Data_value=row[2],
                Suppressed=row[3],
                STATUS=row[4],
                UNITS=row[5],
                Magnitude=row[6],
                Subject=row[7],
                Group=row[8],
                Series_title_1=row[9]
            )
            bo.save()
    return HttpResponse('Data inserted Successfully')
