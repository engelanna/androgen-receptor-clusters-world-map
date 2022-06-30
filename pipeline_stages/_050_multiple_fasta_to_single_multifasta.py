import os
import subprocess


def multiple_fasta_to_single_multifasta(
    input_fasta_dir_path="../assets/fasta/",
    output_fasta_file_path="../assets/fasta/clustering_input/cd_hit_input.fasta",
):
    output_fasta_file = open(output_fasta_file_path, "w")

    for input_fasta_file_name in sorted(
        [file for file in os.listdir(input_fasta_dir_path) if not file.startswith(".")]
    ):
        input_fasta_file_path = f"{input_fasta_dir_path}/{input_fasta_file_name}"
        print(f"processing {input_fasta_file_path}")

        sequence = open(input_fasta_file_path, "r").readlines()[0]
        sequence_header = input_fasta_file_name.replace(".txt", "")

        output_fasta_file.writelines([f">{sequence_header}\n", f"{sequence}"])

    output_fasta_file.close()


if __name__ == "__main__":
    multiple_fasta_to_single_multifasta()
