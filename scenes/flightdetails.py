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
# 8×8 logo matrices keyed by ICAO callsign prefixes
LOGOS = {
    "AAL": [  # American mainline
        [(0,0,255)]*3 + [(255,255,255)] + [(255,0,0)]*3,
        [(0,0,255)]*3 + [(255,255,255)] + [(255,0,0)]*3,
        [(0,0,255)]*2 + [(255,255,255)]*2 + [(255,0,0)]*4,
        [(0,0,255)] + [(255,255,255)]*3 + [(255,0,0)]*4,
        [(255,255,255)]*4 + [(255,0,0)]*4,
        [(255,255,255)]*4 + [(255,0,0)]*4,
        [(255,255,255)]*5 + [(255,0,0)]*3,
        [(255,255,255)]*5 + [(255,0,0)]*3,
    ],
    "ENY": [  # Envoy Air (American Eagle)
        [(0,0,255)]*3 + [(255,255,255)] + [(255,0,0)]*3,
        [(0,0,255)]*3 + [(255,255,255)] + [(255,0,0)]*3,
        [(0,0,255)]*2 + [(255,255,255)]*2 + [(255,0,0)]*4,
        [(0,0,255)] + [(255,255,255)]*3 + [(255,0,0)]*4,
        [(255,255,255)]*4 + [(255,0,0)]*4,
        [(255,255,255)]*4 + [(255,0,0)]*4,
        [(255,255,255)]*5 + [(255,0,0)]*3,
        [(255,255,255)]*5 + [(255,0,0)]*3,
    ],
    "PDT": None,
    "UAL": [  # United mainline
        [(128,128,128)]*3 + [(255,255,255)] + [(0,0,255)] + [(255,255,255)] + [(0,0,255)] + [(128,128,128)],
        [(128,128,128)]*2 + [(255,255,255)]*4 + [(128,128,128)]*2,
        [(128,128,128)] + [(255,255,255)] + [(128,128,128)] + [(0,0,255)]*2 + [(128,128,128)]*2,
        [(255,255,255)]*3 + [(0,0,255)]*2 + [(255,255,255)]*3,
        [(255,255,255)] + [(0,0,255)]*2 + [(255,255,255)]*2 + [(0,0,255)]*2 + [(255,255,255)],
        [(255,255,255)]*8,
        [(128,128,128)]*8,
        [(128,128,128)]*8,
    ],
    "GJS": None,  # GoJet Express - same as United
    "SKW": None,  # Air Wisconsin Express
    # assign after dict definition to avoid recursion
    "DAL": [  # Delta mainline
        [(0,0,128)]*2 + [(255,255,255)]*3 + [(255,0,0)]*3,
        [(0,0,128)] + [(255,255,255)]*5 + [(255,0,0)]*2,
        [(255,255,255)]*2 + [(255,0,0)] + [(255,255,255)]*3 + [(255,0,0)],
        [(255,255,255)]*2 + [(255,0,0)] + [(255,255,255)]*4,
        [(255,255,255)]*8,
        [(200,200,200)]*8,
        [(255,255,255)]*8,
        [(255,255,255)]*8,
    ],
    "EDV": None,  # Endeavor Air (Delta Connection)
    "NKS": [  # Spirit
        [(255,255,0)]*8,
        [(255,255,0)]*8,
        [(255,255,0)]*2 + [(255,255,255)]*4 + [(255,255,0)]*2,
        [(255,255,0)]*2 + [(255,255,255)]*4 + [(255,255,0)]*2,
        [(255,255,0)]*2 + [(255,255,255)]*4 + [(255,255,0)]*2,
        [(255,255,0)]*2 + [(255,255,255)]*4 + [(255,255,0)]*2,
        [(255,255,0)]*8,
        [(255,255,0)]*8,
    ],
    "FFT": [  # Frontier
        [(0,128,0)]*6 + [(255,255,255)]*2,
        [(0,128,0)]*6 + [(255,255,255)]*2,
        [(0,128,0)]*7 + [(255,255,255)],
        [(0,128,0)]*7 + [(255,255,255)],
        [(255,255,255)]*8,
        [(255,255,255)]*8,
        [(255,255,255)]*8,
        [(255,255,255)]*8,
    ],
    "SWA": [  # Southwest
        [(0,0,255)]*3 + [(255,0,0)] + [(255,255,0)]*2 + [(0,0,255)],
        [(0,0,255)] + [(255,0,0)] + [(255,255,0)]*2 + [(255,0,0)] + [(0,0,255)],
        [(255,255,0)]*8,
        [(255,255,0)]*8,
        [(255,255,255)]*8,
        [(0,0,255)]*8,
        [(0,0,255)]*8,
        [(0,0,255)]*8,
    ],
    "ACA": [  # Air Canada
        [(0,51,102)]*3 + [(255,255,255)] + [(0,51,102)]*3,
        [(0,51,102)] + [(255,255,255)]*6 + [(0,51,102)],
        [(255,255,255)]*8,
        [(255,255,255)]*8,
        [(255,255,255)]*8,
        [(255,255,255)]*8,
        [(0,51,102)]*8,
        [(0,51,102)]*8,
    ],
    "AFR": [  # Air France
        [(0,51,153)]*2 + [(255,255,255)] + [(204,0,0)] + [(255,255,255)] + [(0,51,153)]*2,
        [(0,51,153)]*8,
        [(255,255,255)]*8,
        [(204,0,0)]*8,
        [(255,255,255)]*8,
        [(0,51,153)]*8,
        [(255,255,255)]*8,
        [(204,0,0)]*8,
    ],
    "AMX": [  # Aeromexico
        [(0,0,128)]*5 + [(255,0,0)]*3,
        [(0,0,128)]*5 + [(255,0,0)]*3,
        [(0,0,128)]*8,
        [(255,255,255)]*8,
        [(0,0,128)]*8,
        [(0,0,128)]*8,
        [(0,0,128)]*5 + [(255,0,0)]*3,
        [(0,0,128)]*5 + [(255,0,0)]*3,
    ],
    "EIN": [  # Aer Lingus (shamrock green)
        [(0,128,0)]*4 + [(255,255,255)]*4,
        [(0,128,0)]*8,
        [(0,128,0)]*8,
        [(255,255,255)]*8,
        [(0,128,0)]*4 + [(255,255,255)]*4,
        [(255,255,255)]*8,
        [(0,128,0)]*8,
        [(0,128,0)]*8,
    ],
    "ETD": [  # Ethiopian Airlines
        [(0,128,0),(0,128,0),(255,255,0),(255,255,0),
         (255,0,0),(255,0,0),(0,128,0),(0,128,0)],
        [(0,128,0)]*8,
        [(255,255,0)]*8,
        [(255,0,0)]*8,
        [(0,128,0)]*8,
        [(255,255,0)]*8,
        [(255,0,0)]*8,
        [(0,128,0)]*8,
    ],
    "QTR": [  # Qatar Airways
        [(128,0,0)]*8,
        [(128,0,0)]*8,
        [(192,192,192)]*8,
        [(128,0,0)]*8,
        [(192,192,192)]*8,
        [(128,0,0)]*8,
        [(128,0,0)]*8,
        [(192,192,192)]*8,
    ],
}

# Now assign regional/international entries that match their mainlines
for regional in ("GJS", "SKW"):
    LOGOS[regional] = LOGOS["UAL"]
for regional in ("EDV"):
    LOGOS[regional] = LOGOS["DAL"]
for regional in ("JZA"):
    LOGOS[regional] = LOGOS["ACA"]
for regional in ("PDT"):
    LOGOS[regional] = LOGOS["AAL"]

class FlightDetailsScene(object):
    def __init__(self):
        super().__init__()

    @Animator.KeyFrame.add(0)
    def flight_details(self):
        if not self._data:
            return

        # Clear area
        self.draw_square(
            0,
            BAR_STARTING_POSITION[1] - (FLIGHT_NO_TEXT_HEIGHT // 2),
            screen.WIDTH - 1,
            BAR_STARTING_POSITION[1] + (FLIGHT_NO_TEXT_HEIGHT // 2),
            colours.BLACK,
        )

        flight_no_text_length = 0
        callsign = None
        if self._data[self._data_index].get("callsign") and self._data[self._data_index]["callsign"] != "N/A":
            callsign = self._data[self._data_index]["callsign"]
            for ch in callsign:
                ch_length = graphics.DrawText(
                    self.canvas, FLIGHT_NO_FONT,
                    FLIGHT_NO_POSITION[0] + flight_no_text_length,
                    FLIGHT_NO_POSITION[1],
                    FLIGHT_NUMBER_NUMERIC_COLOUR if ch.isnumeric() else FLIGHT_NUMBER_ALPHA_COLOUR,
                    ch,
                )
                flight_no_text_length += ch_length

        icao3 = callsign[:3] if callsign and len(callsign) >= 3 else None

        if icao3 in LOGOS:
            logo = LOGOS[icao3]
            x0 = flight_no_text_length + BAR_PADDING
            y0 = BAR_STARTING_POSITION[1] - 4
            for r in range(8):
                for c in range(8):
                    rr, gg, bb = logo[r][c]
                    col = graphics.Color(rr, gg, bb)
                    self.canvas.SetPixel(x0 + c, y0 + r, col.red, col.green, col.blue)
        else:
            # Default dividing bar logic with optional index text
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
                    self.canvas, fonts.extrasmall,
                    DATA_INDEX_POSITION[0], DATA_INDEX_POSITION[1],
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
