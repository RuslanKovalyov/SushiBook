
from django.contrib import admin
from .models import Section, Page, Product, RecipeDetails

admin.site.register(Section)
# admin.site.register(Page)
admin.site.register(Product)
admin.site.register(RecipeDetails)

class RecipeDetailsInline(admin.TabularInline):      
    model = RecipeDetails
    fields = ('product', 'quantity', 'recipe_part')
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'section')
    inlines = [
        RecipeDetailsInline,
    ]