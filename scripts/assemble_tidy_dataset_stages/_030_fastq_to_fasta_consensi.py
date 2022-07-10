import os
import subprocess


def fastq_to_fasta_consensi(
    input_fastq_dir_path="assets/fastq",
    output_fasta_dir_path="assets/fasta/consensus_sequences",
):
    for input_fastq_file_name in sorted(
        [file for file in os.listdir(input_fastq_dir_path) if not file.startswith(".")]
    ):
        output_fasta_file_path = (
            f"{output_fasta_dir_path}/{input_fastq_file_name.rsplit('.', 1)[0]}.fasta"
        )
        input_fastq_file_path = f"{input_fastq_dir_path}/{input_fastq_file_name}"

        command = "".join(  # seqtk flags: https://github.com/lh3/seqtk
            [
                f"seqtk seq -aQ64 -q20 {input_fastq_file_path}",  # downcase Q<20 bases
                f" | seqtk cutN - > {output_fasta_file_path}",  # cut on 100 introns (default)
            ]
        )

        print(subprocess.run(command, shell=True))


if __name__ == "__main__":
    fastq_to_fasta_consensi()
