# App Registry

## About

A [djangobaseproject](https://github.com/acdh-oeaw/djangobaseproject) based web application to register other web applications.

## Install

* Download or clone this repository.
* Adapt the information in `webpage/metadata.py` according to your needs.
* Create and activate a virtual environment and run `pip install -r requirements.txt`.
* Run `makemigrations`, `migrate`, and `runserver` and check [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## First steps

Make sure that the application you'd like to register has some endpoint return a JSON file like the one below

```json
{
    "title": "ACDH-OeAW App Registry",
    "author": "Firstname Lastname, Firstname Lastname",
    "subtitle": "A registry of Web Applications run by the ACDH-OeAW",
    "description": "ACDH-OeAW App Registry is a registry of Web Applications\
    developed and/or hosted by the Austrian Centre for Digital Humanities at the Austrian\
    Acadamey of Sciences.",
    "github": "https://github.com/acdh-oeaw/dar",
    "purpose_de": "Ziel von ACDH-OeAW App Registry ist die Registrierung von Web\
    Applikationen, die vom ACDH-OeAW entwickelt und/oder gehosted werden.",
    "purpose_en": "The purpose of ACDH-OeAW App Registry is the registration of web\
    apps developed and/or hosted at the ACDH-OeAW",
    "app_type": "database|website|service|tool|digital-edition"
}
```

You can now register applications by browsing to http://127.0.0.1:8000/webapps/apps/create/ and populating the field "The URL of the project's info endpoint." (the only mandatory field). On saving this endpoint will be called, the (hopefully succesfully returned) JSON parsed and the remaining fields populated. Be aware that the field "The URL of the application" will be populated automatically with the `{uri.scheme}://{uri.netloc}/` of the project info's endpoint URL.
