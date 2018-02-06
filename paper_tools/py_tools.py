from paper_tools import general_tools as gt


def build_base(base_path, fullname, initials, author=""):
    # Create folder for latex work
    py_path = "%s%s_scripts/" % (base_path, initials)
    gt.build_folder(py_path, "Python")
    # Create images folder and figures folder
    outputs_path = "%soutputs/" % py_path
    gt.build_folder(outputs_path, "Python outputs")
    figures_path = "%stemp-output/" % py_path
    gt.build_folder(figures_path, "Temp output")
    # TODO: Add toolkit folder, where users can put motion load files and soil profile load files.

    # Copy figure template file into location
    fname = 'figure_template.py'
    template_ffp = gt.get_template_ffp(fname)
    a = open(template_ffp)
    f_str = a.read()
    a.close()
    out_ffp = outputs_path + fname
    ofile = open(out_ffp, "w")
    ofile.write(f_str)
    ofile.close()
    # Add init file
    out_ffp = outputs_path + "__init__.py"
    ofile = open(out_ffp, "w")
    ofile.close()
