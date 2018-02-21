from pypaper import general_tools as gt


def add_init_file(folder_path):
    new_file = open(folder_path + "__init__.py", "w")
    new_file.close()


def build_base_folders(root_folder_full_path, initials):
    # Create folder for latex work
    py_path = "%s%s_scripts/" % (root_folder_full_path, initials)
    gt.build_folder(py_path, "Python")

    # Create images folder and figures folder
    outputs_path = "%soutputs/" % py_path
    gt.build_folder(outputs_path, "Python outputs")
    add_init_file(outputs_path)

    # Create project tools folder
    tools_path = "%stools/" % py_path
    gt.build_folder(tools_path, "Python tools")
    add_init_file(tools_path)

    # Create project research folder
    research_path = "%sresearch/" % py_path
    gt.build_folder(research_path, "Python research")
    add_init_file(research_path)

    # Copy figure template file into location
    fname = 'figure_template.py'
    gt.template_to_folder(fname, outputs_path)



def add_project_python_files(project_root_folder):
    fname = 'all_paths.py'
    gt.template_to_folder(fname, project_root_folder)
    pass