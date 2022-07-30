import pydeck
import pandas as pd

from . import BuildDataframe


class BuildDeckRenderer:
    def __call__(self, minimum_sequence_identity: str):
        df = BuildDataframe()(minimum_sequence_identity)

        cluster_names_to_indexes = {}
        for cluster_index, cluster_name in list(enumerate(df["ClusterName"])):
            cluster_names_to_indexes[cluster_name] = cluster_index

        layer = pydeck.Layer(
            "ColumnLayer",
            data=df,
            get_position=["Longitude", "Latitude"],
            get_elevation="Elevation",
            elevation_scale=2500000,
            radius=125000,
            get_fill_color="Color",
            pickable=True,
            auto_highlight=True,
        )
        view_state = pydeck.ViewState(
            longitude=0,
            latitude=0,
            zoom=1,
            min_zoom=0,
            max_zoom=15,
            pitch=0,
            bearing=0,
        )
        tooltip = {
            "html": (
                '<a href="{SampleLink}">{SampleName}</a> '
                'from <a href="{PopulationLink}">{PopulationDescription}</a><br>'
                "{DataCollection}"
            ),
        }
        return pydeck.Deck(
            layer,
            initial_view_state=view_state,
            map_style="light",
            tooltip=tooltip,
        )
