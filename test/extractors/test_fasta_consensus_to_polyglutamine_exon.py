from pytest import fixture

from src.extractors import exon_with_the_most_cag_repeats


class TestFastaConsensusToPolyglutamineExon:
    @fixture
    def exons(self):
        return [
            "TGGTCAgcACGTACGTTGCcagcAGCagACTGactgCTGACTGACTgCTGACTGAGTACGAC",
            "actACTAGCcAgCaGCAGcaGtAGCTGcaTGCTC",
            "CTGcaTGCTCaGACTACGTACGTAcTGACGTAcAGTCATgCAGCAGCAGTCAtgACGTAC",
        ]

    def test_detect_exon_with_the_most_cag_repeats(self, exons):
        expected = exons[1]
        actual = exon_with_the_most_cag_repeats(exons)

        assert expected == actual
