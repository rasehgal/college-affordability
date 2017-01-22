"""Functions for unitui.csv, take in university and spit out tuition and state"""
import sys

filename = "unitui.csv"

def main():
    """Main entry point for the script."""
    fscan(filename)
    pass

def get_tuition():
    """Return tuition price for this university"""
    pass

def fscan(filename):
    """Scan in file as a dictionary"""
    f = open(filename, "r")
    searchlines = f.readlines()
    f.close()
    d = {}
    for line in searchlines:
#        print line
        line = line.split(",")
        d[line[5]] = [line[6],line[7]+line[8]]
    #print d
    pass

if __name__ == '__main__':
    sys.exit(main()) 

