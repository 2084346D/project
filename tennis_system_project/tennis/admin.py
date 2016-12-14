from django.contrib import admin
from tennis.models import UserProfile, Player, Camp, Day, Session, Attendance

admin.site.register(UserProfile)
admin.site.register(Player)
admin.site.register(Camp)
admin.site.register(Day)
admin.site.register(Session)
admin.site.register(Attendance)

