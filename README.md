# PyOnBrowser

## Usage
~~~bash
python3 main.py <inputfile> --outfile=<outputfile>
js <outfile>
~~~
If \<outputfile\> is not mentioned, the output file name defaults to \_\_gen\_\_.js
### Compatible versions
- python3 : 3.6.7
- node    : 8.10.0

## Example
### Hello World

The simplest example is to run a hello world program. Open up a python3 file and save it as *helloWorld.py*.
Copy the following line of code into *helloWorld.py*.
~~~python
print ('Hello World!')
~~~

Next, run the following command to generate the javascript file.
~~~bash
python3 main.py helloWorld.py --outfile=out.js
~~~
This generates the file *out.js* which contains the generated code.
*out.js* can be executed in the command line in the following manner
~~~bash
js out.js
~~~
Alternatively, it can be included in a webpage.

### Interaction with WebSim
To program your bot in websim using python3, you can use this tool. The file 'modules/Hal.py' contains the API that is supported.

~~~python
import HAL

HAL.setV (12)
HAL.setW (10)
print ('US = ' + str (HAL.getUS ()))
print ('IR = ' + str (HAL.getIR ()))

print (HAL.getLaser ())
print (HAL.getEncoders ())
~~~
### Execute locally without websim with emulated sensors and actuators
python3 --emulate /tmp/sensors main.py helloWorld.py --outfile=out.js
In the directory, there has to be a file per sensor we want to get (US, IR, etc), one number per line.
After running, a file ending in .out will be appended to with the values which were set to the actuators (V.out, W.out, etc).
### Execute tests
To run integration tests run the command:
~~~sh
/pathinstall/PyOnBrowser/integ_tests/runtests.sh
~~~

Each test is a directory consisting of a python file and a number
of files for input of sensors, the names obtained from the sensors and for the
correct output of the sensors ending in .ok (see
/pathinstall/PyOnBrowser/integ_tests/simpl_test/ for an example).

To run A/B testing (tested against native Python)

~~~sh
/pathinstall/PyOnBrowser/ab_test/runabtest.sh
~~~

A/B testing can be used to obtain correct outputs for integration tests
in some cases.
