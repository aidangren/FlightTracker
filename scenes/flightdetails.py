from utilities.animator import Animator
from setup import colours, fonts, screen
from rgbmatrix import graphics

# Setup constants
BAR_STARTING_POSITION = (0, 18)
BAR_PADDING = 2

FLIGHT_NO_POSITION = (1, 21)
FLIGHT_NO_TEXT_HEIGHT = 8
FLIGHT_NO_FONT = fonts.small

FLIGHT_NUMBER_ALPHA_COLOUR = colours.BLUE
FLIGHT_NUMBER_NUMERIC_COLOUR = colours.BLUE_LIGHT

DATA_INDEX_POSITION = (52, 21)
DATA_INDEX_TEXT_HEIGHT = 6
DATA_INDEX_FONT = fonts.extrasmall

DIVIDING_BAR_COLOUR = colours.GREEN
DATA_INDEX_COLOUR = colours.GREY

# 8×8 logo matrices for ORD-serving carriers (Winter 2024, excluding express)
LOGOS = {
    "AA": [
        [(0,0,255)]*3 + [(255,255,255)] + [(255,0,0)]*3,
        [(0,0,255)]*3 + [(255,255,255)] + [(255,0,0)]*3,
        [(0,0,255)]*2 + [(255,255,255)]*2 + [(255,0,0)]*4,
        [(0,0,255)] + [(255,255,255)]*3 + [(255,0,0)]*4,
        [(255,255,255)]*4 + [(255,0,0)]*4,
        [(255,255,255)]*4 + [(255,0,0)]*4,
        [(255,255,255)]*5 + [(255,0,0)]*3,
        [(255,255,255)]*5 + [(255,0,0)]*3,
    ],
    "UA": [
        [(128,128,128)]*3 + [(255,255,255)] + [(0,0,255)] + [(255,255,255)] + [(0,0,255)] + [(128,128,128)],
        [(128,128,128)]*2 + [(255,255,255)]*4 + [(128,128,128)]*2,
        [(128,128,128)] + [(255,255,255)] + [(128,128,128)] + [(0,0,255)]*2 + [(128,128,128)]*2,
        [(255,255,255)]*3 + [(0,0,255)]*2 + [(255,255,255)]*3,
        [(255,255,255)] + [(0,0,255)]*2 + [(255,255,255)]*2 + [(0,0,255)]*2 + [(255,255,255)],
        [(255,255,255)]*8,
        [(128,128,128)]*8,
        [(128,128,128)]*8,
    ],
    "DL": [
        [(0,0,128)]*2 + [(255,255,255)]*3 + [(255,0,0)]*3,
        [(0,0,128)] + [(255,255,255)]*5 + [(255,0,0)]*2,
        [(255,255,255)]*2 + [(255,0,0)] + [(255,255,255)]*3 + [(255,0,0)],
        [(255,255,255)]*2 + [(255,0,0)] + [(255,255,255)]*4,
        [(255,255,255)]*8,
        [(200,200,200)]*8,
        [(255,255,255)]*8,
        [(255,255,255)]*8,
    ],
    "NK": [
        [(255,255,0)]*8,
        [(255,255,0)]*8,
        [(255,255,0)]*2 + [(255,255,255)]*4 + [(255,255,0)]*2,
        [(255,255,0)]*2 + [(255,255,255)]*4 + [(255,255,0)]*2,
        [(255,255,0)]*2 + [(255,255,255)]*4 + [(255,255,0)]*2,
        [(255,255,0)]*2 + [(255,255,255)]*4 + [(255,255,0)]*2,
        [(255,255,0)]*8,
        [(255,255,0)]*8,
    ],
    "F9": [
        [(0,128,0)]*6 + [(255,255,255)]*2,
        [(0,128,0)]*6 + [(255,255,255)]*2,
        [(0,128,0)]*7 + [(255,255,255)],
        [(0,128,0)]*7 + [(255,255,255)],
        [(255,255,255)]*8,
        [(255,255,255)]*8,
        [(255,255,255)]*8,
        [(255,255,255)]*8,
    ],
    "WN": [
        [(0,0,255)]*3 + [(255,0,0)] + [(255,255,0)]*2 + [(0,0,255)],
        [(0,0,255)] + [(255,0,0)] + [(255,255,0)]*2 + [(255,0,0)] + [(0,0,255)],
        [(255,255,0)]*8,
        [(255,255,0)]*8,
        [(255,255,255)]*8,
        [(0,0,255)]*8,
        [(0,0,255)]*8,
        [(0,0,255)]*8,
    ],
    "AC": [
        [(255,0,0)]*3 + [(255,255,255)]*2 + [(255,0,0)]*3,
        [(255,0,0)] + [(255,255,255)]*4 + [(255,0,0)],
        [(255,255,255)]*8,
        [(255,255,255)]*8,
        [(255,255,255)]*8,
        [(255,255,0)]*8,
        [(255,0,0)] + [(255,255,255)]*4 + [(255,0,0)],
        [(255,0,0)]*8,
    ],
    "AS": [
        [(0,128,128)]*8,
        [(0,128,128)]*8,
        [(255,255,255)]*8,
        [(255,255,255)]*8,
        [(0,128,128)]*8,
        [(0,128,128)]*8,
        [(255,255,255)]*8,
        [(0,128,128)]*8,
    ],
    "B6": [
        [(0,0,128)]*4 + [(0,128,255)]*4,
        [(0,0,128)]*4 + [(0,128,255)]*4,
        [(255,255,255)]*8,
        [(0,0,128)]*8,
        [(0,128,255)]*8,
        [(0,0,128)]*8,
        [(255,255,255)]*8,
        [(0,128,255)]*8,
    ],
    "EK": [
        [(218,165,32)]*6 + [(255,0,0)]*2,
        [(218,165,32)]*6 + [(255,0,0)]*2,
        [(218,165,32)]*8,
        [(218,165,32)]*8,
        [(255,255,255)]*8,
        [(218,165,32)]*8,
        [(218,165,32)]*6 + [(255,0,0)]*2,
        [(218,165,32)]*6 + [(255,0,0)]*2,
    ],
    "QR": [
        [(128,0,0)]*8,
        [(128,0,0)]*8,
        [(192,192,192)]*8,
        [(128,0,0)]*8,
        [(192,192,192)]*8,
        [(128,0,0)]*8,
        [(128,0,0)]*8,
        [(192,192,192)]*8,
    ],
    "ET": [
        [(0,128,0),(0,128,0),(255,255,0),(255,255,0),(255,0,0),(255,0,0),(0,128,0),(0,128,0)],
        [(0,128,0)]*8,
        [(255,255,0)]*8,
        [(255,0,0)]*8,
        [(0,128,0)]*8,
        [(255,255,0)]*8,
        [(255,0,0)]*8,
        [(0,128,0)]*8,
    ],
    "AM": [
        [(0,0,128)]*6 + [(255,0,0)]*2,
        [(0,0,128)]*6 + [(255,0,0)]*2,
        [(0,0,128)]*8,
        [(255,255,255)]*8,
        [(0,0,128)]*8,
        [(0,0,128)]*6 + [(255,0,0)]*2,
        [(0,0,128)]*6 + [(255,0,0)]*2,
        [(255,255,255)]*8,
    ],
    "EI": [
        [(0,128,0)]*4 + [(255,255,255)]*4,
        [(0,128,0)]*8,
        [(0,128,0)]*8,
        [(255,255,255)]*8,
        [(0,128,0)]*4 + [(255,255,255)]*4,
        [(255,255,255)]*8,
        [(0,128,0)]*8,
        [(0,128,0)]*8,
    ],
}


class FlightDetailsScene(object):
    def __init__(self):
        super().__init__()

    @Animator.KeyFrame.add(0)
    def flight_details(self):
        if len(self._data) == 0:
            return

        # Clear background
        self.draw_square(
            0,
            BAR_STARTING_POSITION[1] - (FLIGHT_NO_TEXT_HEIGHT // 2),
            screen.WIDTH - 1,
            BAR_STARTING_POSITION[1] + (FLIGHT_NO_TEXT_HEIGHT // 2),
            colours.BLACK,
        )

        flight_no_text_length = 0
        flight_no = None
        if self._data[self._data_index]["flights"] and self._data[self._data_index]["flights"] != "N/A":
            flight_no = f'{self._data[self._data_index]["flights"]}'
            for ch in flight_no:
                ch_length = graphics.DrawText(
                    self.canvas,
                    FLIGHT_NO_FONT,
                    FLIGHT_NO_POSITION[0] + flight_no_text_length,
                    FLIGHT_NO_POSITION[1],
                    FLIGHT_NUMBER_NUMERIC_COLOUR if ch.isnumeric() else FLIGHT_NUMBER_ALPHA_COLOUR,
                    ch,
                )
                flight_no_text_length += ch_length

        # decide drawing: bar or logo
        if self._data and flight_no:
            airline_code = flight_no[:2]
        else:
            airline_code = None

        if airline_code in LOGOS:
            # draw 8×8 logo
            logo = LOGOS[airline_code]
            x0 = flight_no_text_length + BAR_PADDING
            y0 = BAR_STARTING_POSITION[1] - 4  # center 8px tall
            for row in range(8):
                for col in range(8):
                    r, g, b = logo[row][col]
                    color = graphics.Color(r, g, b)
                    self.canvas.SetPixel(x0 + col, y0 + row, color.red, color.green, color.blue)
        else:
            # default dividing bar
            if len(self._data) > 1:
                graphics.DrawLine(
                    self.canvas,
                    flight_no_text_length + BAR_PADDING,
                    BAR_STARTING_POSITION[1],
                    DATA_INDEX_POSITION[0] - BAR_PADDING - 1,
                    BAR_STARTING_POSITION[1],
                    DIVIDING_BAR_COLOUR,
                )
                graphics.DrawText(
                    self.canvas,
                    fonts.extrasmall,
                    DATA_INDEX_POSITION[0],
                    DATA_INDEX_POSITION[1],
                    DATA_INDEX_COLOUR,
                    f"{self._data_index + 1}/{len(self._data)}",
                )
            else:
                graphics.DrawLine(
                    self.canvas,
                    flight_no_text_length + BAR_PADDING if flight_no_text_length else 0,
                    BAR_STARTING_POSITION[1],
                    screen.WIDTH,
                    BAR_STARTING_POSITION[1],
                    DIVIDING_BAR_COLOUR,
                )
