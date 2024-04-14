from django.http import JsonResponse
from django.shortcuts import render

data = [
    {"Equipment": "PAC-L01-01", "Status": 1, "Fault": 0},
    {"Equipment": "PAC-L01-02", "Status": 1, "Fault": 0},
    {"Equipment": "PAC-L01-03", "Status": 1, "Fault": 0},
    {"Equipment": "PAC-L01-04", "Status": 1, "Fault": 0},
    {"Equipment": "PAC-L01-05", "Status": 0, "Fault": 0},
    {"Equipment": "PAC-L01-06", "Status": 1, "Fault": 0},
    {"Equipment": "PAC-L01-07", "Status": 0, "Fault": 1},
]


def mechanical(request, equipment):
    result = [item for item in data if item["Equipment"] == equipment]

    if result:
        return JsonResponse(result[0])
    else:
        return JsonResponse({"error": "Equipment not found"}, status=404)


def all_equipment(request):
    return JsonResponse(data, safe=False)


def dashboard_view(request):
    return render(request, 'dashboard.html')

def chart_view(request):
    return render(request, 'chart.html')