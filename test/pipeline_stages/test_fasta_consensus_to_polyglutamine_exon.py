from pytest import fixture
from typing import List


def fasta_consensus_to_polyglutamine_exon(exons_list: List):
    max_cag_repeat_count = 0
    max_cag_repeat_index = -1

    for index, exon in enumerate(exons_list):
        lowercase_exon = exon.lower()
        pattern = "cag"
        cag_repeat_count = 0

        while pattern in lowercase_exon:
            cag_repeat_count += 1
            pattern += "cag"

        if cag_repeat_count > max_cag_repeat_count:
            max_cag_repeat_count = cag_repeat_count
            max_cag_repeat_index = index

    return exons_list[max_cag_repeat_index]


class TestFastaConsensusToPolyglutamineExon:
    @fixture
    def exons_list(self):
        return [
            "TGGTCAgcACGTACGTTGCcagcAGCagACTGactgCTGACTGACTgCTGACTGAGTACGAC",
            "actACTAGCcAgCaGCAGcaGtAGCTGcaTGCTC",
            "CTGcaTGCTCaGACTACGTACGTAcTGACGTAcAGTCATgCAGCAGCAGTCAtgACGTAC",
        ]

    def test_detect_exon_with_the_most_cag_repeats(self, exons_list):
        expected = exons_list[1]
        actual = fasta_consensus_to_polyglutamine_exon(exons_list)

        assert expected == actual
