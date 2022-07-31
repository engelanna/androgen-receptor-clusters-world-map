import pandas as pd

from src import ScatterSameCoordinatePoints
from src.loaders import (
    ColorLookup,
    just_the_nonhidden_files,
)


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
        df_clusters["Latitude"] = ScatterSameCoordinatePoints()(df_clusters["Latitude"])
        df_clusters["Longitude"] = ScatterSameCoordinatePoints()(
            df_clusters["Longitude"]
        )
        color_lookup = ColorLookup().assign_colors(df_clusters["ClusterName"])
        df_clusters["Color"] = df_clusters.apply(
            lambda row: color_lookup.get(row["ClusterName"]), axis=1
        )
        df_clusters["Elevation"] = [
            0.9 if x == [255, 255, 255] else 1.0 for x in df_clusters["Color"]
        ]
        df_clusters = df_clusters[(sorted(list(df_clusters)))]
        df_clusters.to_csv(
            f"{map_dataframes_output_dir_path}/{cluster_tsv_file_name}",
            index=False,
            sep="\t",
        )
        print(df_clusters)


if __name__ == "__main__":
    clustering_results_to_map_dataframes()
