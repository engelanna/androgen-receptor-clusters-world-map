import pydeck
import pandas as pd


def build_deck_renderer(minimum_sequence_identity: float):
    df = pd.read_csv(
        f"assets/tsv/map_ready_dataframes/min-seq-id-{minimum_sequence_identity:.3f}.tsv",
        sep="\t",
    )
    color_lookup = pydeck.data_utils.assign_random_colors(df["ClusterName"])
    df["Color"] = df.apply(lambda row: color_lookup.get(row["ClusterName"]), axis=1)
    df["Elevation"] = pd.Series([1000 for x in range(len(df.index))])

    # get_source_position=["Longitude", "Latitude"],
    # get_source_color="Color",
    layer = pydeck.Layer(
        "ColumnLayer",
        data=df,
        get_position=["Longitude", "Latitude"],
        get_elevation="Elevation",
        elevation_scale=10000,
        radius=50000,
        get_fill_color="Color",
        pickable=True,
        auto_highlight=True,
    )
    view_state = pydeck.ViewState(
        longitude=0,
        latitude=0,
        zoom=0,
        min_zoom=0,
        max_zoom=15,
        pitch=0,
        bearing=0,
    )
    tooltip = {  # either use "text", or "html"
        "html": "<a href={SampleLink}>{SampleName}</a>",
        # "style": {"color": "red"},
        "className": "interactive",
    }
    # deck_renderer = \
    return pydeck.Deck(
        layer,
        initial_view_state=view_state,
        map_style="road",
        tooltip=tooltip,
    )
    # deck_renderer.to_html("layer.html")


"""
tooltip (bool or dict of {str: str}, default True) – If True/False,
toggles a default tooltip on visualization hover.

"""
