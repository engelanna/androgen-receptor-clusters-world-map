import os
import subprocess


def many_txt_to_single_fasta(
    input_txt_files_dir_path="../assets/txt",
    output_fasta_file_path="../assets/fasta/testData.fasta",
):
    output_fasta_file = open(output_fasta_file_path, "w")

    for input_txt_file_name in [
        file
        for file in os.listdir(input_txt_files_dir_path)
        if not file.startswith(".")
    ]:
        input_txt_file_path = f"{input_txt_files_dir_path}/{input_txt_file_name}"

        sequence = open(input_txt_file_path, "r").readlines()[0]
        sequence_header = input_txt_file_name.replace(".txt", "")

        output_fasta_file.writelines([f"> {sequence_header}\n", f"{sequence}"])

    output_fasta_file.close()


if __name__ == "__main__":
    many_txt_to_single_fasta()
