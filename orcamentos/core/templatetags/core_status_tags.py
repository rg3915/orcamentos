from django import template
from django.utils.html import mark_safe

register = template.Library()


@register.tag
def status_icon(status):
    icons = {
        'c': 'fa-close status-cancelado',
        'elab': 'fa-circle status-elab',
        'p': 'fa-circle status-pendente',
        'co': 'fa-check status-concluido',
        'a': 'fa-star status-aprovado'
    }
    return mark_safe('<i> class="{}"</i>'.format(icons[status]))
