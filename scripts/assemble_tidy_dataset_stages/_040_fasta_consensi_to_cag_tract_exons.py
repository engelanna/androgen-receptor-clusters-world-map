import os
import subprocess

from src.extractors import exon_with_the_most_cag_repeats


def fasta_consensi_to_cag_tract_exons(
    input_fasta_dir_path="assets/fasta/consensus_sequences",
    output_fasta_dir_path="assets/fasta/cag_tract_exons",
    intron_character="n",
):
    for input_fasta_file_name in sorted(
        [file for file in os.listdir(input_fasta_dir_path) if not file.startswith(".")]
    ):
        input_fasta_file_path = f"{input_fasta_dir_path}/{input_fasta_file_name}"

        sequence = open(input_fasta_file_path, "r").readlines()[1].strip()
        exon_list = [exon for exon in sequence.split(intron_character) if exon]
        cag_exon = exon_with_the_most_cag_repeats(exon_list)

        fasta_header = input_fasta_file_name.rsplit(".", 1)[0]
        output_fasta_file_path = f"{output_fasta_dir_path}/{fasta_header}.fasta"

        with open(output_fasta_file_path, "w") as output_fasta_file:
            output_fasta_file.write(f">{fasta_header}\n")
            output_fasta_file.write(f"{cag_exon}\n")

        print(f"wrote {output_fasta_file_path}")


if __name__ == "__main__":
    fasta_consensi_to_cag_tract_exons()
