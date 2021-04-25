from django.contrib import admin

from .models import Developers, Tasks


class DevelopersInline(admin.TabularInline):
    model = Tasks.developers.through

class DevelopersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level', 'rating', 'age')
    list_filter = ('level',)

    search_fields = ('name', 'age', 'level')  
    inlines = [
        DevelopersInline,
    ]   
 
class TasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'complexity', 'startDate')
    list_editable = ('complexity',)
    list_filter = ('complexity',)
    search_fields = ('title', 'complexity')  
    inlines = [
        DevelopersInline,
    ]

    exclude = ('developers',)



admin.site.register(Developers, DevelopersAdmin)
admin.site.register(Tasks, TasksAdmin)