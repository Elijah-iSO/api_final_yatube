from django.contrib import admin

from .models import Comment, Group, Post


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    inlines = (
        CommentInline,
    )
    list_display = ('pk', 'text', 'pub_date', 'author')
    search_fields = ('text',)
    list_filter = ('pub_date',)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'description')
    search_fields = ('slug',)
    list_filter = ('pk',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'post', 'author', 'created')
    search_fields = ('text',)
    list_filter = ('created',)


admin.site.empty_value_display = '-пусто-'
admin.site.register(Post, PostAdmin)
admin.site.register(Group)
admin.site.register(Comment)
