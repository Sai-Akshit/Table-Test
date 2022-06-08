from django.shortcuts import render
from django.http import HttpResponse

from . import algorithm 

# Create your views here.
def juniorTable(request):
    # ttDict = algorithm.main(1)
    ttDict = {'L4': 'CSEPY', 'L5': 'CSEPY', 'L12': 'CSEPY', 'L8': 'LANG1001', 'L15': 'LANG1001', 'L11': 'MECH1001', 'L16': 'MECH1001', 'L7': 'CHEMP', 'L18': 'ECEEP', 'L14': 'CLAD1041', 'D1': 'ECEETH', 'D2': 'ECEETH', 'D3': 'ECEETH', 'G1': 'CHEMTH', 'G2': 'CHEMTH', 'G3': 'CHEMTH'}
    return render(request, 'junior-table.html', ttDict)

def seniorTable(request):
    return render(request, 'senior-table.html', tt)