import os
import subprocess

files = [f for f in os.listdir(".") if os.path.isfile(f) and ".png" in f]

for f in files:
    new_f = f[:-3] + "pdf"
    try:
        subprocess.call(['convert', f, new_f ])
        print "converting %s" %f
    except OSError:
        print "%s exists already" % new_f
