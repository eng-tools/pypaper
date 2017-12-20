import os
import sys

from paper_tools import general_tools as gt
from paper_tools import latex_tools as lt
from paper_tools import py_tools as pyt


def new_paper(folder_path, title, initials):
    print("building new paper")
    fullname = title + "-paper"
    print(folder_path, title, initials)
    base_path = gt.build_base(folder_path, fullname)
    lt.build_base(base_path, fullname, initials, author="")
    pyt.build_base(base_path, fullname, initials, author="")
    gt.add_to_gitignore(base_path, initials)
    pass


def get_script_path():
    ffp = os.path.dirname(os.path.realpath(sys.argv[0])) + "/"
    return ffp


def console_help():
    print("Usage: python manage.py <option> <args>")
    print("Options: new-paper <name>")

if __name__ == "__main__":
    try:
        arg1 = sys.argv[1]
    except IndexError:
        console_help()
        sys.exit(1)
    folder_path = get_script_path()

    # start the program
    if arg1 == "new-paper":
        try:
            title = sys.argv[2]
        except IndexError:
            console_help()
            sys.exit(1)
        if len(sys.argv) > 4:
            # prompt user
            pass
        else:
            initials = sys.argv[3]
        new_paper(folder_path, title, initials)
    else:
        console_help()