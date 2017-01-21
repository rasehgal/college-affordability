"""meeting space for all files to do their thang"""

import sys
import studio
import tuition

rent = "studio.csv"
tuit = "unitui.csv"

def main():
   """test file func sharing"""
   studio.fscan(rent)
   tuition.fscan(tuit)
   pass

if __name__ == '__main__':
    sys.exit(main())
