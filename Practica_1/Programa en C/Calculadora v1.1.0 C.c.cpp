//Programa: Calculadora de suma
//Autor: Equipo 1 SD
//Version: 1.1.0
//Descripcion: Se agrega entrada de datos por teclado.

#include<stdio.h>

int main(){
    float suma;
    float N1, N2;

    printf("Ingresa el dato 1: ");
    scanf("%f", &N1);

    printf("Ingresa el dato 2: ");
    scanf("%f", &N2);

    suma = N1 + N2;

    printf("La suma es: %.2f", suma); /
    return 0;
}
