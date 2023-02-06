from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index), #เมื่อเปิด path นี้เรียกใช้ฟังชัน index ที่อยู่ในไฟล์์ views
    path('about',views.about),
    path('form',views.form)


]