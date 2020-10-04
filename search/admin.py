from django.contrib import admin
from search.models import CveTable

# Register your models here.

class CveTableAdmin(admin.ModelAdmin):
    list_display = ('no','platform','version','platform_version','platform_type','vendor','etc','up_date','edition','language','cve_id','cwe_id','n_of_exploits','vulnerability_type','publish_year','publish_date','update_date','score','gained_access_level','access','conf','integ','avail','description')


admin.site.register(CveTable, CveTableAdmin)
