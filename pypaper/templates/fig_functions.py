

def latex_for_figure(ap, name, ftype):
    str_parts = ["",
                    "\\begin{figure}[H]",
                    "\centering",
                    "\\includegraphics{%s/%s%s}" % (ap.FIGURE_FOLDER, name, ftype),
                    "\\caption{%s \label{fig: %s}}" % (name.replace("_", " "), name),
                    "\\end{figure}"
                 ]
    return "\n".join(str_parts)
