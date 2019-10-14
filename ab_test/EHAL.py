
sensorFiles=dict([])
class FileData(object):
	data=[]

def readSensor(fname):
	print("reading fake: "+ fname)
	fpath=emulateDir+"/"+fname
	content = []
	isPres=True
	try:
		sensorFiles[fname]
	except KeyError:
		isPres=False
	if not isPres:
		try:
			f = open(fpath)
			content = f.readlines()
		except (OSError, IOError) as e:
			print("error reading from fake: "+file+" "+err);	#stderr?
			return False
	else:
		content = sensorFiles[fname].data;
	rest = content[0].rstrip()
	fd = FileData()
	fd.data = content[1:]
	sensorFiles[fname]=fd
	return float(rest)

def writeSensor(fname, val):
	print("writing fake: "+str(val)+"->"+fname)
	fpath = emulateDir + "/"+fname+".out"
	f=open(fpath, "a+")
	try:
		f.write(str(val)+'\n')
	except (OSError, IOError) as e:
		print("error writing to fake: "+file+" "+err)
		return False
	f.close()
	return True

def getUS ():
	return readSensor('US')

def getIR ():
	return readSensor('IR')

def setV (linearSpeed):
	writeSensor('V', linearSpeed.x)

def setW (angularSpeed):
	writeSensor('W', angularSpeed.x)

def getLaser ():
	print('unimplemented')
	return False

def getEncoders ():
	return ()

def getV ():
	return readSensor('V')

def getW ():
	return readSensor('W')

def getInfrared ():
	o = {Left: readSensor('Infrared'), Right: readSensor('Infrared'), Front: readSensor('Infrared')}
	return o
