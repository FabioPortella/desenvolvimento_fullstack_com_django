from django.contrib import admin
from polls.models import Choice, Question


class CustonAdminSite(admin.AdminSite):
    site_header = "Curso de Pyton Admin"


admin_site = CustonAdminSite()
admin_site.register(Choice)
admin_site.register(Question)
