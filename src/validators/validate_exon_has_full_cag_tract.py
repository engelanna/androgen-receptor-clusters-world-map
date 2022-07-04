def cag_repeat_count(exon: str):
    exon = exon.lower()
    pattern = "cag"

    while pattern in exon:
        pattern += "cag"

    return (len(pattern) - 1) // 3


# The spec is at test/validators/validate_exon_has_full_cag_tract
def validate_exon_has_full_cag_tract(exon: str):
    try:
        exon = exon.lower()
        left_limit_of_7_cag_repeats = exon.index("cag" * 7)
        right_limit_of_7_cag_repeats = exon.rindex("cag" * 7) + 21
        if (
            cag_repeat_count(exon) < 7
            or left_limit_of_7_cag_repeats < 2
            or (
                left_limit_of_7_cag_repeats == 2
                and exon[left_limit_of_7_cag_repeats - 2] == "a"
            )
            or (len(exon) - right_limit_of_7_cag_repeats) < 3
            or (len(exon) - right_limit_of_7_cag_repeats == 3 and exon[-1] != "a")
        ):
            return False
    except IndexError:
        return False
    except ValueError:
        return False

    return True
