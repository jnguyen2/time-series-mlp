import sys
import pprint

import geo
from parsedata import parse_csv


def main(args):
    if len(args) < 2:
        return

    fname = args[1]

    data = parse_csv(fname)
    labels = data[0]

    lat_idx = labels.index('latitude')
    lon_idx = labels.index('longitude')

    lat = data[2549][lat_idx]
    lon = data[2549][lon_idx]

    loc_conv = geo.LocationConverter()
    pp = pprint.PrettyPrinter(indent=4)

    raw_loc = loc_conv.coord_to_zip(lat, lon)

    pp.pprint(raw_loc)


if __name__ == '__main__':
    main(sys.argv)
