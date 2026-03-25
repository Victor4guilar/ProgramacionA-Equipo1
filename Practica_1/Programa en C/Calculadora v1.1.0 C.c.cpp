#include<stdio.h>

int main(){
    float suma;
    float N1, N2;
    // Quitamos "float input;" porque no se usa como variable, sino como función

    printf("Ingresa el dato 1: ");
    scanf("%f", &N1); // Quitamos 'float' de aquí

    printf("Ingresa el dato 2: ");
    scanf("%f", &N2); // Quitamos 'float' de aquí

    suma = N1 + N2;   // Quitamos 'float' de aquí y corregimos el N2N2

    printf("La suma es: %.2f", suma); // Cambiamos print por printf

    return 0;
}
