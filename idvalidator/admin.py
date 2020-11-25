from django.contrib import admin

from idvalidator.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'business_id')

    readonly_fields = ('name', 'email', 'business_id', 'created_at')

    # Disable object adding
    def has_add_permission(self, request, obj=None):
        return False

    class Meta:
        # Order newest to oldest
        ordering = ('-created_at',)
