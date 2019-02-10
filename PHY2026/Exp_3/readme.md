## chi_square_line.py && Chi_Square_Line.py

chi_square_line imports the chi squared fitting function from Chi_Square_Line.
This plots the results for Part 1 of the Thermoelectric Effect experiment.

To run use:

```
chi_square_line.py
```

This returns an array of the best fitting parameters and covariance matrix.

The first digonal element of the covariance matrix is the square error in gradient and the second is the square error in intercept.
In this case, we have just limited it to the gradient, i.e. no intercept in function.