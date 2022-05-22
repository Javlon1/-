from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'type', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name','last_name', 'email' )}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Extra'), {'fields': ('type', 'phone')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')})
    )

admin.site.register(Info)
admin.site.register(Slider)
admin.site.register(We_Offer)
admin.site.register(Our_Areas)
admin.site.register(Review)
admin.site.register(Our_Expertise)
admin.site.register(Case_Study)
admin.site.register(Our_Team)
admin.site.register(Blog)
admin.site.register(About)
admin.site.register(About_Us_Detail)
admin.site.register(Question)
admin.site.register(Map)
admin.site.register(Chat)
admin.site.register(Window)