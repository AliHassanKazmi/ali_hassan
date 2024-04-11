from django.http import JsonResponse
from django.shortcuts import render

# Example data
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
    # Filter data based on equipment
    result = [item for item in data if item["Equipment"] == equipment]

    # Check if result is found
    if result:
        # Return the first matching item as JSON response
        return JsonResponse(result[0])
    else:
        return JsonResponse({"error": "Equipment not found"}, status=404)


def all_equipment(request):
    # Return all equipment data as JSON response
    return JsonResponse(data, safe=False)


def dashboard_view(request):
    return render(request, 'dashboard.html')
