from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Grade_One, Grade_Two, Grade_Three, Grade_Four, Grade_Five, Grade_Six, Grade_Seven, Grade_Eight, New_Students

@admin.register(Grade_One)
@admin.register(Grade_Two)
@admin.register(Grade_Three)
@admin.register(Grade_Four)
@admin.register(Grade_Five)
@admin.register(Grade_Six)
@admin.register(Grade_Seven)
@admin.register(Grade_Eight)
@admin.register(New_Students)
class userdata(ImportExportModelAdmin):
    pass
