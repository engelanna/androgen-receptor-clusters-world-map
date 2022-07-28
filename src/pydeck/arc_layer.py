import pydeck
import pandas as pd


def build_deck_renderer(minimum_sequence_identity: float):
    df = pd.read_csv(
        f"assets/tsv/map_ready_dataframes/min-seq-id-{minimum_sequence_identity:.3f}.tsv",
        sep="\t",
    )

    color_lookup = pydeck.data_utils.assign_random_colors(df["ClusterName"])
    df["Color"] = df.apply(lambda row: color_lookup.get(row["ClusterName"]), axis=1)

    # get_source_position=["Longitude", "Latitude"],
    # get_source_color="Color",
    arc_layer = pydeck.Layer(
        "ScatterplotLayer",
        df,
        pickable=True,
        opacity=0.8,
        stroked=True,
        radius_min_pixels=2,
        line_width_min_pixels=1,
        get_position=["Longitude", "Latitude"],
        radius="exits_radius",
        get_fill_color="Color",
        get_line_color="Color",
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
    return pydeck.Deck(
        arc_layer,
        initial_view_state=view_state,
        map_style="dark",
        map_provider="mapbox",
        tooltip=TOOLTIP_TEXT,
    )
    # deck_renderer.to_html("arc_layer.html")
