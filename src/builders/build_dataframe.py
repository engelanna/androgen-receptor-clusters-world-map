import pandas as pd


class BuildDataframe:
    def __call__(self, minimum_sequence_identity: float):
        df = pd.read_csv(
            f"assets/tsv/map_ready_dataframes/min-seq-id-{minimum_sequence_identity}.tsv",
            sep="\t",
        )

        return df
