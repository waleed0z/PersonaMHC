from django.shortcuts import render


def my_static_page(request):
    return render(request, 'myStat/orpheus.html')