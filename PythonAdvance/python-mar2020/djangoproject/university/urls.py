from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:university_id>/', views.university_details, name='university_details'),
<<<<<<< Updated upstream
    path('student/<int:student_id>/', views.student_details, name='student_details'),
=======
    path('student/<int:student_id>/', views.student_details, name='student_details')
>>>>>>> Stashed changes
]
