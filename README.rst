roller-derby-rules
==================

Django app that parses the WFTDA website to fetch the rules of Flat Track Roller Derby and stores them in database with reusable django models.

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

Documentation
-------------

Developer documentation is available in Sphinx format in the docs directory.

Initial installation instructions (including how to build the documentation as
HTML) can be found in docs/install.rst.
