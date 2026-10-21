import pandas as pd
from django.http import request
from django.shortcuts import render
from .dashboard import frequency_table

# Create your views here.

def dashboard_view(request):
    queryset = pd.read_csv("dummy_data/vehicles_data_1000.csv")
    df = pd.DataFrame(queryset)

    return render(request, 'vehicles/index.html', {
        "frequency_table": frequency_table(df)
    })

