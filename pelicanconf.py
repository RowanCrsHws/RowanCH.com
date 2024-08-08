
from datetime import datetime
NOW = datetime.now()
AUTHOR = 'Rowan Cruse Howse'
SITENAME = 'RowanCH'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = 10
# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

THEME = "themes/rowanch"
ARTICLE_URL = "blog/{date:%Y}-{date:%m}-{date:%d}-{slug}.html"
ARTICLE_SAVE_AS = "blog/{date:%Y}-{date:%m}-{date:%d}-{slug}.html"
INDEX_SAVE_AS = "blog/index.html"
MENUITEMS = [
 ('blog', '/blog'),
 ('contact', '/contact'),
]
DIRECT_TEMPLATES = ["formSuccess", "formError", "contact", 'index', 'categories', 'authors', 'archives']
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
