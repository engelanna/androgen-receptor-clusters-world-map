import pydeck as pdk
import pandas as pd


def build_deck_renderer(minimum_sequence_identity: float):
    df = pd.read_csv(
        f"assets/tsv/map_ready_dataframes/min-seq-id-{minimum_sequence_identity:.3f}.tsv",
        sep="\t",
    )

    # Specify a deck.gl ArcLayer
    arc_layer = pdk.Layer(
        "ArcLayer",
        data=df,
        get_width="S000 * 2",
        get_source_position=["lng_h", "lat_h"],
        get_target_position=["lng_w", "lat_w"],
        get_tilt=15,
        get_source_color=[*df["Color"], 40],
        get_target_color=[*df["Color"], 0],
        pickable=True,
        auto_highlight=True,
    )

    view_state = pdk.ViewState(
        latitude=37.7576171,
        longitude=-122.5776844,
        bearing=45,
        pitch=50,
        zoom=8,
    )

    TOOLTIP_TEXT = {
        "html": "{S000} jobs <br /> Home of commuter in red; work location in green"
    }

    # deck_renderer = \
    return pdk.Deck(arc_layer, initial_view_state=view_state, tooltip=TOOLTIP_TEXT)
    # deck_renderer.to_html("arc_layer.html")
