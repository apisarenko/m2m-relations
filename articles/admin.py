from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tags, Section


class TagsInlineFormset(BaseInlineFormSet):

    def clean(self):
        number_of_main_section = 0
        for form in self.forms:
            print(form.cleaned_data)
            if form.cleaned_data.get('main') == True:
                number_of_main_section += 1
        if number_of_main_section > 1:
            raise ValidationError('Основным может быть только один раздел')
        elif number_of_main_section == 0:
            raise ValidationError('Укажите основной раздел')
        return super().clean()


class TagsInline(admin.TabularInline):
    model = Tags
    formset = TagsInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagsInline]


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass
