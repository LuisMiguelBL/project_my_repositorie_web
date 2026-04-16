from django.contrib import admin

# Register your models here.

from .models import Question, Choice


    #fields = ["pub_date","question_text"]
"""
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
"""
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Content",{'fields': ["question_text"], 'classes':['collapse']}),
        ("Date Information", {'fields': ["pub_date"],'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]

    list_filter = ["pub_date"]
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)