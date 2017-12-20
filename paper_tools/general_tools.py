import os


def build_folder(ffp, name):
    try:
        os.makedirs(ffp, exist_ok=False)
    except OSError:
        print("%s folder already exists" % name)


def add_to_gitignore(initials):
    # Find gitignore file
    to_ignore = [".idea/",
                 "user_paths.py",
                 "*.pyc",
                 "temp_output/",
                 "%s_scripts/__pycache__/" % initials,
                 "%s_scripts/matplotlibrc" % initials,
                 "*TSWLatexianTemp_*",
                 "%s-paper/%s-paper.pdf" % (initials, initials)]
