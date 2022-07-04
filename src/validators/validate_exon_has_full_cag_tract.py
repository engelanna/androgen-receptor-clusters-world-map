def cag_repeat_count(exon: str):
    exon = exon.lower()
    pattern = "cag"

    while pattern in exon:
        pattern += "cag"

    return (len(pattern) - 1) // 3


# The spec is at test/validators/validate_exon_has_full_cag_tract
def validate_exon_has_full_cag_tract(exon: str):
    exon = exon.lower()

    try:
        if (
            cag_repeat_count(exon) < 7
            or exon.index("cag") < 2
            or exon[exon.index("cag") - 2] == "a"
            or len(exon) - exon.rindex("cag") < 6
            or exon[exon.rindex("cag") + 5] != "a"
        ):
            return False
    except IndexError:
        return False
    except ValueError:
        return False

    return True
