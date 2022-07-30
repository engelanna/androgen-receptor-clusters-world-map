import pandas as pd
import pydeck


class BuildDataframe:
    def __call__(self, minimum_sequence_identity: float):
        df = pd.read_csv(
            f"assets/tsv/map_ready_dataframes/min-seq-id-{minimum_sequence_identity}.tsv",
            sep="\t",
        )
        color_lookup = pydeck.data_utils.assign_random_colors(df["ClusterName"])
        df["Color"] = df.apply(lambda row: color_lookup.get(row["ClusterName"]), axis=1)
        df["Elevation"] = pd.Series([1000 for x in range(len(df.index))])

        return df
