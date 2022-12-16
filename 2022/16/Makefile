all: py1 cc1 cc2

py1:
	python p1.py <input.txt

cc1:
	g++ --std=c++17 -O -o p1 p1.cc && ./p1 <input.txt && rm -f p1

cc2:
	g++ --std=c++17 -Ofast -march=native -mtune=native -o p2 p2.cc && ./p2 <input.txt && rm -f p2
