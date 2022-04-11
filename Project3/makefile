main: main.o
	g++ -o main main.o

main.o: main.cpp
	g++ -c main.cpp basic.h

.PHONY : clean
clean :
	-rm *.o $(objects) main *.gch
