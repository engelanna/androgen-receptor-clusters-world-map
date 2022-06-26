import os
import subprocess


def fastq_to_fasta_consensus(
    input_fastq_dir_path="../assets/fastq",
    output_fasta_dir_path="../assets/fasta/consensus_sequences",
):
    for input_fastq_file_name in sorted(
        [file for file in os.listdir(input_fastq_dir_path) if not file.startswith(".")]
    ):
        output_fasta_file_path = (
            f"{output_fasta_dir_path}/{input_fastq_file_name.rsplit('.', 1)[0]}.fasta"
        )
        input_fastq_file_path = f"{input_fastq_dir_path}/{input_fastq_file_name}"

        print(  # seqtk flags: https://github.com/lh3/seqtk
            subprocess.run(  # mask Q < 20 bases with lowercase
                f"seqtk seq -aQ64 -q20 {input_fastq_file_path} > {output_fasta_file_path}",
                shell=True,
            )
        )


if __name__ == "__main__":
    fastq_to_fasta_consensus()
