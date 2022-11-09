from typing import Tuple
from colorthief import ColorThief


class PaletteMaker:
    def make(self, image):
        color_thief = ColorThief(image)
        palette = color_thief.get_palette(color_count=10, quality=10)

        return {
            "bg_color": self.get_darkest_color(palette),
            "alt_bg_color": self.get_darkest_color(palette),
            "fg_color": self.get_brightest_color(palette),
            "alt_fg_color": self.get_brightest_color(palette),
        }

    def get_brightest_color(self, palette):
        brightest_color = (0, 0, 0)

        for color in palette:
            if sum(color) > sum(brightest_color):
                brightest_color = color

        palette.remove(brightest_color)
        return self.get_hex(brightest_color)

    def get_darkest_color(self, palette):
        darkest_color = (255, 255, 255)

        for color in palette:
            if sum(color) < sum(darkest_color):
                darkest_color = color

        palette.remove(darkest_color)
        return self.get_hex(darkest_color)

    def get_hex(self, rgb_tuple: Tuple[int, int, int]):
        return "#%02x%02x%02x" % rgb_tuple
