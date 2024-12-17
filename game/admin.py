from django.contrib import admin
from .models import Usuario, Character, Item, Inventario, Battle, Mision, MisionActiva
	
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Character)
admin.site.register(Item)
admin.site.register(Inventario)
admin.site.register(Battle)
admin.site.register(Mision)
admin.site.register(MisionActiva)