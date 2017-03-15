from django.contrib import admin
from tennis.models import UserProfile, Player, Event, Day, Session, Attendance

admin.site.register(UserProfile)
admin.site.register(Player)
admin.site.register(Event)
admin.site.register(Day)
admin.site.register(Session)
admin.site.register(Attendance)

