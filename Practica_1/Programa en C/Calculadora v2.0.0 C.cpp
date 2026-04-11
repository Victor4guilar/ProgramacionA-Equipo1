//Programa: Calculadora básica
//Autor: Equipo 1 SD
//Version: 2.0.0
//Descripcion: Calcula suma, resta, multiplicación y división

#include <stdio.h>

int main() {
    int operacion;
    float N1, N2;

    printf("Bienvenido, selecciona que operacion deseas realizar:\n");
    printf("1. Suma\n");
    printf("2. Resta\n");
    printf("3. Multiplicacion\n");
    printf("4. Division\n");

    printf("Operacion: ");
    if (scanf("%d", &operacion) != 1) {
        printf("Error: Debes ingresar un numero valido.\n");
        return 1;
    }

    if (operacion >= 1 && operacion <= 4) {

        printf("Ingresa el dato 1: ");
        if (scanf("%f", &N1) != 1) {
            printf("Error: Debes ingresar solo numeros.\n");
            return 1;
        }

        printf("Ingresa el dato 2: ");
        if (scanf("%f", &N2) != 1) {
            printf("Error: Debes ingresar solo numeros.\n");
            return 1;
        }

        if (operacion == 1) {
            printf("La suma es: %.2f\n", N1 + N2);

        } else if (operacion == 2) {
            printf("La resta es: %.2f\n", N1 - N2);

        } else if (operacion == 3) {
            printf("La multiplicacion es: %.2f\n", N1 * N2);

        } else if (operacion == 4) {
            if (N2 == 0) {
                printf("Error: No se puede dividir entre cero.\n");
            } else {
                printf("La division es: %.2f\n", N1 / N2);
            }
        }

    } else {
        printf("Opcion no valida\n");
    }

    return 0;
}