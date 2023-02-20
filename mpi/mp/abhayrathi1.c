#include <stdio.h>
#include <omp.h>

double dot_product(const double *a, const double *b, int n) 
{
    double sum = 0.0;

    #pragma omp parallel for reduction(+:sum)
        for (int i = 0; i < n; i++) 
        {
            int thread_id = omp_get_thread_num();
            printf("Thread ID: %d sum during each iteration: %f\n", thread_id, sum);
            sum += a[i] * b[i];
        }
    
    return sum;
}

int main(void) 
{
    int n = 100;
    double a[n], b[n];

    for (int i = 0; i < n; i++) 
    {
        a[i] = i;
        b[i] = i;
    }

    double result = dot_product(a, b, n);
    printf("Result: %lf\n", result);
    
    printf("-----------------------------\n");

    printf("submitted by Abhay Rathi 20BCE2905");

   return 0;
   
}