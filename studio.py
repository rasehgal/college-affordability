"""Functions for studio.csv, take in city and spit out most recent rent/mo"""
import sys

filename = "studio.csv"


def main():
    """Main entry point for the script."""
    fscan(filename)
    pass

def get_rent():
    """Return a list of tuples containing the top grossing movies of 2013 and link to their IMDB
    page."""
    pass

def fscan(filename):
    """Scan in file as a dictionary"""
    f = open(filename, "r")
    searchlines = f.readlines()
    f.close()
    for line in searchlines:
    	print line
    pass

if __name__ == '__main__':
    sys.exit(main())
