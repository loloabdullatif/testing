from django.urls import path
from api import views

urlpatterns = [
    path('members/',views.members),
    path('members/details/<int:id>', views.member1,),
    path('member/',views.member),#member not members
    #path('members/<int:id>',views.members),
]
