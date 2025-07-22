from django.shortcuts import render


def my_static_page(request):
    return render(request, 'myStat/orpheus.html')

def get_educated(request):
    return render(request, 'myStat/mentinfo.html')