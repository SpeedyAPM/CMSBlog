from django.contrib import admin
from blog.models import BlogPost
from blog.models import HomepageParagraph
# Register your models here.

#admin.site.register(Blog)

@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author", )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['author'].initial = request.user
        form.base_fields['author'].disabled = True

        if obj:
            if obj.author != request.user:
                form.base_fields['title'].disabled = True
                form.base_fields['slug'].disabled = True
                form.base_fields['content'].disabled = True
                form.base_fields['cover'].disabled = True
                form.base_fields['tags'].disabled = True
        return form

    #delete bulk (by selecting) only for superuser
    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.is_superuser:
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions

    #delete individual posts only for superuser or author
    def has_delete_permission(self, request, obj=None):
        is_superuser = request.user.is_superuser
        is_author = False
        if obj:
            is_author = (obj.author == request.user)
        return is_superuser or is_author

@admin.register(HomepageParagraph)
class HomepageParagraph(admin.ModelAdmin):
    list_display = ("sno", "title", "subtitle", "content",)