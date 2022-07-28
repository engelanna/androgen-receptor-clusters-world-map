import pydeck
import pandas as pd


def build_deck_renderer(minimum_sequence_identity: float):
    df = pd.read_csv(
        f"assets/tsv/map_ready_dataframes/min-seq-id-{minimum_sequence_identity:.3f}.tsv",
        sep="\t",
    )

    color_lookup = pydeck.data_utils.assign_random_colors(df["ClusterName"])
    df["ClusterColor"] = df.apply(
        lambda row: color_lookup.get(row["ClusterName"]), axis=1
    )
    color_lookup = pydeck.data_utils.assign_random_colors(df["SampleName"])
    df["SampleColor"] = df.apply(
        lambda row: color_lookup.get(row["SampleName"]), axis=1
    )

    arc_layer = pydeck.Layer(
        "ArcLayer",
        data=df,
        get_source_position=["ClusterLongitude", "ClusterLatitude"],
        get_target_position=["PopulationLongitude", "PopulationLatitude"],
        get_source_color="ClusterColor",
        get_target_color="SampleColor",
        pickable=True,
        auto_highlight=True,
    )

    view_state = pydeck.ViewState(
        latitude=0.0,
        longitude=0.0,
        zoom=0,
    )

    TOOLTIP_TEXT = {
        "html": "{S000} jobs <br /> Home of commuter in red; work location in green"
    }

    # deck_renderer = \
    return pydeck.Deck(arc_layer, initial_view_state=view_state, tooltip=TOOLTIP_TEXT)
    # deck_renderer.to_html("arc_layer.html")
