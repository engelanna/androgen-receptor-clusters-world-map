import os
import subprocess


def fastq_to_fasta(
    input_fastq_dir_path="../assets/fastq", output_fasta_dir_path="../assets/fasta"
):
    for input_fastq_file_name in os.listdir(input_fastq_dir_path):
        output_fasta_file_path = (
            f"{output_fasta_dir_path}/{input_fastq_file_name.rsplit('.', 1)[0]}.fasta"
        )
        input_fastq_file_path = f"{input_fastq_dir_path}/{input_fastq_file_name}"

        print(
            subprocess.run(
                f"seqtk seq -aQ64 -q20 -n N {input_fastq_file_path} > {output_fasta_file_path}",
                shell=True,
            )
        )


if __name__ == "__main__":
    fastq_to_fasta()
