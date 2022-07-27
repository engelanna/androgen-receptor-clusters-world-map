import pandas as pd


def clustering_results_to_map_dataframes(
    html_color_codes=pd.read_csv("assets/tsv/populations_lat_long.tsv", sep="\t"),
    populations_lat_long=pd.read_csv("assets/tsv/populations_lat_long.tsv", sep="\t"),
    clustering_output_dir_path="assets/tsv/clustering_output",
):
    clustering_output = pd.read_csv(
        "assets/tsv/clustering_output/min-seq-id-0.950.tsv",
        names=["Cluster representative", "Clustered sequence"],
        sep="\t",
    )
    # output_fasta_file = open(output_fasta_file_path, "w")

    # for input_fasta_file_name in sorted(just_the_nonhidden_files(input_fasta_dir_path)):
    #     input_fasta_file_path = f"{input_fasta_dir_path}/{input_fasta_file_name}"
    #     print(f"processing {input_fasta_file_path}")

    #     sequence_header, sequence = list(fasta_loader(input_fasta_file_path).items())[0]
    #     sequence_header = sequence_header[1:]
    #     sequence_header = (
    #         f">{input_fasta_file_name.replace('.fasta', '')}:{sequence_header}"
    #     )
    #     # at this point, the header is e.g. >filename:chrX:67543872-67730762
    #     output_fasta_file.write(f"{sequence_header}\n")
    #     output_fasta_file.write(f"{sequence}\n")

    # output_fasta_file.close()


if __name__ == "__main__":
    clustering_results_to_map_dataframes()
