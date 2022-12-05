all: py js go cc

py:
	python3 p.py <input.txt

js:
	node p.js <input.txt

go:
	go run p.go <input.txt
	go run p-strings.go <input.txt

cc:
	g++ --std=c++11 -o p p.cc && ./p <input.txt && rm -f p
