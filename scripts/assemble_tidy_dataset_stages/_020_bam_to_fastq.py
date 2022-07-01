import os
import subprocess


def bam_to_fastq(
    input_bam_dir_path="assets/bam",
    reference_genome_file_path="assets/fasta/reference_genomes/hg38.fa",
    output_fastq_dir_path="assets/fastq",
):
    for input_bam_filename in sorted(
        [file for file in os.listdir(input_bam_dir_path) if not file.startswith(".")]
    ):
        input_bam_file_path = f"{input_bam_dir_path}/{input_bam_filename}"
        output_fastq_file_path = (
            f"{output_fastq_dir_path}/{input_bam_filename.rsplit('.', 1)[0]}.fastq"
        )
        command = "".join(
            [
                f"samtools mpileup --uncompressed --fasta-ref {reference_genome_file_path} {input_bam_file_path}",
                " | bcftools call --consensus-caller",
                f" | $(which vcfutils.pl) vcf2fq > {output_fastq_file_path}",
            ]
        )
        print(subprocess.run(command, shell=True))


if __name__ == "__main__":
    bam_to_fastq()
