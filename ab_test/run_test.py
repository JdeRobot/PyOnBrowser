import os

TestFile=os.environ['PYONBROWSERTEST']
execfile("EHAL.py")
execfile(TestFile)
