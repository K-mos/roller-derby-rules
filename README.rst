roller-derby-rules
==================

WFTDA doesn't provide any easy way to fetch the rules of Flat Track Roller Derby.
This script will parse the official current page http://wftda.com/rules/20130615 and will store the rules in a database.

Quickstart
----------

To bootstrap the project::

    virtualenv rules
    source rules/bin/activate
    cd path/to/rules/repository
    pip install -r requirements.pip
    pip install -e .
    cp rules/settings/local.py.example rules/settings/local.py
    manage.py syncdb --migrate
    python manage.py parse_wftda_rules
