from django.contrib import admin
from .models import Message

# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    list_display = ('from_user','to_user','text','created')
    list_filter = ('from_user','to_user')
    date_hierarchy='created'
admin.site.register(Message, MessageAdmin)
