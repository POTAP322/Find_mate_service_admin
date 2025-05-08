from django.contrib import admin
from .models import Game, User, PartnerRequest, UserGame, UserLog

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'telegram_id', 'username', 'account_status', 'current_partner_requests')
    list_filter = ('account_status',)
    search_fields = ('username', 'telegram_id')

@admin.register(PartnerRequest)
class PartnerRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'game', 'required_players', 'platform', 'created_at')
    list_filter = ('platform', 'created_at')
    search_fields = ('user__username', 'game__name')

@admin.register(UserGame)
class UserGameAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'game')
    search_fields = ('user__username', 'game__name')

@admin.register(UserLog)
class UserLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'log_type', 'created_at')
    list_filter = ('log_type', 'created_at')
    search_fields = ('user__username', 'log_text')
