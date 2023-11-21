from django.contrib import admin
from .models import BlogNews
from ckeditor.widgets import CKEditorWidget
from django import forms


class BlogNewsAdminForm(forms.ModelForm):
    class Meta:
        model = BlogNews
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(),
            'description_small': CKEditorWidget(),
        }


@admin.register(BlogNews)
class BlogNewsAdmin(admin.ModelAdmin):
    form = BlogNewsAdminForm
    list_display = ('title', 'description_small', 'location', 'photo', 'pub_date', 'author', 'comment_author')

    def author(self, obj):
        return obj.author.username if obj.author else '-'

    author.short_description = 'Author'

    def comment_author(self, obj):
        return obj.comment_author.username if obj.comment_author else '-'

    comment_author.short_description = 'Comment Author'
