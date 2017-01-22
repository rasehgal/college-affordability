"""Functions for unitui.csv, take in university and spit out tuition and state"""
import sys

filename = "unitui.csv"
d = {}
univ = "Truckee Meadows Community College"

def main():
   """Main entry point for the script."""
   get_state(univ)
   get_tuition(univ)
   pass

def get_tuition(uni_name):
   """Return tuition price for this university"""
   if uni_name in d:
      print(d[uni_name][1])
   pass

def get_state(uni_name):
   """Return state initials for this university"""
   fscan(filename)
   if uni_name in d:
      print(d[uni_name][0])
   pass

def fscan(filename):
   """Scan in file as a dictionary"""
   f = open(filename, "r")
   searchlines = f.readlines()
   f.close()
   for line in searchlines:
#      print line
      line = line.split(",")
      tuition = line[7]+line[8]
      tuition = tuition.strip('"')
      d[line[5]] = [line[6],int(tuition)]
#   print d
   pass

if __name__ == '__main__':
   sys.exit(main()) 

