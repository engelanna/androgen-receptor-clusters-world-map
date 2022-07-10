import os
import subprocess

from src.loaders import just_the_nonhidden_files


def multiple_fasta_to_single_multifasta(
    input_fasta_dir_path="assets/fasta/cag_tract_exons",
    output_fasta_file_path="assets/fasta/clustering_input/cd_hit_input.fasta",
):
    output_fasta_file = open(output_fasta_file_path, "w")

    for input_fasta_file_name in sorted(just_the_nonhidden_files(input_fasta_dir_path)):
        input_fasta_file_path = f"{input_fasta_dir_path}/{input_fasta_file_name}"
        print(f"processing {input_fasta_file_path}")

        sequence = open(input_fasta_file_path, "r").readlines()[1]
        sequence_header = input_fasta_file_name.replace(".fasta", "")

        output_fasta_file.writelines([f">{sequence_header}\n", f"{sequence}"])

    output_fasta_file.close()


if __name__ == "__main__":
    multiple_fasta_to_single_multifasta()
