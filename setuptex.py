import subprocess

subprocess.call(['pdflatex', 'ma.tex'])

subprocess.call(['bibtex', 'ma.aux'])

subprocess.call(['pdflatex', 'ma.tex'])

subprocess.call(['pdflatex', 'ma.tex'])
