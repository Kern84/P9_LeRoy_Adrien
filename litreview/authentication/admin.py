from django.contrib import admin
from authentication.models import User
from publication.models import Ticket, Review, UserFollows

admin.site.register(User)
admin.site.register(Ticket)
admin.site.register(Review)
admin.site.register(UserFollows)
