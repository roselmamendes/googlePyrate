from google_pyrate.google_pyrate import GooglePyrate
import sys

if __name__ == '__main__':
    google_pyrate = GooglePyrate()
    google_pyrate.show_the_results_for(sys.argv[1])
