import pandas as pd
import pydeck

from src.loaders import just_the_nonhidden_files


file_name_to_sample_name = lambda column: column.split(".")[0]


def clustering_results_to_map_dataframes(
    df_samples=pd.read_csv("assets/tsv/samples.tsv", sep="\t"),
    df_populations=pd.read_csv("assets/tsv/populations.tsv", sep="\t"),
    clusters_dir_path="assets/tsv/clustering_output",
    map_dataframes_output_dir_path="assets/tsv/map_ready_dataframes",
):

    for cluster_tsv_file_name in just_the_nonhidden_files(clusters_dir_path):
        df_clusters = pd.read_csv(
            f"{clusters_dir_path}/{cluster_tsv_file_name}",
            names=["Cluster name", "Sample name"],
            sep="\t",
        )
        for colname in list(df_clusters):
            df_clusters[colname] = df_clusters[colname].apply(file_name_to_sample_name)

        sample_name_join = pd.merge(
            df_clusters, df_samples, on=["Sample name"], how="left"
        )
        df_clusters["Sample link"] = (
            f"https://www.internationalgenome.org/data-portal/sample/"
            + df_clusters["Sample name"]
        )
        df_clusters["Population link"] = (
            "https://www.internationalgenome.org/data-portal/population/"
            + sample_name_join["Population elastic ID"]
        )
        df_clusters = df_clusters.merge(df_samples, on="Sample name").merge(
            df_populations, on="Population elastic ID"
        )
        df_clusters.to_csv(
            f"{map_dataframes_output_dir_path}/{cluster_tsv_file_name}",
            index=False,
            sep="\t",
        )
        print(df_clusters)


if __name__ == "__main__":
    clustering_results_to_map_dataframes()
