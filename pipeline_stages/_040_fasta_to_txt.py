import os
import subprocess


def fasta_to_txt(
    input_fasta_dir_path="../assets/fasta/consensus_sequences",
    output_txt_dir_path="../assets/txt",
):
    for input_fasta_file_name in sorted(
        [file for file in os.listdir(input_fasta_dir_path) if not file.startswith(".")]
    ):
        input_fasta_file_path = f"{input_fasta_dir_path}/{input_fasta_file_name}"
        print(f"processing {input_fasta_file_path}")

        sequence = open(input_fasta_file_path, "r").readlines()[1].strip()
        sequence = sequence.lstrip("N")
        sequence = sequence.rstrip("N")

        output_txt_file_path = (
            f"{output_txt_dir_path}/{input_fasta_file_name.rsplit('.', 1)[0]}.txt"
        )

        with open(output_txt_file_path, "w") as output_txt_file:
            output_txt_file.write(f"{sequence}\n")


if __name__ == "__main__":
    fasta_to_txt()
