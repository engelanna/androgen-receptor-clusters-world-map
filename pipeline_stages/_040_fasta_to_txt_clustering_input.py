import os
import subprocess


def fasta_to_txt_clustering_input(
    input_fasta_dir_path="../assets/fasta",
    output_dir_path="../assets/clustering_txt_input",
):

    for input_fasta_file_name in os.listdir(input_fasta_dir_path):
        input_fasta_file_path = f"{input_fasta_dir_path}/{input_fasta_file_name}"

        sequence = open(input_fasta_file_path, "r").readlines()[1].strip()
        sequence = sequence.lstrip("N")
        sequence = sequence.rstrip("N")

        output_file_path = (
            f"{output_dir_path}/{input_fasta_file_name.rsplit('.', 1)[0]}.txt"
        )
        output_file = open(output_file_path, "w")
        output_file.write(sequence)
        output_file.close()


if __name__ == "__main__":
    fasta_to_txt_clustering_input()
