from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShot)
admin.site.register(Rating)
admin.site.register(Review)