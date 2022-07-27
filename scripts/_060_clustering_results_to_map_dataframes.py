import pandas as pd

from src.loaders import just_the_nonhidden_files


file_name_to_sample_name = lambda file_name: file_name.split(".")[0]


def clustering_results_to_map_dataframes(
    html_color_codes=pd.read_csv("assets/tsv/populations_lat_long.tsv", sep="\t"),
    populations_lat_long=pd.read_csv("assets/tsv/populations_lat_long.tsv", sep="\t"),
    clusters_dir_path="assets/tsv/clustering_output",
):
    for cluster_tsv_file_name in sorted(just_the_nonhidden_files(clusters_dir_path)):
        clusters_df = pd.read_csv(
            f"{clusters_dir_path}/{cluster_tsv_file_name}",
            names=["Cluster representative", "Clustered sequence"],
            sep="\t",
        )
        print(clusters_df)
    # output_fasta_file = open(output_fasta_file_path, "w")

    #     sequence_header, sequence = list(fasta_loader(input_fasta_file_path).items())[0]
    #     sequence_header = sequence_header[1:]
    #     sequence_header = (
    #         f">{cluster_tsv_file_name.replace('.fasta', '')}:{sequence_header}"
    #     )
    #     # at this point, the header is e.g. >filename:chrX:67543872-67730762
    #     output_fasta_file.write(f"{sequence_header}\n")
    #     output_fasta_file.write(f"{sequence}\n")

    # output_fasta_file.close()


if __name__ == "__main__":
    clustering_results_to_map_dataframes()
