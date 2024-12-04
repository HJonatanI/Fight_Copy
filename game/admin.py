from django.contrib import admin
from .models import Usuario, Character, Item, Inventario, Battle
	
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Character)
admin.site.register(Item)
admin.site.register(Inventario)
admin.site.register(Battle)
