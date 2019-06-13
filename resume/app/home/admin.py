from django.contrib import admin
from .models import PersonalInfo, Section, Content, FooterText, Social


class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'degree', 'image', 'birthday', 'placeofbirth', 'mail', 'phone']

    class Meta:
        model = PersonalInfo


class SectionAdmin(admin.ModelAdmin):
    list_display = ['title']

    class Meta:
        model = Section


class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'section',  'startdate', 'enddate']

    class Meta:
        model = Content


class FooterTextAdmin(admin.ModelAdmin):
    list_display = ['text']

    class Meta:
        model = FooterText


class SocialAdmin(admin.ModelAdmin):
    list_display = ['title', 'username']

    class Meta:
        model = Social


admin.site.register(PersonalInfo, PersonalInfoAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(FooterText, FooterTextAdmin)
admin.site.register(Social, SocialAdmin)