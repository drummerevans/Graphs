## refractray.c

To run in Mac use:

```bash
// this compiles the program
gcc -c *.c
gcc refractray.o nrutil.o -lm -o refractray

./refractray

// as an example input use: ./refractray test.data 0.5 1e-4 
Usage refractray outfile phi0(deg) dtheta(rad)

// to see all the data and press q to escape
more test.dat
```

To run in Windows use:

```bash
// this compiles the program
gcc -c *.c
gcc refractray.o nrutil.o -lm -o refractray

// remember the .exe extension!
./refractray.exe

// as an example input use: ./refractray.exe test.data 0.5 1e-4 
Usage refractray outfile phi0(deg) dtheta(rad)

// to see all the data and press q to escape
more test.dat
```