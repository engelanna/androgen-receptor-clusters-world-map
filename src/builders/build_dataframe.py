import pandas as pd
import pydeck

from src.loaders import ColorLookup


class BuildDataframe:
    def __call__(self, minimum_sequence_identity: float):
        df = pd.read_csv(
            f"assets/tsv/map_ready_dataframes/min-seq-id-{minimum_sequence_identity}.tsv",
            sep="\t",
        )
        color_lookup = ColorLookup().assign_colors(df["ClusterName"])
        df["Color"] = df.apply(lambda row: color_lookup.get(row["ClusterName"]), axis=1)
        df["Elevation"] = [0.9 if x == [255, 255, 255] else 1.0 for x in df["Color"]]

        return df
