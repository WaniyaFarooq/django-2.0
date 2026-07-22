from django.utils.text import slugify
from .models import Receipe
import uuid
def generate_slug(title: str) -> str:
    slug = slugify(title)
    original_slug = slug

    counter = 1

    while Receipe.objects.filter(slug=slug).exists():
        slug = f"{original_slug}-{counter}"
        counter += 1

    return slug