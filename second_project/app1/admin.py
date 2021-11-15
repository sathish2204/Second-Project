from django.contrib import admin

from .models import australia, employe, india, team1_batting, team1_bowling, team2_batting, team2_bowling


admin.site.register(employe)
admin.site.register(india)
admin.site.register(australia)
admin.site.register(team1_batting)
admin.site.register(team2_batting)
admin.site.register(team1_bowling)
admin.site.register(team2_bowling)
