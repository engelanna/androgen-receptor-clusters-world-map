import os
import subprocess


def fasta_consensi_to_cag_tract_exons(
    input_fasta_dir_path="assets/fasta/consensus_sequences",
    output_fasta_dir_path="assets/fasta/cag_tract_exons",
    intron_character="n",
):
    for input_fasta_file_name in sorted(
        [file for file in os.listdir(input_fasta_dir_path) if not file.startswith(".")]
    ):
        input_fasta_file_path = f"{input_fasta_dir_path}/{input_fasta_file_name}"
        print(f"processing {input_fasta_file_path}")

        sequence = open(input_fasta_file_path, "r").readlines()[1].strip()
        sequence = sequence.lstrip(intron_character).rstrip(intron_character)

        output_fasta_file_path = (
            f"{output_fasta_dir_path}/{input_fasta_file_name.rsplit('.', 1)[0]}.fasta"
        )

        with open(output_fasta_file_path, "w") as output_fasta_file:
            output_fasta_file.write(f"{sequence}\n")


if __name__ == "__main__":
    fasta_consensi_to_cag_tract_exons()
