from paper_tools import general_tools as gt


def build_base(base_path, fullname, initials, author=""):
    # Create folder for latex work
    py_path = "%s%s_scripts/" % (base_path, initials)
    gt.build_folder(py_path, "Python")
    # Create images folder and figures folder
    images_path = "%soutputs/" % py_path
    gt.build_folder(images_path, "Python outputs")
    figures_path = "%s%s-figures/" % (py_path, initials)
    gt.build_folder(figures_path, "Figures")

    # Copy latex file into location
    a = open("../paper_files/base-paper.tex")
