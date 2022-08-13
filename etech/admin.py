from django.contrib import admin
from .models import Category, About, Services, Portfolio, Image, Contact, Slider


class AdminCategory(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Category, AdminCategory)
admin.site.register(About)
admin.site.register(Services)
admin.site.register(Portfolio)
admin.site.register(Image)
admin.site.register(Contact)
admin.site.register(Slider)
