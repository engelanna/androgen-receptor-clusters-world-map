from pandas.core.series import Series
from random import uniform


class ScatterSameCoordinatePoints:
    def __call__(self, column: Series):
        unique_values = []

        for _, value in column.iteritems():
            if not value in unique_values:
                unique_values.append(value)
            else:
                while value in unique_values:
                    value = uniform(value - 2.5, value + 2.5)
                unique_values.append(value)

        return Series(list(unique_values))
