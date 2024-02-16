from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['nom',"slug",'chopetilishVaqti','holati']
    list_filter = ['nom','chopetilishVaqti','holati']
    prepopulated_fields = {"slug":('nom',)}
    search_fields = ['nom','kontent']
    date_hierarchy = 'chopetilishVaqti'
    ordering = ['holati','chopetilishVaqti']
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['nomi']
@admin.register(Email)
class emailAdmin(admin.ModelAdmin):
    list_display = ['email']
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(reklama)
class reklamaAdmin(admin.ModelAdmin):
    list_display = ['Name']
@admin.register(Magazin)
class MagazinAdmin(admin.ModelAdmin):
    list_display = ['Name']
@admin.register(Follow_us)
class Follow_us_Admin(admin.ModelAdmin):
    list_display = ['nomi']
@admin.register(Get_in_touch)
class Get_in_touch_Admin(admin.ModelAdmin):
    list_display = ['email']
@admin.register(Telfon)
class TelfonAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {"slug": ('name',)}