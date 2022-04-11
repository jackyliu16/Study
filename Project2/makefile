CC=g++

main: main.o
	$(CC) -o main main.o

main.o: main.cpp basic.h
	$(CC) -c main.cpp -o main.o -I.
clean:
	rm -rf *.o main
