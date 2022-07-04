from src.validators import validate_exon_has_full_cag_tract


def test_7_repeats_with_correct_boundaries_is_fine():
    assert True == validate_exon_has_full_cag_tract(f"TG{'CAG' * 7}CAA")


def test_over_7_repeats_with_correct_boundaries_is_fine():
    assert True == validate_exon_has_full_cag_tract(f"TG{'CAG' * 8}CAA")


def test_an_adenine_at_left_boundary_is_wrong():
    assert False == validate_exon_has_full_cag_tract(f"AG{'CAG' * 7}CAA")


def test_a_non_adenine_at_right_boundary_is_wrong():
    assert False == validate_exon_has_full_cag_tract(f"TG{'CAG' * 7}CAT")


def test_6_repeats_is_too_short_and_hence_wrong():
    assert False == validate_exon_has_full_cag_tract(f"CTG{'CAG' * 6}CAA")


def test_7_repeats_without_boundaries_is_wrong():
    assert False == validate_exon_has_full_cag_tract("CAG" * 7)


def test_enough_repeats_without_at_least_a_2_character_left_boundary_is_wrong():
    assert False == validate_exon_has_full_cag_tract(f"G{'CAG' * 7}CAA")


def test_enough_repeats_without_at_least_a_3_character_right_boundary_is_wrong():
    assert False == validate_exon_has_full_cag_tract(f"TG{'CAG' * 7}CA")
