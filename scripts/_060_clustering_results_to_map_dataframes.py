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
            names=["ClusterName", "SampleName"],
            sep="\t",
        )
        for colname in list(df_clusters):
            df_clusters[colname] = df_clusters[colname].apply(file_name_to_sample_name)

        df_clusters = df_clusters.merge(df_samples, on="SampleName").merge(
            df_populations, on="PopulationElasticId"
        )
        df_clusters["SampleLink"] = (
            f"https://www.internationalgenome.org/data-portal/sample/"
            + df_clusters["SampleName"]
        )
        df_clusters["PopulationLink"] = (
            "https://www.internationalgenome.org/data-portal/population/"
            + df_clusters["PopulationElasticId"]
        )
        df_clusters = df_clusters[(sorted(list(df_clusters)))]
        df_clusters.to_csv(
            f"{map_dataframes_output_dir_path}/{cluster_tsv_file_name}",
            index=False,
            sep="\t",
        )
        print(df_clusters)


if __name__ == "__main__":
    clustering_results_to_map_dataframes()
