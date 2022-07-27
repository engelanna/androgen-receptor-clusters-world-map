from os.path import exists
import subprocess
import time


def download_bam_files(
    input_urls_file_path="assets/txt/download_bam_files_input_urls.txt",
    output_bam_dir_path="assets/bam",
):
    with open(input_urls_file_path, "r") as file:
        for index, url in enumerate([line.rstrip("\n") for line in file]):
            output_filename = (
                f"{output_bam_dir_path}/{url.split('/')[-1].replace('.cram', '.bam')}"
            )

            returncode = -1

            while returncode != 0:
                returncode = subprocess.run(
                    f"samtools view -hb {url} chrX:67544021-67730619 > {output_filename}",
                    shell=True,
                ).returncode

                index_file_name = f"{url.split('/')[-1]}.crai"
                if returncode != 0 and exists(index_file_name):
                    subprocess.run(f"rm {index_file_name}", shell=True)

            print(f"Downloaded {output_filename}")
            time.sleep(2)


if __name__ == "__main__":
    download_bam_files()
