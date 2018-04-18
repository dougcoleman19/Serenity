from django.contrib import admin

from .models import Gender, Ethnicity, Demographics, Type, AbuseType, Status, County


class GenderAdmin(admin.ModelAdmin):
    fields = [ 'gender_description', ]


class EthnicityAdmin(admin.ModelAdmin):
    fields = [ 'ethnicity_description', ]


class DemographicsAdmin(admin.ModelAdmin):
    fields = [ 'demographics_description', ]


class TypeAdmin(admin.ModelAdmin):
    fields = [ 'type_description', ]


class AbuseTypeAdmin(admin.ModelAdmin):
    fields = [ 'abusetype_description', ]


class StatusAdmin(admin.ModelAdmin):
    fields = [ 'status_description', ]


class CountyAdmin(admin.ModelAdmin):
    list_display = ('county_name', 'avenues_support')
    fields = [ 'county_name', 'avenues_support',  ]


admin.site.register(Gender, GenderAdmin)
admin.site.register(Ethnicity, EthnicityAdmin)
admin.site.register(Demographics, DemographicsAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(AbuseType, AbuseTypeAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(County, CountyAdmin)