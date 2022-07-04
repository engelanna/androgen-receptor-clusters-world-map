import re


def extract_full_cag_tract(exon: str):
    return re.search("(cag){7,}", exon, re.IGNORECASE).group()
