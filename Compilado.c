#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Factorial recursivo
unsigned long long factorial_recursivo(int n) {
    if (n == 0 || n == 1) return 1;
    return n * factorial_recursivo(n - 1);
}

// Factorial iterativo
unsigned long long factorial_iterativo(int n) {
    unsigned long long resultado = 1;
    for (int i = 2; i <= n; i++) {
        resultado *= i;
    }
    return resultado;
}

// Medición de tiempo
double medir_tiempo(unsigned long long (*funcion)(int), int n) {
    clock_t inicio = clock();
    funcion(n);
    clock_t fin = clock();
    return (double)(fin - inicio) / CLOCKS_PER_SEC;
}

// Medición de memoria (aproximada: tamaño de la pila + variables locales)
size_t medir_memoria(int n, int recursivo) {
    if (recursivo) {
        return sizeof(unsigned long long) * n; // aprox. stack por llamadas
    } else {
        return sizeof(unsigned long long) + sizeof(int) * n; // aprox. variables en bucle
    }
}

void generar_csv(const char *filename, unsigned long long (*funcion)(int), int recursivo) {
    FILE *f = fopen(filename, "w");
    if (!f) return;
    fprintf(f, "n,tiempo,memoria\n");
    for (int n = 1; n < 500; n++) {
        double tiempo = medir_tiempo(funcion, n);
        size_t memoria = medir_memoria(n, recursivo);
        fprintf(f, "%d,%f,%zu\n", n, tiempo, memoria);
    }
    fclose(f);
}

int main() {
    generar_csv("factorial_recursivo_c.csv", factorial_recursivo, 1);
    generar_csv("factorial_iterativo_c.csv", factorial_iterativo, 0);
    return 0;
}
