from django.conf import settings


def populate_webapp(webpage_object, metadata):
    """ parses a metadata_dict and populates a webpage object with the parsed data
    :param webpage_object: An instance of the class appreg.models.WebApp
    :param metadata: A dictionary providing string for the following keys ["title",\
    "subtitle", "author", "description", "purpose_en", "gitbub", "app_type", "base_tech",\
    "framework"]
    :return: An instance of the class appreg.models.WebApp.
    """
    try:
        webpage_object.title = metadata['title']
    except KeyError:
        webpage_object.title = 'no info provided'
    try:
        webpage_object.subtitle = metadata['subtitle']
    except KeyError:
        webpage_object.subtitle = 'no info provided'
    try:
        webpage_object.author = metadata['author']
    except KeyError:
        webpage_object.author = 'no info provided'
    try:
        webpage_object.description = metadata['description']
    except KeyError:
        webpage_object.description = 'no info provided'
    try:
        webpage_object.purpose_en = metadata['purpose_en']
    except KeyError:
        webpage_object.purpose_en = 'no info provided'
    try:
        webpage_object.git_url = metadata['github']
    except KeyError:
        webpage_object.git_url = 'no info provided'
    try:
        webpage_object.app_type = metadata['app_type']
    except KeyError:
        webpage_object.app_type = 'no info provided'
    try:
        webpage_object.base_tech = metadata['base_tech']
    except KeyError:
        webpage_object.base_tech = 'no info provided'
    try:
        webpage_object.framework = metadata['framework']
    except KeyError:
        webpage_object.framework = 'no info provided'
    try:
        webpage_object.version = metadata['version']
    except KeyError:
        webpage_object.version = 'no info provided'
    try:
        webpage_object.last_commit = metadata['last_commit']
    except KeyError:
        webpage_object.last_commit = 'no info provided'
    try:
        webpage_object.title_img = metadata['title_img']
    except KeyError:
        webpage_object.title_img = settings.DEFAULT_TITLE_IMG
    try:
        webpage_object.project_logo = metadata['project_logo']
    except KeyError:
        webpage_object.project_logo = settings.DEFAULT_LOGO
    return webpage_object
