import sys
import os

# from pypaper import MIMUMUM_VERSION
import pypaper
from pypaper import general_tools as gt
from pypaper import latex_tools as lt
from pypaper import py_tools as pyt

__project_pypaper_version__ = "0.2.6"  # version that project was built with
PROJECT_ROOT_FULL_PATH = os.path.dirname(os.path.abspath(__file__)) + "/"
PROJECT_NAME = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

import sys
from distutils.version import StrictVersion

if StrictVersion(__project_pypaper_version__) < StrictVersion(pypaper.MINIMUM_VERSION):
    raise ValueError("project built with incompatible pypaper version: %s; "
                     "required version: %s; "
                     "Or install an older version of pypaper." % (__project_pypaper_version__,
                                                                  pypaper.MINIMUM_VERSION))


def new_research_project(initials):
    print("building research project")
    root_folder_full_path = PROJECT_ROOT_FULL_PATH
    project_name = PROJECT_NAME

    print(folder_path, initials)
    gt.build_base_folders(root_folder_full_path, initials)
    lt.build_base_folders(root_folder_full_path, project_name, initials, author="")
    pyt.build_base_folders(root_folder_full_path, initials)
    gt.add_to_gitignore(root_folder_full_path, initials)
    gt.add_to_requirements_txt(root_folder_full_path)
    pass


def get_script_path():
    ffp = os.path.dirname(os.path.realpath(sys.argv[0])) + "/"
    return ffp


def build_new_bibtex(latex_ffp, big_bibtex_ffp, new_bibtex_ffp='new_bibtex.bib'):
    citations = lt.extract_citation_keys_from_latex(latex_ffp=latex_ffp)
    print(citations)
    bstr = lt.compile_bibtex(citations, big_bibtex_ffp)
    with open(new_bibtex_ffp, 'w') as bibfile:
        bibfile.write(bstr)


def console_help():
    print("Usage: python manage.py <option> <args>")
    print("Options: init <optional: initials>")
    print("         init <optional: initials>")
    print("         short-bib <latex file path> <large bibtex path> <optional: new bibtex path>")


if __name__ == "__main__":
    try:
        arg1 = sys.argv[1]
    except IndexError:
        console_help()
        sys.exit(1)
    folder_path = get_script_path()

    # start the program
    if arg1 in ["init"]:
        if len(sys.argv) < 3:
            # prompt user
            initials = "ni"
            pass
        else:
            initials = sys.argv[2]
        new_research_project(initials)
    elif arg1 == "short-bib":
        try:
            latex_ffp = sys.argv[2]
            big_bibtex_ffp = sys.argv[3]
        except IndexError:
            console_help()
            sys.exit(1)
        if len(sys.argv) < 5:
            new_bibtex_ffp = 'new_bibtex.bib'
        else:
            new_bibtex_ffp = sys.argv[4]
        build_new_bibtex(latex_ffp, big_bibtex_ffp, new_bibtex_ffp)

    else:
        console_help()