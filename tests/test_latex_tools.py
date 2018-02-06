import os
from paper_tools import latex_tools as lt

test_dir = os.path.dirname(__file__)

def test_latex_build():
    pass


def test_compile_bibtex():
    ffp = test_dir + "/test_data_files/sample.bib"
    citations = ["Safak:1992ub", "Vesic:1975"]
    not_cited = ["Rodriguez:2000sr"]

    bibtex_str = lt.compile_bibtex(citations, ffp)
    print(bibtex_str)
    for cite in citations:
        assert cite in bibtex_str, cite
    for cite in not_cited:
        assert cite not in bibtex_str

    # can not find
    unlisted_citations = ["Rathje:2017ip"]

    bibtex_str = lt.compile_bibtex(unlisted_citations, ffp)
    for cite in unlisted_citations:
        assert cite not in bibtex_str


def test_extract_citations():
    ffp = test_dir + "/test_data_files/sample_latex.tex"
    expected_citations = ['Vesic:1975', 'Chatzigogos:2008uv', 'Safak:1992ub', 'Raychowdhury:2009hw']
    citations = lt.extract_citation_keys_from_latex(latex_ffp=ffp)
    assert len(expected_citations) == len(citations)
    for ec in expected_citations:
        assert ec in citations


if __name__ == '__main__':
    test_extract_citations()