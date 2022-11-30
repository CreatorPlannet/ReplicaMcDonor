from django.contrib import admin
from .models import Post
from .models import Juice
from .models import drinkHot
from .models import Snack

# Register your models here.
admin.site.register(Post)
admin.site.register(Juice)
admin.site.register(drinkHot)
admin.site.register(Snack)