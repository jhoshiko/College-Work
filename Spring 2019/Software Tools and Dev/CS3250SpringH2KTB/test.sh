#!/bin/sh

cd example
rm -f *.class
javac *.java
cd ..
./run_unittest.py -v

