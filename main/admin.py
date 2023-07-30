from django.contrib import admin
from .models import News, Job, SushiRoll, Freelancer, Chef, Partner

admin.site.site_header = "God 'mode"

admin.site.register(News)
admin.site.register(Job)
admin.site.register(SushiRoll)
admin.site.register(Freelancer)
admin.site.register(Chef)
admin.site.register(Partner)