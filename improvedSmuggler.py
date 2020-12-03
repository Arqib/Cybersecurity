import subprocess
import sys
url = sys.argv[1]
subprocess.check_output([r"sed -i 's/Host.*/Host: {0}/g' temp.txt".format(url)], shell=True),
