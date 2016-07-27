from django.contrib import admin

from .models import BlogPost, Category


# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    def make_published(self, request, queryset):
        queryset.update(status='p')
        # queryset.update(aprobat=datetime.now())

    make_published.short_description = "Mark selected stories as published"

    actions = [make_published]
    list_display = ['title', 'author', 'status', 'timestamp', 'updated']
    class Meta:
        model = BlogPost

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(BlogPostAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        # if obj is not None and not request.user.is_superuser and request.user.id != obj.author.id:
        #     return False
        return True

    def queryset(self, request):
        # if request.user.is_superuser:
        #     return Afaceri.objects.all()
        return BlogPost.objects.filter(author=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

class CategoryAdmin(admin.ModelAdmin):

    class Meta:
        model = Category


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category, CategoryAdmin)