
from pypaper import latex_tools
import all_paths as ap

INITIALS = "###INITIALS###"

latex_ffp = "%s%s-paper.tex" % (ap.PUBLICATION_PATH, INITIALS)
full_bibtex_ffp = "<path-to-full-bibtex-file>"
local_bibtex_ffp = ap.PUBLICATION_PATH + "%s-references.bib" % INITIALS

clean_first = 1
if clean_first:  # remove month attribute
    a = open(full_bibtex_ffp)
    lines = a.readlines()
    a.close()
    output = []
    for line in lines:
        if "month = " not in line:
            output.append(line)
    ofile = open(full_bibtex_ffp, "w")
    ofile.write("\n".join(output))
    ofile.close()

# citations = latex_tools.extract_citation_keys_from_latex(latex_ffp=latex_ffp)
# citations.sort()
# for citation in citations:
#     print(citation)
p_str = latex_tools.small_bibtex_str(latex_ffp, full_bibtex_ffp, sort=True, verbose=True)
ofile = open(local_bibtex_ffp, "w")
ofile.write(p_str)
ofile.close()

