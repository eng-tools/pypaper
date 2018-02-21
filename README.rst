.. image:: https://travis-ci.org/eng-tools/pypaper.svg?branch=master
   :target: https://travis-ci.org/eng-tools/pypaper
   :alt: Testing Status

.. image:: https://img.shields.io/pypi/v/pypaper.svg
   :target: https://pypi.python.org/pypi/pypaper
   :alt: PyPi version

.. image:: https://coveralls.io/repos/github/eng-tools/pypaper/badge.svg
   :target: https://coveralls.io/github/eng-tools/pypaper

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://github.com/eng-tools/pypaper/blob/master/LICENSE
    :alt: License


#######
pypaper
#######

A Python package to speed up the writing of papers by automating various aspects of research writing

----------
How to use
----------

Copy the manage.py file into the directory above where you will write the paper

Generate a paper or chapter project
###################################

From the directory where you want the project folder to be created (or already exists)

For new paper run:
`python manage.py paper <paper name> <optional: initials>`

For new chapter run:
`python manage.py chapter <paper name> <optional: initials>`

Follow the prompts.


Generate a small bib-tex file
#############################

run:
`short-bib <latex file path> <large bibtex path> <optional: new bibtex path>`