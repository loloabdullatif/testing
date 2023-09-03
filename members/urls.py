from django.urls import path
from members import views


#Routing
urlpatterns = [
     path("", views.index, name="index"),
     path('members/', views.members),
     path('members/details/<int:id>', views.details, name='details'),
     path('add_member/', views.add_member, name='add_member'),

]
