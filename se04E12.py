"""

12 - Read a distance in miles and show converted in Km,
The formula for convertion is: K = 1,61 * M, being K
the a distance in quilometers and M in miles.

"""

def main():

    distance_miles = float(input('Type the distance in miles: '))
    distance_km = distance_miles * 1,61
    print(f'The result of convertion Miles in Quilometers: {distance_km}')


if __name__ == '__main_)':
    main()
