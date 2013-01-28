import re

def title_from_slug(slug):
    slug = unicode.replace(slug, '_', ' ')

    pattern = r'(?<=[a-z])(?=[A-Z])'
    slug = re.sub(pattern, ' ', slug)

    slug = unicode.replace(slug, '/', " / ")

    return slug.title()