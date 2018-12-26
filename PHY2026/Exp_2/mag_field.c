#include <stdio.h>
#include <math.h>


int main() {
    FILE *fptr;
    double h = 6.63e-34;
    double mag_const = 4*3.14159e-7;
    double freq, B, I;
    double val = 4/5;

    fopen("mag_vals.txt", "w");
    

if(fptr != NULL) {
    for(int i = 0; i < 22; i++) {
    printf("Enter a value for current: \n");
    scanf("%lf", &I);

    double first = mag_const * pow(0.894427, 3);
    printf("%le", first);
    B = first * (320 / 0.075) * I;

    printf("Number: %d magnetic field value is: %le\n", i, B);
    fprintf(fptr, "%le", B);
    I = 0;
    
    }
    return 0;
}
else {
    printf("File did not open.\n");
    return 1;
}
 
}