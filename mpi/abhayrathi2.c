#include <stdio.h>
#include <omp.h>

double multiply_reduction(const double *a,const double * b ,int n) 
{
    double product = 1.0;
    #pragma omp parallel for reduction(*:product)
    for (int i = 0; i < n; i++) 
    {
        double sum = 0.0;
        int thread_id = omp_get_thread_num();
        product *= (a[i]*b[i]);
        sum += product;
        printf("Thread ID: %d product during each iteration: %f\n", thread_id, product );
        
    }

    return product;
}

int main(void) {
    int n = 15;
    double a[n];
    double b[n];
    for (int i = 0; i < n; i++) {
        a[i] = i + 2+i;
        b[i] = i + 1;
    }

    double result = multiply_reduction(a,b,n);
    printf("Result: %lf\n", result);
    printf("submitted by Abhay Rathi 20BCE2905");

    return 0;
}