import argparse

parser = argparse.ArgumentParser(description='Check the local weather from your terminal')

parser.add_argument('-c', '--current', action='store_true',
                    help='sum the integers (default: find the max)')

parser.add_argument('-f', '--forecast', nargs='*', choices=range(1, 5), type=int, help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args)
