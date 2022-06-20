import subprocess
import time


with open("../assets/download_bam_files_input_urls.txt", "r") as file:
    for url in [line.rstrip("\n") for line in file if len(line) > 1]:
        time.sleep(2)

        output_filename = "../output/bam/" + url.split("/")[-1].replace(".cram", ".bam")

        completed_process = subprocess.run(
            f"samtools view -hb {url} chrX:67544021-67730619 > {output_filename}",
            shell=True,
        )

        print(completed_process)
