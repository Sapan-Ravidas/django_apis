from django.shortcuts import render
from django.http import JsonResponse

# we want to return only the data which is json payload
def test_view(request):
    data = {
        'name' : 'sapan',
        'age' : 23,    
    }
    
    # if you want send other data like list, then you just pass other argument 
    ## safe = False
    ## return JsonResponse(safe=False)
    return JsonResponse(data)