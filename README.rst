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

    $ python manage.py paper <paper name> <optional: initials>

For new chapter run:
.. code:: bash

    $ python manage.py chapter <paper name> <optional: initials>

Follow the prompts.


Generate a small bib-tex file
#############################

run:
.. code:: bash

    $ short-bib <latex file path> <large bibtex path> <optional: new bibtex path>



Project folders and files
-------------------------

 - root_dir/
    - manage.py: This is provides the command-line tools for generate new figures, tables, bibtex files
    - settings.py: This contains you research project settings (e.g. publication file type)
        - *Note: all parameters should by written in UPPER_CASE_WITH_UNDERSCORES*
    - all_paths.py: This contains you paths to different folders that are specific to the project
    - user_paths.py: This contains paths that are specific to the user's computer
    - requirements.txt: A list of python packages used in the research
    - .gitignore: A list of files and folders that should not be tracked by git
    - data/: This folder contains data specific to the project
        - Note: Only include small non-binary files here that can be easily tracked with git,
        for large data files use another storage (e.g. Google Drive/Dropbox/OneDrive) and link the folder using
        ``user_paths.py``
    - <initials>_scripts/: This folder contains all the python files used for research, and generating outputs
        - outputs/:
            - figure_<name-of-figure>.py: This file is used to build a figure for your research paper
            - table_<name-of-figure>.py: This file is used to build a table for your research paper
        - tools/: This folder contains scripts and functions that are specific to your project but used in many files
        - research/: This folder contains scripts that used to generate data for your research
    - <initials>_paper/: This folder contains the research paper as a latex document
        - <initials>-paper.tex/: The main latex document
        - <initials>-figures/: Figures that are data generated, the ``PUBLICATION_FIGURE_PATH`` in ``all_paths.py``
        - <initials>-images/: Non-data generated files, e.g. drawings


Tutorial: A new research paper
------------------------------

Definitions list:
#################

papers_dir:
    The folder that contains your research papers.
short_research_name:
    This should be a two word name describing your research using hyphens "-" instead of spaces " ".
initials:
    This should be the initials of the research name (usually two characters).
project_root_folder_name:
    The name of the root folder of your new research paper "<short_research_name>-paper"
main_bibtex_file:
    The bibtex file that contains all of your references.

Setup Steps:
############

1. Install pypaper
.. code:: bash

    $ pip install pypaper

2. Create a new repository called ``<project_root_folder_name>`` on Bitbucket or Github with a README file.

3. Clone the folder to your papers directory
.. code:: bash

    $ cd <papers_dir>
    $ git clone <clone-url>

4. Change the current directory to ``<project_root_folder_name>``.
.. code:: bash

    $ cd <project_root_folder_name>

5. Add the pypaper manager.py file to your project
.. code:: bash

    $ python -m pypaper.init_project

6. Create the project folders
.. code:: bash

    $ python manage.py init <initials>

7. Add new folders to git repository
.. code:: bash

    $ git add .
    $ git commit -m "Added pypaper project files"
    $ git push


Steps to create a new figure
############################

8. Copy the ``figure_template.py`` and rename it the name of your new figure with the prefix "figure_"
 e.g. "figure_beam_deflections_under_load.py" # TODO: add clt

9. Replace the code for plotting a figure ``subplot.plot([0], [0], label="", c=cbox(0))``. Note that ``cbox`` is a line
colour iterator, where you specific an integer and it returns a colour. Useful for plotting two lines in the same colour.
You can learn more about it here: https://github.com/eng-tools/bwplot

10. Update the publication settings ``PUBLICATION_FILE_TYPE`` and ``PUBLICATION_DPI``, which correspond to the image
type and the dots-per-inch as specified by the conference/journal/book.

11. When run the new figure script you will generate a new figure in the images folder call the same as the figure
script name, e.g. "beam_deflections_under_load.eps".

12. Add to the script to generate_all.py

Steps to create a new table
###########################

1. copy a table template file

2. Load the object with the parameters

3. Pass to XXXXX


Steps to save the work state for sharing and re-running
=======================================================

1. Generate a new python virtual environment and activate it

.. code:: bash
    brew install pyenv
    pyenv install 3.6.4
    pyenv virtualenv 3.6.4 <virtual-env-name>
    pyenv activate <virtual-env-name>

2. Install dependencies ``pip install -r requirements.txt``

3. Check that you can re-build all of your research, run ``python generate_all.py``, otherwise continue to add to
requirements.txt, until you have all the required packages.

3. View the versions of the dependencies ``pip freeze``

4. Copy the output back into requirements.txt with the exact version numbers.

5. Commit and push the project.


