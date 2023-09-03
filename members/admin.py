from django.contrib import admin
from members.models import Member



# Register your models here. for styling in admin dashboard

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "email","address",)
  
admin.site.register(Member, MemberAdmin)
