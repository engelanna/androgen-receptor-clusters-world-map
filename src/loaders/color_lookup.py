from collections import Counter, OrderedDict
import random


class ColorLookup:
    def __init__(self):
        self.preset_colors_remaining = [
            [255, 255, 255],
            [255, 255, 0],
            [255, 0, 0],
            [0, 255, 0],
            [0, 0, 255],
            [255, 165, 0],
        ]

    def assign_colors(self, data_vector):
        """Produces lookup table keyed by each class of data, with value as an RGB array

        Parameters
        ---------
        data_vector : list
            Vector of data classes to be categorized, passed from the data itself

        Returns
        -------
        collections.OrderedDict
            Dictionary of random RGBA value per class, keyed on class
        """
        classes = [item[0] for item in Counter(data_vector).most_common()]
        colors = []
        for _ in classes:
            colors.append(self._next_rgb())
        return OrderedDict([item for item in zip(classes, colors)])

    def _next_rgb(self):
        if self.preset_colors_remaining:
            return self.preset_colors_remaining.pop(0)
        else:
            return [round(random.random() * 255) for _ in range(0, 3)]
