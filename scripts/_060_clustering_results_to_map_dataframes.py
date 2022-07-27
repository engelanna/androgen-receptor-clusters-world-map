import pandas as pd
import pydeck

from src.loaders import just_the_nonhidden_files


file_name_to_sample_name = lambda column: column.split(".")[0]


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
        for colname in list(clusters_df):
            clusters_df[colname] = clusters_df[colname].apply(file_name_to_sample_name)

        color_lookup = pydeck.data_utils.assign_random_colors(
            clusters_df["Cluster representative"]
        )
        clusters_df["Color"] = clusters_df.apply(
            lambda row: color_lookup.get(row["Cluster representative"]), axis=1
        )
        print(clusters_df)


if __name__ == "__main__":
    clustering_results_to_map_dataframes()
