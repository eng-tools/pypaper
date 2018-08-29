import re
import bibtexparser
from pypaper import general_tools as gt


def build_base_folders(base_path, root_folder_name, initials, author=""):
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
    f_str = f_str.replace("###TITLE###", root_folder_name)
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


def combine_bibtex(bibtex_ffp1, bibtex_ffp2):
    """
    Merges to bibtex files

    :param ffp:
    :return:
    """

    with open(bibtex_ffp1) as bibtex_file:
        bibtex_database = bibtexparser.load(bibtex_file)

    with open(bibtex_ffp2) as org_bibtex_file:
        org_bibtex_database = bibtexparser.load(org_bibtex_file)

    for entry in bibtex_database.entries_dict:
        if entry not in org_bibtex_database.entries_dict:
            print("Not found: ", entry)
        # else:
        #     print('found')
        # print(entry, bibtex_database.entries_dict[entry])


def compile_bibtex(citations, big_bibtex_ffp):
    """
     finds the bibtex entries that correspond to a list of cite keys,
     from a large bibtex file and writes a new bibtex file
     with just the required references.
     :param citations: a list of citation keys.
    :param big_bibtex_ffp: full file path to bibtex file
    :return:
    """

    remove_keys = ["annote", "date-added", "date-modified", "local-url", "file", "rating", "month", "uri", "read"
                   "abstract", "read"]

    with open(big_bibtex_ffp) as org_bibtex_file:
        org_bibtex_database = bibtexparser.load(org_bibtex_file)

    new_bibtex_db = bibtexparser.loads(" ")  # create a new bibtex DB obj
    for entry in citations:
        if entry not in org_bibtex_database.entries_dict:
            print("Not found: ", entry)
        else:
            new_bibtex_db.entries.append(org_bibtex_database.entries_dict[entry])
            # new_bibtex_db.entries_dict[entry['ID']] = org_bibtex_database.entries_dict[entry]

    # new_bibtex_db = copy.deepcopy(org_bibtex_database)
    # for entry in org_bibtex_database.entries_dict:
    #     if entry not in citations:
    #         print("Not found: ", entry)
    #         del new_bibtex_db.entries_dict[entry]
    #     else:
    #         print("adding: ", entry)
    #         new_bibtex_db.entries_dict[entry] = org_bibtex_database.entries_dict[entry]

    # print(new_bibtex_db.entries)

    for entry in new_bibtex_db.entries_dict:
        for r_key in remove_keys:
            if r_key in new_bibtex_db.entries_dict[entry]:
                del new_bibtex_db.entries_dict[entry][r_key]
    bibtex_str = bibtexparser.dumps(new_bibtex_db)
    return bibtex_str


def extract_citation_keys_from_latex(latex_ffp, chicago=True):
    """
    Reads a latex file and returns a list of cite keys used.

    :param latex_ffp: full file path to latex file
    :return:
    """
    # \\cite\{([^\},]+)(?:,\s*([^\},]+))*\}
    # \\cite\{ = match anything that starts with \cite{
    # (  +) = creates a capture group
    # [^\}] = do not match anything with "}"
    #

    citations = []

    a = open(latex_ffp)
    lines = a.readlines()
    matches = []
    for line in lines:

        matches += re.findall(r'\\cite\{([^\}]+)(?:,\s*([^\},]+))*\}', line)
        matches += re.findall(r'\\citep\{([^\}]+)(?:,\s*([^\},]+))*\}', line)
        matches += re.findall(r'\\citet\{([^\}]+)(?:,\s*([^\},]+))*\}', line)
        matches += re.findall(r'\\citep\[e.g.\]\[\]\{([^\}]+)(?:,\s*([^\},]+))*\}', line)
        if chicago:
            matches += re.findall(r'\\citeN\{([^\}]+)(?:,\s*([^\},]+))*\}', line)
            matches += re.findall(r'\\citeNP\{([^\}]+)(?:,\s*([^\},]+))*\}', line)
            matches += re.findall(r'\\shortcite\{([^\}]+)(?:,\s*([^\},]+))*\}', line)
            matches += re.findall(r'\\shortciteN\{([^\}]+)(?:,\s*([^\},]+))*\}', line)
            matches += re.findall(r'\\shortciteNP\{([^\}]+)(?:,\s*([^\},]+))*\}', line)

    for m in matches:
        for new_cite in m:
            new_cite = new_cite.replace(" ", "")
            if new_cite == "":
                continue
            cites = new_cite.split(",")
            for single_cite in cites:
                if single_cite not in citations:
                    citations.append(single_cite)

    return citations


def small_bibtex_str(latex_ffp, full_bibtex_ffp, sort=True, verbose=False):
    """
    Reads a latex file and extracts the cite keys then finds
     the references in a large bibtex file and writes a new bibtex file
     with just the required references.

    :return:
    """
    citations = extract_citation_keys_from_latex(latex_ffp=latex_ffp)
    if sort:
        citations.sort()
    if verbose:
        for cite in citations:
            print(cite)
        print("Total number of citations: ", len(citations))
    b_str = compile_bibtex(citations, full_bibtex_ffp)
    return b_str


# if __name__ == '__main__':
#     ffp = "../tests/test_data_files/sample_latex.tex"
#     full_bibtex_ffp = "../tests/test_data_files/sample.bib"
#     citations = extract_citation_keys_from_latex(latex_ffp=ffp)
#     print(citations)
#
#     bstr = compile_bibtex(citations, full_bibtex_ffp)
#     print(bstr)
