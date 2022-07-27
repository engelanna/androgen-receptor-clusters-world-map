import os
import subprocess

from src.loaders import just_the_nonhidden_files, FastaDictFromFile


def multiple_fasta_to_single_multifasta(
    input_fasta_dir_path="assets/fasta/consensus_sequences",
    output_fasta_file_path="assets/fasta/clustering_input/mmseqs_input.fasta",
    fasta_loader=FastaDictFromFile(),
):
    output_fasta_file = open(output_fasta_file_path, "w")

    for input_fasta_file_name in sorted(just_the_nonhidden_files(input_fasta_dir_path)):
        input_fasta_file_path = f"{input_fasta_dir_path}/{input_fasta_file_name}"
        print(f"processing {input_fasta_file_path}")

        sequence_header, sequence = list(fasta_loader(input_fasta_file_path).items())[0]
        sequence_header = sequence_header[1:]
        sequence_header = (
            f">{input_fasta_file_name.replace('.fasta', '')}:{sequence_header}"
        )
        # at this point, the header is e.g. >filename:chrX:67543872-67730762
        output_fasta_file.write(f"{sequence_header}\n")
        output_fasta_file.write(f"{sequence}\n")

    output_fasta_file.close()


if __name__ == "__main__":
    multiple_fasta_to_single_multifasta()
