from django.contrib import admin
from carpoolhost.models import Member,RegMember,Host,Client

admin.site.register(Member)
admin.site.register(RegMember)
admin.site.register(Host)
admin.site.register(Client)

# Register your models here.
