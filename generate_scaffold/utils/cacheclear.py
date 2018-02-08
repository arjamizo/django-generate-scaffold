import os


try:
    from django.db.models.loading import AppCache
    from django.utils.datastructures import SortedDict
except:
    # http://andrewsforge.com/article/upgrading-django-to-17/part-3-django-17-new-features/#deprecated-behavior
    pass



def reload_django_appcache():
    return None
    cache = AppCache()

    cache.app_store = SortedDict()
    cache.app_models = SortedDict()
    cache.app_errors = {}
    cache.handled = {}
    cache.loaded = False

    for app in cache.get_apps():
        __import__(app.__name__)
        reload(app)


def clean_pyc_in_dir(dirpath):
    for root, _, files in os.walk(dirpath):
        for f in [f for f in files if os.path.splitext(f)[-1] == '.pyc']:
            os.remove(os.path.join(root, f))

