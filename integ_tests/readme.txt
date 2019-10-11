Integration tests. To run them just
	./runtests.sh
To create a test, make a directory ending in _test. Inside there has to be:
	- A Python file to be translated for example this.py
	- A correct output file this.py.out. To create one, you can run the test, make it fail and copy the reported this.py.out file into this.out.ok
		after checking it is correct.
	- A correct output file which the data log of emulated sensors, for example V.out.ok. Again,  you can run the test, make it fail and copy the reported V.py.out file into V.out.ok
		after checking it is correct.
