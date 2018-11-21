from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *

@admin.register(pred_one)
class predAdmin(ImportExportModelAdmin):
    pass

@admin.register(prod_area)
class prodAdmin(ImportExportModelAdmin):
    pass

@admin.register(one)
class oneAdmin(ImportExportModelAdmin):
    pass

@admin.register(two)
class twoAdmin(ImportExportModelAdmin):
    pass

@admin.register(three)
class threeAdmin(ImportExportModelAdmin):
    pass

@admin.register(pred_three)
class predthreeAdmin(ImportExportModelAdmin):
    pass

