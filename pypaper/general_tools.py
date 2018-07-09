import os
import pypaper


def build_folder(ffp, name):
    """
    Makes a new directory

    :param ffp:
    :param name:
    :return:
    """
    try:
        os.makedirs(ffp, exist_ok=False)
    except OSError:
        print("%s folder already exists" % name)


def build_base_folders(root_folder_full_path, initials):
    """
    Creates the project folders

    :param root_folder_full_path:
    :param initials:
    :return:
    """
    # Create the project temporary output folder
    build_folder(root_folder_full_path + "temp/", "Temporary")
    # Create the project module data output folder
    data_path = "%sdata/" % root_folder_full_path
    build_folder(data_path, "Project data")
    # Copy template files into location
    fname = 'settings.py'
    template_to_folder(fname, root_folder_full_path)
    fname = 'all_paths.py'
    ap_replacements = {"###INITIALS###": initials}
    template_to_folder(fname, root_folder_full_path, ap_replacements)
    fname = 'user_paths.py'
    template_to_folder(fname, root_folder_full_path)
    return root_folder_full_path


def get_template_ffp(template_name):
    """
    Gets the full path to the template

    :param template_name:
    :return:
    """
    templates_dir = os.path.join(os.path.dirname(pypaper.__file__), 'templates')
    template_file = os.path.join(templates_dir, template_name)
    return template_file


def template_to_folder(template_name, folder_path, replacements={}):
    """
    Copies a template into a folder

    :param template_name:
    :param folder_path:
    :return:
    """
    template_ffp = get_template_ffp(template_name)
    a = open(template_ffp)
    f_str = a.read()
    a.close()
    for key in replacements:
        f_str = f_str.replace(key, replacements[key])
    out_ffp = folder_path + template_name
    ofile = open(out_ffp, "w")
    ofile.write(f_str)
    ofile.close()


def add_to_gitignore(root_folder_full_path, initials):
    """
    Add a list of files that should not be tracked by git

    :param base_path:
    :param initials:
    :return:
    """
    # Find gitignore file
    to_ignore = ["# Added by pypaper",
                 ".idea/",
                 "user_paths.py",
                 "*.pyc",
                 "temp_output/",
                 "%s_scripts/__pycache__/" % initials,
                 "%s_scripts/matplotlibrc" % initials,
                 "*TSWLatexianTemp_*",
                 "%s-paper/%s-paper.pdf" % (initials, initials),
                 "temp/*",
                 "venv/"
                 ]
    a = open(root_folder_full_path + ".gitignore", "a")
    a.write("\n" + "\n".join(to_ignore))
    a.close()


def add_to_requirements_txt(root_folder_full_path):
    """
    Adds python packages used in project

    :param project_root_folder:
    :return:
    """
    to_ignore = ["matplotlib",
                 "bwplot",
                 "engformat>=0.1.3"

                 ]
    a = open(root_folder_full_path + "requirements.txt", "a")
    a.write("\n" + "\n".join(to_ignore))
    a.close()
