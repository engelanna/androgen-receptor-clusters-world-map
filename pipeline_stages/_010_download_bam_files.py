import subprocess
import time


def download_bam_files(
    input_urls_file_path="../assets/download_bam_files_input_urls.txt",
    output_bam_dir_path="../assets/bam",
):
    with open(input_urls_file_path, "r") as file:
        for url in [line.rstrip("\n") for line in file if len(line) > 1]:
            time.sleep(2)

            output_filename = (
                f"{output_bam_dir_path}/{url.split('/')[-1].replace('.cram', '.bam')}"
            )

            completed_process = subprocess.run(
                f"samtools view -hb {url} chrX:67544021-67730619 > {output_filename}",
                shell=True,
            )

            print(completed_process)


if __name__ == "__main__":
    download_bam_files()
