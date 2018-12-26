#include <stdio.h>
#include <math.h>

int main() {
    FILE *fptr;
    double h = 6.63e-34;
    double mag_const = 4 * 3.14159e-7;
    double freq, B, I, r;
    float val = 4/5;
    double err_I, err_B;

    fopen("mag_vals.txt", "r+a");
    

if(fptr != NULL) {
    for(int i = 0; i < 22; i++) {
    printf("Enter a value for the current error: \n");
    scanf("%lf", &I);

    err_I = pow(I, 2);
    // printf("%lf", err_I);
    double init_val = err_I + 0.00871;
    printf("Init val: %lf\n", init_val);
    printf("%le\n", B);
    err_B = 3.836485e-3 * sqrt(init_val);
    printf("Error in B is: %le\n", err_B);
    fprintf(fptr, "%le\n", err_B);
    I = 0;
    
    }
    return 0;
}
else {
    printf("File did not open.\n");
    return 1;
}
}