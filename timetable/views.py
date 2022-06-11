from django.shortcuts import render
from django.http import HttpResponse

from . import algorithm 

# Create your views here.
def juniorTable(request):
    ttDict ={
        'L2': 'CSEPY', 
        'L10': 'CSEPY', 
        'L17': 'CSEPY', 
        'L6': 'LANG1001', 
        'L13': 'LANG1001', 
        'L1': 'MECH1001', 
        'L9': 'MECH1001',
         'L15': 'CHEMP',
         'L8': 'ECEEP',
         'L5': 'CLAD1041',
         'TD12': 'MATH1041',
         'TD11': 'MATH1041',
         'G1': 'ECEETH',
         'TG11': 'ECEETH',
         'TG12': 'ECEETH',
         'TH1': 'CHEMTH',
         'H2': 'CHEMTH',
         'H3': 'CHEMTH',
         'I2': 'MATH1051',
         'I3': 'MATH1051'
    }
    return render(request, 'junior-table.html', ttDict)

def seniorTable(request):
    return render(request, 'senior-table.html', tt)