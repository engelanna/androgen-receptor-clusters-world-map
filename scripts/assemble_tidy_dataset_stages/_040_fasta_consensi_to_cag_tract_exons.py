import os
import subprocess

from src.extractors import extract_exon_with_the_most_cag_repeats
from src.loaders import (
    FastaDictFromFile,
    just_the_nonhidden_files,
)


def fasta_consensi_to_cag_tract_exons(
    input_fasta_dir_path="assets/fasta/consensus_sequences",
    output_fasta_dir_path="assets/fasta/cag_tract_exons",
    fasta_dict_loader=FastaDictFromFile(),
):
    for input_fasta_file_name in sorted(just_the_nonhidden_files(input_fasta_dir_path)):
        input_fasta_file_path = f"{input_fasta_dir_path}/{input_fasta_file_name}"

        exon_list = list(fasta_dict_loader(input_fasta_file_path).values())
        cag_exon = extract_exon_with_the_most_cag_repeats(exon_list)

        fasta_header = input_fasta_file_name.rsplit(".", 1)[0]
        output_fasta_file_path = f"{output_fasta_dir_path}/{fasta_header}.fasta"

        with open(output_fasta_file_path, "w") as output_fasta_file:
            output_fasta_file.write(f"{cag_exon}\n")

        print(f"wrote {output_fasta_file_path}")


if __name__ == "__main__":
    fasta_consensi_to_cag_tract_exons()
