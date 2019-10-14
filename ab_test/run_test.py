#!/usr/bin/python3


import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('testfile', nargs=1, help='test to run')
args = parser.parse_args()
try:
	testData=open(args.testfile[0]).read()
except (OSError, IOError) as e:
	sys.exit('Error!')
exec(testData)

