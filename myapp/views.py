from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Person
# Create your views here.

def index(request):
    #return HttpResponse("<h1>Hello World</h1>") #แสดงข้อความ และใช้ภาษาHTMLได้
    #ดึงข้อมูลจาก Person มาทำงานใน views ฟังชัน index จากนั้นโยนข้อมูลไปทำงานที่ index.html
    all_person = Person.objects.all() #.all() .filter(เงื่อนไข เช่น age = 25)  
    return render(request,"index.html" , {"all_person":all_person}) 

def about(request):
    #return HttpResponse("<h1>เกี่ยวกับเรา</h1>")
    return render(request,"about.html") 

def form(request):
    #return HttpResponse("<h1>แบบฟอร์มบันทึกข้อมูล</h1>")
    if request.method == "POST":
        #รับข้อมูล
        name = request.POST["name"]
        age = request.POST["age"]
        print(name , age)
        return redirect("/") #กลับไปที่หน้าแรก /

        #บันทึกข้อมูล
    else :    
        return render(request,"form.html") 