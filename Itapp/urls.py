from django.urls import path

from Itapp import views

urlpatterns = [

    path('', views.home),
    path('about/', views.abo),
    path('service/', views.ser),
    path('project/', views.pro),
    path('blog/', views.blo),
    path('team/', views.tea),
    path('testimonial/', views.tes),
    path('404/', views.four),
    path('contact/', views.con),

]
