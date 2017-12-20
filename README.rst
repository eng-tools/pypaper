.. image:: https://travis-ci.org/eng-tools/paper_tools.svg?branch=master
   :target: https://travis-ci.org/eng-tools/paper_tools
   :alt: Testing Status

.. image:: https://img.shields.io/pypi/v/paper_tools.svg
   :target: https://pypi.python.org/pypi/paper_tools
   :alt: PyPi version

.. image:: https://coveralls.io/repos/github/eng-tools/paper_tools/badge.svg
   :target: https://coveralls.io/github/eng-tools/paper_tools

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://github.com/eng-tools/paper_tools/blob/master/LICENSE
    :alt: License


###########
paper_tools
###########

A Python package to speed up the writing of papers by automating various aspects of research writing

----------
How to use
----------

Copy the manage.py file into the directory above where you will write the paper

No existing folder for paper
############################

If the base folder for your paper doesn't exist

run:
`python manage.py new-paper <paper name>`

Follow the prompts.

Existing folder for paper 
#########################

run:
`python manage.py new-paper <folder name>`
