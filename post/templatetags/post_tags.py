from django import template
from django.db.models import Q
from django.utils.timezone import now
from post.models import Post

register = template.Library()

@register.inclusion_tag('post/most_view_posts.html')
def render_most_view_posts():
    context = {
        'm_posts':Post.objects.filter( Q(active=True) & Q(published_at__lte=now()) ).order_by('-views_count')[0:5],
    }
    return context
    