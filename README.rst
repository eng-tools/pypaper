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


How to use
----------

Copy the manage.py file into the directory above where you will write the paper

Generate a paper or chapter project
###################################

From the directory where you want the project folder to be created (or already exists)

For new paper run:
    .. code:: bash
    $python manage.py paper <paper name> <optional: initials>

For new chapter run:
    .. code:: bash
    python manage.py chapter <paper name> <optional: initials>

Follow the prompts.


Generate a small bib-tex file
#############################

run:
`short-bib <latex file path> <large bibtex path> <optional: new bibtex path>`



Project folders and files
-------------------------

 - root_dir/
    - manage.py: This is provides the command-line tools for generate new figures, tables, bibtex files
    - settings.py: This contains you research project settings (e.g. publication file type)
        - *Note: all parameters should by written in UPPER_CASE_WITH_UNDERSCORES*
    - all_paths.py: This contains you paths to different folders that are specific to the project
    - user_paths.py: This contains paths that are specific to the user's computer
    - sr_data/: This folder contains data specific to the project
        - Note:

TODO: Explain each folder and file


Tutorial: A new research paper
------------------------------

Definitions list:

papers_dir:
    The folder that contains your research papers.
short_research_name:
    This should be a two word name describing your research using hyphens "-" instead of spaces " ".
initials:
    This should be the initials of the research name (usually two characters).
project_root_folder_name:
    The name of the root folder of your new research paper "<short_research_name>-paper"
main_bibtex_file: The bibtex file that contains all of your references.

Steps:

1. Install pypaper
    .. code:: bash

    $ pip install pypaper

2. Create a new repository called "<project_root_folder_name>" on Bitbucket or Github with a README file.

3. Clone the folder to your papers directory
    .. code:: bash

    $ cd <papers_dir>
    $ git clone <clone-url>

4. Add the pypaper manager.py file to your project
    .. code:: bash

    $ python -m pypaper.init_project

5. Change the current directory to <project_root_folder_name>.
    .. code:: bash
    $ cd <project_root_folder_name>

6. Create the project folders
    .. code:: bash
    $ python manage.py paper <initials>

7. Add new folders to git repository
    .. code:: bash

    $ git add .
    $ git commit -m "Added pypaper project files"
    $ git push

8. Create a new figure, copy the 'figure_template.py' # TODO: add clt

7. Only save .svg files, non-binary files

## deploy a sample project to github for the blog



copy the templates and create a figure or run `python new figure <name>`

copy a table template file and create a table

add to generate all

add to requirements.txt file

create a pyenv and run pip install -r requirements.txt

the pip freeze
then copy contents back into requirements.txt with the exact version numbers.

Commit and push the project.