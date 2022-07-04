from .assemble_tidy_dataset_stages import (
    download_bam_files,
    bam_to_fastq,
    fastq_to_fasta_consensi,
    fasta_consensi_to_cag_tract_exons,
    multiple_fasta_to_single_multifasta,
)

download_bam_files()
bam_to_fastq()
fastq_to_fasta_consensi()
fasta_consensi_to_cag_tract_exons()
multiple_fasta_to_single_multifasta()
