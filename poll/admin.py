from django.contrib import admin
from poll.models import Poll, Item, Queue, Vote, Choice
from django.utils.translation import ugettext_lazy as _


class PollItemInline(admin.TabularInline):
    model = Item
    extra = 5
    max_num = 10
    fields = ('userbox', 'value', 'index', 'vote_count',)
    readonly_fields = ('vote_count',)


class PollAdmin(admin.ModelAdmin):
    list_display = ('title', 'startdate', 'polltype', 'vote_count',
                    'publish')
    inlines = [
        PollItemInline,
    ]

    fieldsets = (
                 (None, {'fields': ('title',)}),
                 (_('Options'), {'fields': ('publish', 'polltype',
                                            'startdate',)}),
                 )


class VoteChoiceItemInline(admin.TabularInline):
    model = Choice
    extra = 5
    max_num = 10
    readonly_fields = ('item', 'uservalue')


class VoteAdmin(admin.ModelAdmin):
    list_display = ('poll', 'ip', 'user', 'datetime')
    list_filter = ('poll', 'datetime')
    inlines = [
        VoteChoiceItemInline,
    ]

admin.site.register(Poll, PollAdmin)
#admin.site.register(Queue, admin.ModelAdmin)
admin.site.register(Vote, VoteAdmin)
