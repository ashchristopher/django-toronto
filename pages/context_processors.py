from django.conf import settings


def page_settings(request):
    context = {
        'GA_TRACKING_CODE': settings.GA_TRACKING_CODE,
    }

    return context
