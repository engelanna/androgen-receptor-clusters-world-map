import os
import subprocess

from src.loaders import just_the_nonhidden_files

_run_shell_command = lambda command: print(subprocess.run(command, shell=True))


def reheader_bam_files_in_place(bam_dir_path="assets/bam"):
    for bam_filename in sorted(just_the_nonhidden_files(bam_dir_path)):
        bam_file_path = f"{bam_dir_path}/{bam_filename}"
        tmp_bam_file_path = f"{bam_file_path}.tmp"
        header_file_path = f"{bam_file_path}.header"

        _run_shell_command(f"samtools view -H {bam_file_path} > {header_file_path}")
        _run_shell_command(
            f"samtools reheader --no-PG {header_file_path} {bam_file_path} > {tmp_bam_file_path}"
        )
        _run_shell_command(f"mv {tmp_bam_file_path} {bam_file_path}")
    _run_shell_command(f"rm {header_file_path}")


if __name__ == "__main__":
    reheader_bam_files_in_place()
