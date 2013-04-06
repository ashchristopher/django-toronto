from django import template


register = template.Library()


@register.inclusion_tag('presentations/_tag_display_presentation.html', takes_context=True)
def display_presentation(context, presentation):
    return {
        'presentation': presentation,
        'static_url': context['STATIC_URL']
    }
