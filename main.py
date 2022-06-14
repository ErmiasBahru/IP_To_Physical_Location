import argparse
import geoip2.database

def print_result(trg_ip):
    with geoip2.database.Reader('geolite2_city.mmdb') as geo:
        res = geo.city(trg_ip)
        city = res.city.name
        region = res.subdivisions.most_specific.name
        country = res.country.name
        latitude = res.location.latitude
        longitude = res.location.longitude

        print(f'[*] Target: {trg_ip} geo-located at:')
        print(f'{"":>3}[+] {city}, {region}, {country}')
        print(f'{"":>3}[+] Latitude: {latitude}, Longitude: {longitude}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        usage='python main.py TARGET_IP'
    )
    parser.add_argument('target_ip', type=str, metavar='TARGET_IP',
                        help='IP address of the target')
    print_result(parser.parse_args().target_ip)