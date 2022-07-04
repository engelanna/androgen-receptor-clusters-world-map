from pytest import fixture

from src.extractors import extract_exon_with_the_most_cag_repeats


@fixture
def exons():
    return [
        "TGGTCAgcACGTACGTTGCcagcAGCagACTGactgCTGACTGACTgCTGACTGAGTACGAC",
        "actACTAGCcAgCaGCAGcaGtAGCTGcaTGCTC",
        "CTGcaTGCTCaGACTACGTACGTAcTGACGTAcAGTCATgCAGCAGCAGTCAtgACGTAC",
    ]


def test_extract_exon_with_the_most_cag_repeats(exons):
    expected = exons[1]
    actual = extract_exon_with_the_most_cag_repeats(exons)

    assert expected == actual
