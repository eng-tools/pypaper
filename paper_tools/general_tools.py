import os
import paper_tools


def build_folder(ffp, name):
    try:
        os.makedirs(ffp, exist_ok=False)
    except OSError:
        print("%s folder already exists" % name)


def build_base(base_path, fullname):
    # Create folder for latex work
    paper_path = "%s%s_paper/" % (base_path, fullname)
    build_folder(paper_path, "Base")
    return paper_path


def get_template_ffp(template_name):
    templates_dir = os.path.join(os.path.dirname(paper_tools.__file__), 'templates')
    template_file = os.path.join(templates_dir, template_name)
    return template_file


def add_to_gitignore(base_path, initials):
    # Find gitignore file
    to_ignore = [".idea/",
                 "user_paths.py",
                 "*.pyc",
                 "temp_output/",
                 "%s_scripts/__pycache__/" % initials,
                 "%s_scripts/matplotlibrc" % initials,
                 "*TSWLatexianTemp_*",
                 "%s-paper/%s-paper.pdf" % (initials, initials)]
    a = open(base_path + ".gitignore", "a")
    a.write("\n" + "\n".join(to_ignore))
    a.close()
