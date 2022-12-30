import markdown
from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()

@register.filter
@stringfilter
def convert_markdown(markdown_text):
    data = markdown.markdown(markdown_text, extensions=['markdown.extensions.fenced_code', 'markdown.extensions.codehilite', 'markdown.extensions.tables', 'markdown.extensions.toc', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', 'markdown.extensions.smarty'])
    return data