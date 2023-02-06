from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    #return HttpResponse("<h1>Hello World</h1>") #แสดงข้อความ และใช้ภาษาHTMLได้
    name = "Namcha"
    age = 8
    return render(request,"index.html",{"fname":name,"age":age}) #แสดงผลหน้าเว็บเพจที่อยู่ในไฟล์ index.html และในหน้านี้มีข้อมูล name age

def about(request):
    #return HttpResponse("<h1>เกี่ยวกับเรา</h1>")
    return render(request,"about.html") 

def form(request):
    #return HttpResponse("<h1>แบบฟอร์มบันทึกข้อมูล</h1>")
    return render(request,"form.html") 