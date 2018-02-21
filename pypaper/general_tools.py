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


def build_base_folders(base_path, root_folder_name, initials):
    """
    Creates the project folders

    :param base_path:
    :param root_folder_name:
    :param initials:
    :return:
    """
    # Create the project root folder
    project_path = "%s%s/" % (base_path, root_folder_name)
    build_folder(project_path, "Base")
    # Create the project temporary output folder
    build_folder(project_path + "temp/", "Temporary")
    # Create the project module data output folder
    data_path = "%s%s_data/" % (project_path, initials)
    build_folder(data_path, "Project data")
    return project_path


def get_template_ffp(template_name):
    """
    Gets the full path to the template

    :param template_name:
    :return:
    """
    templates_dir = os.path.join(os.path.dirname(pypaper.__file__), 'templates')
    template_file = os.path.join(templates_dir, template_name)
    return template_file


def template_to_folder(template_name, folder_path):
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
    out_ffp = folder_path + template_name
    ofile = open(out_ffp, "w")
    ofile.write(f_str)
    ofile.close()


def add_to_gitignore(base_path, initials):
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
                 "temp/*"
                 ]
    a = open(base_path + ".gitignore", "a")
    a.write("\n" + "\n".join(to_ignore))
    a.close()


def add_to_requirements_txt(project_root_folder):
    """
    Adds python packages used in project

    :param project_root_folder:
    :return:
    """
    to_ignore = ["matplotlib",
                 "bwplot",
                 "engformat"

                 ]
    a = open(project_root_folder + "requirements.txt", "a")
    a.write("\n" + "\n".join(to_ignore))
    a.close()
