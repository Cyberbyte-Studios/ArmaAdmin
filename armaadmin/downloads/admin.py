from django.contrib import admin

from armaadmin.downloads.models import File, FileSync, Branch


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'description', 'groups')

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'filename', 'size')


@admin.register(FileSync)
class FileAdmin(admin.ModelAdmin):
    actions = None
    list_display = (
        'id', 'user', 'created', 'updated', 'deleted', 'total', 'previous_total', 'size', 'started', 'finished')
    readonly_fields = (
        'id', 'user', 'created', 'updated', 'deleted', 'total', 'previous_total', 'size', 'started', 'finished')

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
