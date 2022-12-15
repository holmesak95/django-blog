# a new import
from django.contrib import admin
from blogging.models import Post, Category

# and a new admin registration
# admin.site.register(Post)
# admin.site.register(Category)

# https://docs.djangoproject.com/en/dev/ref/contrib/admin/#working-with-many-to-many-models


class CategoryInline(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]


class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]
    exclude = ["posts"]


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
