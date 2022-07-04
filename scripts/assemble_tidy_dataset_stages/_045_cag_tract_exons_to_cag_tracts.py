import os

from src.extractors import extract_full_cag_tract
from src.validators import validate_exon_has_full_cag_tract


_just_the_nonhidden_files = lambda dir: [
    file for file in os.listdir(dir) if not file.startswith(".")
]


def cag_tract_exons_to_cag_tracts(
    input_fasta_dir_path="assets/fasta/cag_tract_exons",
    output_fasta_dir_path="assets/fasta/cag_tracts",
):
    for input_fasta_file_name in sorted(
        _just_the_nonhidden_files(input_fasta_dir_path)
    ):
        input_fasta_file_path = f"{input_fasta_dir_path}/{input_fasta_file_name}"

        with open(input_fasta_file_path, "r") as input_fasta_file:
            cag_exon = input_fasta_file.readlines()[1].strip()
            fasta_header = input_fasta_file_name.rsplit(".", 1)[0]

            if validate_exon_has_full_cag_tract(cag_exon):
                full_cag_tract = extract_full_cag_tract(cag_exon)
                output_fasta_file_path = (
                    f"{output_fasta_dir_path}/{input_fasta_file_name}"
                )
                with open(output_fasta_file_path, "w") as output_fasta_file:
                    output_fasta_file.write(f">{fasta_header}\n")
                    output_fasta_file.write(f"{full_cag_tract}\n")
            else:
                print(f"dropping exon {fasta_header} (incomplete CAG tract)")


if __name__ == "__main__":
    cag_tract_exons_to_cag_tracts()
