"""meeting space for all files to do their thang"""

import sys
import studio
import tuition
import city

rent = "studio.csv"
tuit = "unitui.csv"
cities = "unicity.csv"

def main():
   """test file func sharing"""
   studio.fscan(rent)
   tuition.fscan(tuit)
   city.fscan(cities)
   pass

if __name__ == '__main__':
    sys.exit(main())
