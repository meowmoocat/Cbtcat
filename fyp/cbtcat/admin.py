from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import CbtcatUser, L1A, L2Ans, L3Ans, L4Ans, L5Ans, L6Ans, Lvl1UserData, Lvl2UserData, Lvl4UserData, \
    Lvl6UserData, Lvl5UserData, Login, Lvl3UserData


class CbtcatUserInline(admin.StackedInline):
    model = CbtcatUser
    can_delete = False
    verbose_name_plural = 'cbtcat_users'


@admin.register(Login)
class Login(admin.ModelAdmin):
    list_display = ('username', 'date_time')


@admin.register(L1A)
class L1A(admin.ModelAdmin):
    list_display = ('finished', 'current_question', 'created_on', 'finished_on', 'username')


@admin.register(L2Ans)
class L2Ans(admin.ModelAdmin):
    list_display = ('finished', 'current_question', 'created_on', 'finished_on', 'username')


@admin.register(L3Ans)
class L3Ans(admin.ModelAdmin):
    list_display = ('finished', 'current_question', 'created_on', 'finished_on', 'username')


@admin.register(L4Ans)
class L4Ans(admin.ModelAdmin):
    list_display = ('finished', 'current_question', 'created_on', 'finished_on', 'username')


@admin.register(L5Ans)
class L5Ans(admin.ModelAdmin):
    list_display = ('finished', 'current_question', 'created_on', 'finished_on', 'username')


@admin.register(L6Ans)
class L6Ans(admin.ModelAdmin):
    list_display = ('finished', 'current_question', 'created_on', 'finished_on', 'username')


@admin.register(Lvl1UserData)
class Lvl1UserData(admin.ModelAdmin):
    list_display = ('num_unique_users_started', 'num_unique_users_started', 'num_unique_users_completed',
                    'total_times_started', 'total_times_finished')


@admin.register(Lvl2UserData)
class Lvl2UserData(admin.ModelAdmin):
    list_display = ('num_unique_users_started', 'num_unique_users_started', 'num_unique_users_completed',
                    'total_times_started', 'total_times_finished')


@admin.register(Lvl3UserData)
class Lvl3UserData(admin.ModelAdmin):
    list_display = ('num_unique_users_started', 'num_unique_users_started', 'num_unique_users_completed',
                    'total_times_started', 'total_times_finished')


@admin.register(Lvl4UserData)
class Lvl4UserData(admin.ModelAdmin):
    list_display = ('num_unique_users_started', 'num_unique_users_started', 'num_unique_users_completed',
                    'total_times_started', 'total_times_finished')


@admin.register(Lvl5UserData)
class Lvl5UserData(admin.ModelAdmin):
    list_display = ('num_unique_users_started', 'num_unique_users_started', 'num_unique_users_completed',
                    'total_times_started', 'total_times_finished')


@admin.register(Lvl6UserData)
class Lvl6UserData(admin.ModelAdmin):
    list_display = ('num_unique_users_started', 'num_unique_users_started', 'num_unique_users_completed',
                    'total_times_started', 'total_times_finished')


@admin.register(CbtcatUser)
class CbtcatUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'num_times_login', 'current_level')
    fields = ['username', 'num_times_login']


class UserAdmin(BaseUserAdmin):
    inlines = (CbtcatUserInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

