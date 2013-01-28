import re

def title_from_slug(slug):
    slug = str.replace(slug, '_', ' ')

    pattern = r'(?<=[a-z])(?=[A-Z])'
    slug = re.sub(pattern, ' ', slug)

    slug = str.replace(slug, '/', " / ")

    return slug.title()