from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    return HttpResponse("주문 관련 화면입니다.")
