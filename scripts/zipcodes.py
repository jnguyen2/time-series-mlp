""" zipcodes.py

Given a dataset with latitudes and longitude values, output a file that
contains all of the zip codes represented in the dataset. This will help
reduce the number of calls to the geocoder.

"""
from geopy.geocoders import Nominatim


class LocationConverter:
    def __init__(self):
        self.geocoder = Nominatim(user_agent='cps360-final-project')

    def coord_to_zip(self, lat, lon):
        """ Find the zip code of the given coordinates.

        Args:
            lat (str): Latitude.
            lon (str): Longitude.

        Returns:
            str: Zipcode.
        """
        query = str(lat) + ', ' + str(lon)
        location = self.geocoder.reverse(query)
        return location.raw['address']['postcode']


def main(args):
    pass


if __name__ == '__main__':
    main()
