from django.contrib import admin

from .models import Subscribers

@admin.register(Subscribers)
class PersonAdmin(admin.ModelAdmin):
    pass

# @admin.register(Group)
# class GroupAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Membership)
# class MembershipAdmin(admin.ModelAdmin):
#     pass