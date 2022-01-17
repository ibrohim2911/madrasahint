from django.contrib import admin
from .models import User
class UserAdmin(admin.ModelAdmin):
     list_display = ('id', 'name', 'surname','number','age', 'daraja', 'vaqt')
     list_editable = ('name', 'surname','number','age', 'daraja', 'vaqt')
admin.site.register(User)

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'surname','number')
#     list_editable = ('name', 'surname',.........)