from pandas import read_csv
from pandas.core.series import Series
from pytest import fixture

from src import ScatterSameCoordinatePoints


class TestScatterSameCoordinatePoints:
    @fixture
    def column_of_latitudes(self) -> Series:
        return read_csv(
            "assets/tsv/map_ready_dataframes/min-seq-id-0.995.tsv", sep="\t"
        )["Latitude"]

    @fixture
    def column_of_longitudes(self) -> Series:
        return read_csv(
            "assets/tsv/map_ready_dataframes/min-seq-id-0.995.tsv", sep="\t"
        )["Longitude"]

    def test_scattering_latitudes(self, column_of_latitudes: Series):
        expected = len(column_of_latitudes)
        actual = len(set(ScatterSameCoordinatePoints()(column_of_latitudes)))

        assert expected == actual

    def test_scattering_longitudes(self, column_of_longitudes: Series):
        expected = len(column_of_longitudes)
        actual = len(set(ScatterSameCoordinatePoints()(column_of_longitudes)))

        assert expected == actual
