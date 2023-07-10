from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('palakkad/',views.palakkad,name='palakkad'),
    path('thrissur/', views.thrissur, name='thrissur'),
    path('malappuram/',views.malappuram,name='malappuram'),
    path('cochin/',views.cochin,name='cochin'),
    path('kozhikode/',views.kozhikode,name='kozhikode'),
    path('bangalore/',views.bangalore,name='bangalore'),
    path('signup/', views.signin, name='signin'),

]