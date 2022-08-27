from beav.models.Attribute import Attribute
from beav.models.Value import Value
from beav.models.Group import Group
from beav.models.Entity import Entity
from django.contrib import admin


admin.site.register(Attribute)

admin.site.register(Value)

admin.site.register(Group)



class EntityAdmin(admin.ModelAdmin):

     # define the raw_id_fields
    raw_id_fields = ('product',)
    # define the related_lookup_fields
    related_lookup_fields = {
        'fk': ['product'],
    }

    autocomplete_lookup_fields = {
        'fk': ['product'],
    }

admin.site.register(Entity,EntityAdmin)
