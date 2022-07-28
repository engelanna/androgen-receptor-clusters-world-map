import pydeck
import pandas as pd


def build_deck_renderer(minimum_sequence_identity: float):
    df = pd.read_csv(
        f"assets/tsv/map_ready_dataframes/min-seq-id-{minimum_sequence_identity:.3f}.tsv",
        sep="\t",
    )

    color_lookup = pydeck.data_utils.assign_random_colors(df["Cluster name"])
    df["Color"] = df.apply(lambda row: color_lookup.get(row["Cluster name"]), axis=1)

    # Specify a deck.gl ArcLayer
    arc_layer = pydeck.Layer(
        "ArcLayer",
        data=df,
        get_source_position=["Longitude", "Latitude"],
        get_target_position=[5, 20],
        get_source_color=[255, 100, 0],
        get_target_color="Color",
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
