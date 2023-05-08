from django.contrib import admin

from .models import Game
from  .models import GamePlatform
from .models import PriceList
from .models import Payment



admin.autodiscover()

admin.site.register(GamePlatform)
admin.site.register(Game)
admin.site.register(PriceList)
admin.site.register(Payment)
