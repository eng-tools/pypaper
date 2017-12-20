import os
import paper_tools
from paper_tools import general_tools as gt


def build_base(base_path, fullname, initials, author=""):
    # Create folder for latex work
    latex_path = "%s%s_paper/" % (base_path, initials)
    gt.build_folder(latex_path, "Latex")
    # Create images folder and figures folder
    images_path = "%s%s-images/" % (latex_path, initials)
    gt.build_folder(images_path, "Images")
    figures_path = "%s%s-figures/" % (latex_path, initials)
    gt.build_folder(figures_path, "Figures")
    # Copy base .svg file into image folder

    # Copy latex file into location

    template_ffp = gt.get_template_ffp('base-paper.tex')
    a = open(template_ffp)
    f_str = a.read()
    a.close()
    f_str = f_str.replace("###TITLE###", fullname)
    f_str = f_str.replace("###AUTHOR###", author)
    # Add example .svg file into latex
    latex_file_name = "%s-paper.tex" % initials
    out_ffp = latex_path + latex_file_name
    ofile = open(out_ffp, "w")
    ofile.write(f_str)
    ofile.close()


def find_references(fn):
    """
    Creates a cite key based on a function, or object or method.
    :param fn: function, object or method
    :return:
    """
    full_docstring = fn.__doc__
    ds_lines = full_docstring.split("\n")
    for line in ds_lines:
        if ".. [1]" in line:
            print(line)


def find_equations(fn):
    """
    Creates a latex equation based on a function, or object or method.
    :param fn: function, object or method
    :return:
    """
    full_docstring = fn.__doc__
    ds_lines = full_docstring.split("\n")
    for line in ds_lines:
        if ".. math" in line:
            print(line)